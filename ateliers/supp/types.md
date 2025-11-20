# Atelier supplémentaire - Typage

Pour tous les codes suivants, typez tout comme vu en classe.

## Numéro 1

```python
import numpy as np

numbers = np.array([1, 2, 3, 4, 5])

for n in numbers:
    if n % 2 == 0:
        print("even:", int(n))
```

<details>
<summary>Solution</summary>

```python
import numpy as np
import numpy.typing as npt

numbers: npt.NDArray[np.int_] = np.array([1, 2, 3, 4, 5])
n: int

for n in numbers:
    if n % 2 == 0:
        print("even:", int(n))
```

</details>

## Numéro 2

```python
numbers = [1, 2, 3, 4, 5]
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)
    else:
        print(f"{n} is odd")
for e in evens:
    print("even:", e)
print("done")
```

<details>
<summary>Solution</summary>

```python
numbers: list[int] = [1, 2, 3, 4, 5]
evens: list[int] = []
n: int
e: int

for n in numbers:
    if n % 2 == 0:
        evens.append(n)
    else:
        print(f"{n} is odd")

for e in evens:
    print("even:", e)

print("done")
```

</details>

## Numéro 3

```python
def pgcd(a, b):
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return abs(a)

x = 48
y = 18
result = pgcd(x, y)
print(result)
```

<details>
<summary>Solution</summary>

```python
def pgcd(a: int, b: int) -> int:
    temp: int

    while b != 0:
        temp = a % b
        a = b
        b = temp

    return abs(a)

x: int = 48
y: int = 18
result: int = pgcd(x, y)
print(result)
```

</details>

## Numéro 4

```python
def filter_evens(numbers):
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result

nums = [10, 15, 20, 25]
evens = filter_evens(nums)
print(evens)
```

<details>
<summary>Solution</summary>

```python
def filter_evens(numbers: list[int]) -> list[int]:
    result: list[int] = []
    n: int

    for n in numbers:
        if n % 2 == 0:
            result.append(n)

    return result

nums: list[int] = [10, 15, 20, 25]
evens: list[int] = filter_evens(nums)
print(evens)
```

</details>

## Numéro 5

```python
def word_counts(words):
    counts = {}
    for w in words:
        if w in counts:
            counts[w] += 1
        else:
            counts[w] = 1
    return counts

words = ["pomme", "banane", "pomme", "orange", "banane", "pomme"]
counts = word_counts(words)
print(counts)
```

<details>
<summary>Solution</summary>

```python
def word_counts(words: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    w: str

    for w in words:
        if w in counts:
            counts[w] += 1
        else:
            counts[w] = 1

    return counts

words: list[str] = ["pomme", "banane", "pomme", "orange", "banane", "pomme"]
counts: dict[str, int] = word_counts(words)
print(counts)
```

</details>