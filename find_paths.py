from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

from create_graph import G as metro


def dfs_iterative(graph, start, end):
    graph_map = graph.copy()

    DFS_graph = nx.DiGraph()
    DFS_graph.add_node(start)

    visited = set()
    stack = [start]
    current_node = start
    counter = 1
    while stack:
        previous_node = current_node
        vertex = stack.pop()
        current_node = vertex
        if vertex not in visited:
            DFS_graph.add_edge(previous_node, current_node)
            graph_map.nodes[current_node]["count"] = counter
            counter+=1
            visited.add(vertex)
            stack.extend(graph[vertex])
        if current_node == end:
            break
    return DFS_graph, graph_map


def bfs_iterative(graph, start, end):
    graph_map = graph.copy()

    BFS_graph = nx.DiGraph()
    BFS_graph.add_node(start)

    visited = set()
    queue = deque([start])

    current_node = start
    counter = 1
    while queue:
        previous_node = current_node
        vertex = queue.popleft()
        current_node = vertex
        if vertex not in visited:
            BFS_graph.add_edge(previous_node, current_node)
            graph_map.nodes[current_node]["count"] = counter
            counter += 1
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)
        if current_node == end:
            break
    return BFS_graph, graph_map


bfs_graph, graph_map = bfs_iterative(metro, "Держпром", "Армійська")
pos = nx.drawing.nx_pydot.graphviz_layout(graph_map, prog="dot")
plt.figure(figsize=(20, 10))
labels = nx.get_node_attributes(graph_map, 'count')
nx.draw(graph_map, pos=pos, with_labels=True, labels=labels)
plt.savefig("BFS_order_Армійська.png")
pos = nx.drawing.nx_pydot.graphviz_layout(bfs_graph, prog="dot")
plt.figure(figsize=(20, 10))
nx.draw(bfs_graph, pos=pos, with_labels=True)
plt.savefig("BFS_Армійська.png")

dfs_graph, graph_map = dfs_iterative(metro, "Держпром", "Армійська")
pos = nx.drawing.nx_pydot.graphviz_layout(graph_map, prog="dot")
plt.figure(figsize=(20, 10))
labels = nx.get_node_attributes(graph_map, 'count')
nx.draw(graph_map, pos=pos, with_labels=True, labels=labels)
plt.savefig("DFS_order_Армійська.png")
pos = nx.drawing.nx_pydot.graphviz_layout(dfs_graph, prog="dot")
plt.figure(figsize=(20, 10))
nx.draw(dfs_graph, pos=pos, with_labels=True)
plt.savefig("DFS_tree_Армійська.png")