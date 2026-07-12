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

## Worked example

Single Number on `[4, 1, 2, 1, 2]` using XOR cancellation
(`x ^ x = 0`, `0 ^ x = x`, order-independent):

1. `ans = 0`.
2. `ans ^= 4` -> `0100` (4).
3. `ans ^= 1` -> `0101` (5).
4. `ans ^= 2` -> `0111` (7).
5. `ans ^= 1` -> `0110` (6)  — the two `1`s have now cancelled.
6. `ans ^= 2` -> `0100` (4)  — the two `2`s have now cancelled.

Answer `4`. Every value that appears twice XORs to `0`, so only the unpaired
number survives — `O(n)` time and `O(1)` space with no hash map.
