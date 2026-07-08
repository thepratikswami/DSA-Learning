# Bit Manipulation

## What bit manipulation is all about

Bit manipulation uses binary representation to solve problems with XOR, shifts, and masks.

### When to use bit manipulation

- Finding a unique number among duplicates.
- Counting set bits.
- Checking or building bit masks.
- Problems involving powers of two or binary states.

## Pattern hacks to identify bit-manipulation problems

- Keywords: `bits`, `binary`, `xor`, `single number`, `missing number`, `mask`.
- Values appear in pairs or repeated groups.
- A set of choices can be represented as bits.

## Common strategies

- Use XOR to cancel equal values.
- Use `n & (n - 1)` to remove the lowest set bit.
- Use shifts to inspect individual bits.
- Use DP relation `bits[i] = bits[i >> 1] + (i & 1)`.

## Template

```python
ans = 0
for x in nums:
    ans ^= x
return ans
```

## Notes

XOR is especially useful because `x ^ x == 0` and `x ^ 0 == x`.
