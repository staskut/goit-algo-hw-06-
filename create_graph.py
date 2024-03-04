import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
line1 = [
    ("Перемога", "Олексіївська"),
    ("Олексіївська", "23 серпня"),
    ("23 серпня", "Ботанічний сад"),
    ("Ботанічний сад", "Наукова"),
    ("Наукова", "Держпром"),
    ("Держпром", "Архітектора Бекетова"),
    ("Архітектора Бекетова", "Захисників України"),
    ("Захисників України", "Метробудівників")
]

line2 = [
    ("Холодна гора", "Південний вокзал"),
    ("Південний вокзал", "Центральний ринок"),
    ("Центральний ринок", "Майдан Конституції"),
    ("Майдан Конституції", "Проспект Гагаріна"),
    ("Проспект Гагаріна", "Спортивна"),
    ("Спортивна", "Завод імені Малишева"),
    ("Завод імені Малишева", "Турбоатом"),
    ("Турбоатом", "Палац спорту"),
    ("Палац спорту", "Армійська"),
    ("Армійська", "Імені Масельського"),
    ("Імені Масельського", "Тракторний завод"),
    ("Тракторний завод", "Індустріальна"),
]
line3 = [
    ("Героїв праці", "Студентська"),
    ("Студентська", "Академіка Павлова"),
    ("Академіка Павлова", "Академіка Барабашова"),
    ("Академіка Барабашова", "Київська"),
    ("Київська", "Пушкінська"),
    ("Пушкінська", "Університет"),
    ("Університет", "Історичний музей"),
]
transfers = [
    # пересадки
    ("Історичний музей", "Майдан Конституції"),
    ("Університет", "Держпром"),
    ("Метробудівників", "Спортивна"),
]

G.add_edges_from(line1, color="g", line="Олексіївська лінія", weight=1)
G.add_edges_from(line2, color="r", line="Холодногірсько-Заводська лінія", weight=1)
G.add_edges_from(line3, color="b", line="Салтівська лінія", weight=1)
G.add_edges_from(transfers, color="grey", weight=2)  # для пересадок "відстань" подвійна


def count_lines(neighbours: dict):
    unique_lines = set()
    for k, v in neighbours.items():
        if not "line" in v.keys():
            continue
        unique_lines.add(v["line"])
    return len(unique_lines)


if __name__ == "__main__":
    edges = G.edges()
    colors = [G[u][v]['color'] for u, v in edges]

    # pos = nx.planar_layout(G)

    pos = nx.drawing.nx_pydot.graphviz_layout(G, prog="dot")
    plt.figure(figsize=(20, 10))
    nx.draw(G, pos=pos, edge_color=colors, width=3, with_labels=True)
    plt.savefig("Схема Харківського метрополітену.png")

    print("Схема Харківського метрополітену")
    print("Кількість станцій: ", len(G.nodes))
    print("Пересадкові станції: ", [node for node, degree in G.degree if count_lines(G[node]) > 1])
    print("Кінцеві станції: ", [node for node, degree in G.degree if count_lines(G[node]) == 1])
