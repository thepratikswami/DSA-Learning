# Graphs

## What graphs are all about

Graph problems model relationships between nodes. The main job is choosing the right traversal or graph algorithm.

### When to use graph patterns

- Connected components and islands.
- Shortest path or weighted reachability.
- Cycle detection.
- Course scheduling and prerequisites.
- Union-find connectivity.

## Pattern hacks to identify graph problems

- Keywords: `connected`, `path`, `island`, `course`, `network`, `edge`, `component`.
- Items reference each other through relationships.
- You can model choices as nodes and transitions as edges.

## Common strategies

- Use DFS or BFS for traversal and components.
- Use topological sort for prerequisite ordering.
- Use union-find for undirected connectivity and redundant edges.
- Use Dijkstra for weighted shortest paths with non-negative weights.

## Template

```python
seen = set()

def dfs(node):
    if node in seen:
        return
    seen.add(node)
    for nei in graph[node]:
        dfs(nei)
```

## Notes

Build the graph representation first. A clear adjacency list often makes the rest of the solution straightforward.
