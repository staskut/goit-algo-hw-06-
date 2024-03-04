import pandas as pd

from create_graph import G


def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.nodes.keys())

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, attrs in graph[current_vertex].items():
            distance = distances[current_vertex] + attrs["weight"]

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances


dist_df = pd.DataFrame(index=G.nodes.keys(), columns=G.nodes.keys())
for station in dist_df.index:
    dist_dict = dijkstra(G, station)
    for k, v in dist_dict.items():
        dist_df.loc[station, k] = v

print((dist_df))
dist_df.to_csv("Умовна відстань між станціями.csv")
