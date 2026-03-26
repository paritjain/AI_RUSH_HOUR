import heapq
from collections import deque 

# Shared helper
def _stats(nodes: int, path_len: int) -> dict:
    return {'nodes_explored': nodes, 'solution_length': path_len}

# 1.  BFS  –  Breadth-First Search
def bfs(initial_state):
if initial_state.is_goal():
        return [], _stats(0, 0)
queue   = deque([(initial_state, [])])
visited = {initial_state.encode()}
nodes   = 0
