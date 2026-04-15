---
tags:
  - phase-1
  - functional-programming
  - fundamentals
difficulty: medium
status: written
---

# Functional Programming

> **TL;DR:** FP treats computation as the evaluation of pure functions over immutable data. Same input → same output, no side effects. In Python, you don't go full FP; you adopt the parts that make code easier to reason about: pure functions, immutability, higher-order functions, and composition.

## 📖 Concept Overview

Functional programming emphasizes **what** to compute, not **how**. Core ideas:

1. **Pure functions** — output depends only on inputs; no side effects.
2. **Immutability** — data isn't modified; new values are derived.
3. **First-class functions** — functions are values, passed and returned like any other.
4. **Composition** — small functions combined into bigger ones.

The payoff: easier to test (no setup), easier to reason about (no hidden state), trivially parallelizable (no shared mutable state). Python is multi-paradigm — you'd never write a whole app in pure FP — but borrowing FP discipline for data transformations makes them dramatically simpler.

## 🔍 Deep Dive

### Pure functions

```python
# ❌ Impure: depends on and mutates external state
counter = 0
def add(x):
    global counter
    counter += 1
    return x + counter

# ✅ Pure: same input always gives same output
def add(x: int, y: int) -> int:
    return x + y
```

Test for purity: can you replace the call with its return value without changing behavior? If yes → pure.

### Immutability

```python
# ❌ Mutating in place
def add_tax(items, rate):
    for item in items:
        item["price"] *= (1 + rate)
    return items

# ✅ Return a new list of new dicts
def add_tax(items, rate):
    return [{**item, "price": item["price"] * (1 + rate)} for item in items]
```

Python helpers: `tuple`, `frozenset`, `dataclass(frozen=True)`, `types.MappingProxyType`.

### Higher-order functions (HOFs)

Functions that take or return other functions.

```python
# map, filter, reduce
from functools import reduce

nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))           # [2,4,6,8,10]
evens   = list(filter(lambda x: x % 2 == 0, nums))   # [2,4]
total   = reduce(lambda acc, x: acc + x, nums, 0)    # 15

# But Pythonic = comprehensions
doubled = [x * 2 for x in nums]
evens   = [x for x in nums if x % 2 == 0]
total   = sum(nums)
```

### functools toolkit

```python
from functools import partial, reduce, lru_cache, cache, wraps

# partial: pre-fill arguments
def power(base, exp): return base ** exp
square = partial(power, exp=2)
square(5)  # 25

# lru_cache / cache: memoization
@cache
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)

# reduce: collapse a sequence
total = reduce(lambda a, b: a + b, [1, 2, 3, 4])
```

### Composition

```python
def compose(*fns):
    def composed(x):
        for fn in reversed(fns):
            x = fn(x)
        return x
    return composed

clean = compose(str.lower, str.strip)
clean("  HELLO  ")  # "hello"
```

### Currying

Transform `f(a, b, c)` into `f(a)(b)(c)`.

```python
def curry(fn):
    def curried(*args, **kwargs):
        if len(args) + len(kwargs) >= fn.__code__.co_argcount:
            return fn(*args, **kwargs)
        return lambda *more_args, **more_kw: curried(*args, *more_args, **kwargs, **more_kw)
    return curried

@curry
def add(a, b, c):
    return a + b + c

add(1)(2)(3)  # 6
add(1, 2)(3)  # 6
```

In practice, `functools.partial` covers 95% of currying use cases in Python.

### Generators & lazy evaluation

```python
def integers():
    n = 1
    while True:
        yield n
        n += 1

from itertools import islice
list(islice((x * x for x in integers()), 5))  # [1,4,9,16,25]
```

Lazy pipelines avoid materializing intermediate lists — essential for streams.

### Side-effect isolation pattern

Push side effects to the edges of your program; keep the core pure.

```mermaid
flowchart LR
    Input[Read input/IO] --> Pure[Pure transformations]
    Pure --> Output[Write output/IO]
    style Pure fill:#90EE90
    style Input fill:#FFB6C1
    style Output fill:#FFB6C1
```

## ⚖️ Trade-offs & Pitfalls

- ✅ **Use FP for:** data transformations, ETL pipelines, business rules with no I/O, anywhere testability matters.
- ❌ **Avoid pure FP for:** stateful entities (a Connection, a Game), heavy I/O orchestration.
- 🐛 **Common mistakes:**
    - "I'm using `map` so it's functional" — purity matters more than syntax.
    - Deep recursion without `sys.setrecursionlimit` awareness (Python lacks TCO).
    - Mutating a "supposedly" immutable list because Python tuples can hold mutable items.
- 💡 **Rules of thumb:**
    - Comprehensions over `map`/`filter` in Python.
    - Use `dataclass(frozen=True)` for record-like data.
    - Push side effects to the boundary; keep the middle pure.

## 🎯 Interview Questions

<details>
<summary><strong>Q1: What's a pure function?</strong></summary>

A function whose output depends only on its inputs and that produces no side effects (no I/O, no mutation of external state, no clock reads, no random calls). Pure functions are referentially transparent — you can replace the call with its return value anywhere without changing program behavior.

</details>
<details>
<summary><strong>Q2: Why is immutability valuable in concurrent code?</strong></summary>

No shared mutable state means no data races. Multiple threads can read the same value without locks. In Python this matters less because of the GIL, but in distributed systems (or any language with real parallelism) immutability eliminates an entire class of bugs.

</details>
<details>
<summary><strong>Q3: Difference between `map`/`filter` and list comprehensions in Python?</strong></summary>

Functionally equivalent for simple cases. Comprehensions are more idiomatic, often clearer, and slightly faster. `map`/`filter` shine when you already have a named function to apply (`map(json.loads, lines)`). Generator expressions (`(x*2 for x in xs)`) are lazy — useful for large or infinite sequences.

</details>
<details>
<summary><strong>Q4: What is `functools.lru_cache` and when would you use it?</strong></summary>

Decorator that memoizes function results based on arguments — cache hits skip the function body. Use for **pure** functions with expensive computation and a bounded input space. Don't use for impure functions (cache won't reflect external changes) or unbounded inputs (memory leak).

</details>
<details>
<summary><strong>Q5: Python doesn't optimize tail calls — why does that matter?</strong></summary>

Recursive solutions in FP languages rely on tail-call optimization to avoid stack overflow. Python doesn't do TCO; deep recursion blows the stack (~1000 frames default). Convert recursion to iteration, or use an explicit stack/queue, when depth might grow.

</details>

## 🏗️ Scenarios

### Scenario: Building a user-event ETL

**Situation:** Read raw user events from S3, normalize timestamps, drop bot traffic, enrich with user metadata, write to BigQuery.

**Constraints:** Idempotent reruns. ~10M events/day. Must be testable without S3.

**Approach:** Express the pipeline as a series of pure transformations. Side effects (reading S3, writing BQ) live only at the edges.

**Solution:**

```python
from dataclasses import dataclass
from datetime import datetime
from typing import Iterable

@dataclass(frozen=True)
class RawEvent:
    user_id: str
    ts: str
    action: str
    user_agent: str

@dataclass(frozen=True)
class CleanEvent:
    user_id: str
    ts: datetime
    action: str
    is_premium: bool

# Pure transformations — trivially testable
def parse_ts(e: RawEvent) -> RawEvent:
    return RawEvent(e.user_id, e.ts, e.action, e.user_agent)

def is_human(e: RawEvent) -> bool:
    return "bot" not in e.user_agent.lower()

def enrich(e: RawEvent, premium_ids: set[str]) -> CleanEvent:
    return CleanEvent(e.user_id, datetime.fromisoformat(e.ts),
                      e.action, e.user_id in premium_ids)

def transform(events: Iterable[RawEvent], premium_ids: set[str]) -> Iterable[CleanEvent]:
    return (enrich(e, premium_ids) for e in events if is_human(e))

# Side effects only here
def run():
    raw = read_from_s3(...)             # impure
    premium = load_premium_ids(...)     # impure
    clean = transform(raw, premium)     # pure
    write_to_bq(clean)                  # impure
```

**Trade-offs:** Tests for `transform` need no mocks — pass in lists, get lists out. The orchestration function (`run`) is the only thing requiring integration tests. Memory stays low because `transform` is a generator.

## 🔗 Related Topics

- [OOP & SOLID](oop-solid.md) — orthogonal paradigm; good code mixes both
- [Async & Concurrency](async-concurrency.md) — immutability simplifies concurrent code
- [Testing Frameworks](testing-frameworks.md) — pure functions are dream tests

## 📚 References

- *Functional Python Programming* — Steven Lott
- [PEP 309 — `functools.partial`](https://peps.python.org/pep-0309/)
- [`functools` docs](https://docs.python.org/3/library/functools.html)
- [`itertools` recipes](https://docs.python.org/3/library/itertools.html)
