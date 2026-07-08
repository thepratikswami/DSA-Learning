# Linked List

## What linked list is all about

Linked-list problems focus on pointer manipulation. The key is changing links without losing access to the remaining nodes.

### When to use linked-list patterns

- Reversing nodes.
- Detecting cycles.
- Removing nodes by position.
- Reordering or merging lists.
- Using fast and slow pointers.

## Pattern hacks to identify linked-list problems

- Keywords: `node`, `next`, `cycle`, `reverse`, `merge`, `nth from end`.
- You cannot index directly into the structure.
- The problem asks for in-place changes to node links.

## Common strategies

- Use a dummy node to simplify head changes.
- Use fast and slow pointers for cycles and middle positions.
- Track `prev`, `curr`, and `next_node` during reversal.
- Use a heap when merging many sorted lists.

## Template

```python
prev = None
curr = head

while curr:
    next_node = curr.next
    curr.next = prev
    prev = curr
    curr = next_node

return prev
```

## Notes

Draw the links before coding. Most bugs come from overwriting `next` too early.
