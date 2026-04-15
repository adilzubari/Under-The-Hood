---
tags:
  - phase-1
  - error-handling
  - exceptions
  - fundamentals
difficulty: medium
status: written
---

# Error Handling

> **TL;DR:** Use exceptions for *exceptional* conditions, not control flow. Catch the narrowest exception you can. Re-raise with context (`raise X from e`). For business outcomes that can normally fail, return a Result type. For transient failures, retry with backoff.

## 📖 Concept Overview

Error handling is one of the highest-leverage skills: a system that fails gracefully under partial outage is worth orders of magnitude more than one that crashes. The basics are simple — `try/except/else/finally` — but the discipline lies in *what to catch where, what to retry, what to surface, and what to log.*

Two key distinctions:

1. **Exceptional vs expected failures.** Exceptions are for "this normally works; something unusual happened." Expected outcomes (user not found, validation failed) are sometimes better as return values.
2. **Recoverable vs not.** Catch only what you can act on. Catching everything and logging hides real bugs.

## 🔍 Deep Dive

### Exception hierarchy

```
BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 └── Exception
      ├── ArithmeticError
      ├── LookupError (KeyError, IndexError)
      ├── OSError (FileNotFoundError, ConnectionError)
      ├── TypeError
      ├── ValueError
      └── ... your custom exceptions ...
```

Catch `Exception`, not `BaseException` — never swallow `KeyboardInterrupt` or `SystemExit`.

### EAFP vs LBYL

Python idiom: **EAFP** ("easier to ask forgiveness than permission") — try, catch on failure.

```python
# ✅ EAFP — Pythonic
try:
    value = d[key]
except KeyError:
    value = default

# ❌ LBYL — extra check, race-prone in concurrent code
if key in d:
    value = d[key]
else:
    value = default
```

EAFP is faster in the success case (no double-lookup) and free of TOCTOU races (file checked then opened can race). Use LBYL when checking is cheap and exception cost matters in a tight loop.

### Custom exceptions

```python
class BillingError(Exception):
    """Base for billing problems."""

class InsufficientFundsError(BillingError):
    def __init__(self, account_id: str, requested: int, available: int):
        super().__init__(f"insufficient funds in {account_id}: requested {requested}, have {available}")
        self.account_id = account_id
        self.requested = requested
        self.available = available

class ProviderUnavailableError(BillingError): pass
```

Subclass for each *meaningful* category. Add structured attributes (not just a message string) so callers can act programmatically.

### Re-raise with context

```python
def parse_int(s: str) -> int:
    try:
        return int(s)
    except ValueError as e:
        raise ConfigError(f"expected integer in field 'port', got {s!r}") from e
```

`from e` chains the original exception. Tracebacks show both — debuggability without losing context.

### `try/except/else/finally`

```python
try:
    result = do_thing()
except SpecificError as e:
    handle(e)
else:
    # only runs if no exception
    log_success(result)
finally:
    # always runs
    cleanup()
```

Using `else` keeps the success path *out of* the `try` block, narrowing what the `except` catches.

### Context managers for cleanup

```python
# ❌ manual cleanup
f = open("file.txt")
try:
    process(f)
finally:
    f.close()

# ✅ automatic cleanup
with open("file.txt") as f:
    process(f)
```

`contextlib.contextmanager` for custom ones:

```python
from contextlib import contextmanager

@contextmanager
def db_transaction(conn):
    conn.execute("BEGIN")
    try:
        yield conn
        conn.execute("COMMIT")
    except Exception:
        conn.execute("ROLLBACK")
        raise
```

### `contextlib.suppress` for "ignore this specific error"

```python
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove("optional.tmp")
```

Cleaner than `try/except: pass` when you genuinely want to ignore.

### Result types (instead of exceptions)

For *expected* failures (validation, user not found), exceptions can be heavy and force callers to use `try/except` for normal flow. Alternative:

```python
from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")
E = TypeVar("E")

@dataclass
class Ok(Generic[T]):
    value: T

@dataclass
class Err(Generic[E]):
    error: E

Result = Ok[T] | Err[E]

def find_user(id: str) -> Result[User, str]:
    user = db.get(id)
    if user is None:
        return Err("not found")
    return Ok(user)

match find_user("u1"):
    case Ok(user):  print(user.name)
    case Err(msg):  print(f"error: {msg}")
```

Common in Rust, Go-style. In Python, used selectively — exceptions remain idiomatic for most cases.

### Retries with backoff

```python
import time, random
from typing import Callable, TypeVar

T = TypeVar("T")

def retry(fn: Callable[[], T], *, attempts=5, base_delay=0.5,
          retry_on: tuple[type, ...] = (Exception,)) -> T:
    for i in range(attempts):
        try:
            return fn()
        except retry_on as e:
            if i == attempts - 1:
                raise
            delay = base_delay * (2 ** i) + random.uniform(0, 0.1)  # jitter
            time.sleep(delay)
```

Or use `tenacity`:

```python
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    retry=retry_if_exception_type(ConnectionError),
)
def fetch(url): ...
```

Always retry on *idempotent* operations only. Retry on transient errors (network, timeout); don't retry on permanent ones (auth, bad input).

### What to log, what to surface

```python
def handle_request(req):
    try:
        return process(req)
    except UserError as e:
        # expected; surface to user, no stack trace
        return error_response(400, str(e))
    except Exception as e:
        # unexpected; log full context, return generic message
        logger.exception("unhandled error processing request")
        return error_response(500, "internal error")
```

Never expose raw exception messages to external users — they leak internals (file paths, SQL fragments).

## ⚖️ Trade-offs & Pitfalls

- ✅ **Catch when:** you can recover, transform the error, or add context.
- ❌ **Don't catch when:** you can't actually do anything (let it bubble).
- 🐛 **Common mistakes:**
    - `except:` (bare) — catches `KeyboardInterrupt` too. Use `except Exception:`.
    - `except Exception: pass` — silent failures. Always log or re-raise.
    - Catching `Exception` everywhere → masks bugs; catch the narrowest type you actually expect.
    - Using exceptions for control flow on the hot path (Python exceptions cost ~µs each — fine for the rare case, expensive in tight loops).
    - Retrying without backoff → thundering herd.
- 💡 **Rules of thumb:**
    - Catch narrow, raise wide.
    - One catch per responsibility level (request handler, domain operation).
    - `raise X from e` preserves chain. Don't lose tracebacks.
    - Log once per error (at the boundary), not every layer.

## 🎯 Interview Questions

<details>
<summary><strong>Q1: Why is `except:` (bare except) considered bad?</strong></summary>

It catches *every* exception including `KeyboardInterrupt` and `SystemExit` — making the program unkillable from the keyboard and breaking shutdown. It also hides programming bugs (typos, missing imports) by catching `NameError`/`ImportError`. Use `except Exception:` if you really need broad handling.

</details>
<details>
<summary><strong>Q2: When do exceptions hurt performance?</strong></summary>

Raising/catching costs microseconds — fine for the rare case. Expensive in *very* tight loops or as control flow (`for x in iterable: try: ...`). Profile if suspicious. Common idiomatic exception (`StopIteration` ending a `for` loop) is optimized.

</details>
<details>
<summary><strong>Q3: What's wrong with `except Exception as e: log(e); raise`?</strong></summary>

Often nothing — if you're adding context. But: (1) The catch may be at the wrong layer (better to let it bubble to the request boundary). (2) Logging at every layer creates duplicate logs of the same error. (3) Without `from e` or context, you lose the original traceback when re-raising a different exception. Log *once* at the boundary; re-raise without modification deeper inside.

</details>
<details>
<summary><strong>Q4: When would you choose Result types over exceptions?</strong></summary>

For expected-failure cases where the type system should force callers to handle both outcomes (validation, parsing, lookup-or-default). Result types make failure paths visible in signatures (`Result[User, NotFound]` vs `User`). For exceptional cases (network down, programmer error), exceptions remain better — they bubble naturally.

</details>
<details>
<summary><strong>Q5: How would you design retry behavior for an HTTP call?</strong></summary>

Three knobs: (1) **What to retry on** — connection errors, 5xx, 429 (rate limited). Never retry 4xx (it'll fail again). (2) **Backoff** — exponential with jitter, e.g., 1s, 2s, 4s, 8s ± random. (3) **Total budget** — max attempts AND max total time. Combine with circuit breaker for cascading failure protection. Ensure operations are idempotent or use idempotency keys.

</details>
<details>
<summary><strong>Q6: What does `raise X from e` do?</strong></summary>

Sets `X.__cause__ = e`. Tracebacks show both: 'During handling of [original], another exception occurred: [new]'. This preserves the root cause when you wrap an exception in a domain-specific one. Without `from`, Python sets `__context__` instead (still chained, but labeled differently — 'During handling… ').

</details>

## 🏗️ Scenarios

### Scenario: Webhook delivery with intermittent failures

**Situation:** Service POSTs webhooks to customer URLs. Some URLs are flaky (50% success). Some are permanently down (404). Some return 500 occasionally. You need: high delivery rate, no dropped webhooks for transient failures, no infinite retries for dead URLs.

**Constraints:** Each webhook has a max delivery window (24h). Failures recorded for the customer dashboard.

**Approach:** Retry transient errors with exponential backoff + jitter. After max attempts, dead-letter for review. Distinguish HTTP status classes.

**Solution:**

```python
import time, random
import httpx

class TransientError(Exception): pass
class PermanentError(Exception): pass

def deliver(url, payload):
    try:
        r = httpx.post(url, json=payload, timeout=5.0)
    except (httpx.TimeoutException, httpx.ConnectError) as e:
        raise TransientError(str(e)) from e

    if r.status_code in (429,) or 500 <= r.status_code < 600:
        raise TransientError(f"HTTP {r.status_code}")
    if 400 <= r.status_code < 500:
        raise PermanentError(f"HTTP {r.status_code}: {r.text[:200]}")
    return r

def deliver_with_retry(url, payload, max_attempts=8):
    for attempt in range(max_attempts):
        try:
            return deliver(url, payload)
        except PermanentError as e:
            dead_letter(url, payload, str(e))
            return
        except TransientError as e:
            if attempt == max_attempts - 1:
                dead_letter(url, payload, str(e))
                return
            delay = min(60, 2 ** attempt + random.uniform(0, 1))
            time.sleep(delay)
```

**Trade-offs:** Permanent errors fail fast (no wasted retries). Transient errors get up to 8 attempts with exponential backoff capped at 60s. Dead-letter queue surfaces stuck deliveries to ops. Total worst-case wait is bounded (~2 minutes per webhook). Add idempotency keys so duplicate deliveries on the receiver don't double-process.

## 🔗 Related Topics

- [Logging & Observability](logging-observability.md) — what to log when you catch
- [Resilience & Fault Tolerance](../14-resilience-fault-tolerance/index.md) — circuit breakers, bulkheads
- [Testing](testing-frameworks.md) — testing the failure paths

## 📚 References

- [PEP 3134 — Exception chaining](https://peps.python.org/pep-3134/)
- [`contextlib`](https://docs.python.org/3/library/contextlib.html)
- [`tenacity`](https://tenacity.readthedocs.io/) — retry library
- *Release It!* — Michael Nygard (failure modes chapters)
