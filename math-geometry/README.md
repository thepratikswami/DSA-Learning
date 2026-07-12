# Math and Geometry

## What the pattern is all about

Math and geometry problems lean on numeric properties and grid layout instead of
a data structure. The main job is spotting the arithmetic or spatial trick that
collapses a brute-force loop into a formula or an in-place transformation.

### When to use math and geometry patterns

- Rotating, transposing, or spiraling through a matrix.
- Marking state inside a grid without extra memory.
- Number theory: GCD, LCM, primes, factorization.
- Digit manipulation: reversing digits, carry propagation, digit sums.
- Fast power and modular arithmetic on large exponents.

## Pattern hacks to identify math and geometry problems

- Keywords: `rotate`, `spiral`, `in-place`, `digits`, `power`, `prime`, `gcd`.
- The input is a matrix and the ask is to reorder or overwrite cells.
- A naive solution is `O(n)` or `O(exp)` but a formula makes it `O(log n)`.
- The answer depends on properties of numbers rather than their order.

## Common strategies

- Transpose then reverse rows (or columns) to rotate a matrix by 90 degrees.
- Shrink four boundaries inward for spiral traversal.
- Use the first row and column as marker storage for O(1) space grid marking.
- Detect number cycles with a `set` or Floyd fast/slow pointers.
- Halve the exponent every step for fast power, handling negatives via reciprocal.
- Use `math.gcd` and remember `lcm(a, b) = a * b // gcd(a, b)`.

## Template

```python
def fast_pow(base: float, exp: int) -> float:
    if exp < 0:
        base, exp = 1 / base, -exp
    result = 1.0
    while exp:
        if exp & 1:
            result *= base
        base *= base
        exp >>= 1
    return result
```

## Notes

Draw the small case on paper first. Most matrix problems become obvious once you
label indices, and most number problems become obvious once you write out the
first few terms of the sequence.
