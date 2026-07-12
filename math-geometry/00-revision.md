# Math and Geometry Interview Revision

## Core idea

Replace brute-force scanning with a numeric property or an in-place spatial
transformation. The win comes from a formula, a boundary walk, or reusing the
grid itself as scratch space.

## How to recognize it

- The problem manipulates a matrix (rotate, spiral, mark) rather than searching it.
- The answer depends on digits, primes, GCD, or exponents.
- A `O(log n)` or `O(1)`-space solution is hinted by tight constraints.
- Sequences of numbers repeat, suggesting cycle detection.

## Interview thinking steps

1. Write out a tiny example and label every index or digit.
2. Decide whether the trick is arithmetic (formula) or spatial (index mapping).
3. For matrices, ask if you can transform in place instead of allocating a copy.
4. For numbers, look for halving (fast power), cycles (sets), or carries (digits).
5. Confirm the mutation direction so you do not overwrite data you still need.

## Pitfalls

- Rotating a matrix by copying rows in the wrong order.
- Forgetting that in-place methods return `None` and mutate the argument.
- Fast power stack overflow or missing the negative-exponent reciprocal.
- Marking zeroes in the grid before finishing the scan, corrupting later reads.
- Off-by-one on spiral boundaries, revisiting the middle row or column.

## Complexity

Matrix transforms are `O(rows * cols)`. Fast power is `O(log n)`. GCD is
`O(log(min(a, b)))`. Digit math is `O(number of digits)`.

## Worked example

Rotate the matrix `[[1,2,3],[4,5,6],[7,8,9]]` by 90 degrees clockwise, in place.

```
step 1 - transpose (swap m[i][j] with m[j][i] for i < j):

  1 2 3        1 4 7
  4 5 6   ->   2 5 8
  7 8 9        3 6 9

step 2 - reverse each row:

  1 4 7        7 4 1
  2 5 8   ->   8 5 2
  3 6 9        9 6 3
```

Result `[[7,4,1],[8,5,2],[9,6,3]]`. Transpose reflects across the main diagonal,
and reversing each row flips horizontally; together they equal a 90-degree
clockwise rotation using only `O(1)` extra space.
