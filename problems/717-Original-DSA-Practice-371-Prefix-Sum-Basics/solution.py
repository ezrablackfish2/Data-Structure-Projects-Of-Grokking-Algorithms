from collections import deque

def solve(graph, start):
    seen = set([start])
    q = deque([start])
    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for nxt in graph.get(node, []):
            if nxt not in seen:
                seen.add(nxt)
                q.append(nxt)
    return order

if __name__ == "__main__":
    g = {"A":["B","C"],"B":["D"],"C":[],"D":[]}
    print(solve(g, "A"))
