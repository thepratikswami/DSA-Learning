# Bit Manipulation Interview Revision

## Core idea

Use binary operations to encode, compare, count, or cancel values efficiently.

## How to recognize it

- The problem mentions bits or binary.
- Values appear exactly twice except one value.
- You need set-bit counts.
- A subset or state can be represented by a mask.

## Interview thinking steps

1. Identify whether XOR, shifting, or masking applies.
2. Use XOR for cancellation problems.
3. Use `n & 1` to inspect the lowest bit.
4. Use `n & (n - 1)` to drop the lowest set bit.
5. Watch language-specific integer behavior.

## Pitfalls

- Confusing XOR with OR.
- Forgetting operator precedence.
- Mishandling negative numbers in languages with fixed-width integers.
- Overusing bits when a clearer hash solution is acceptable.

## Complexity

Most bit solutions are `O(n)` time and `O(1)` space, or `O(number_of_bits)` for a single number.
