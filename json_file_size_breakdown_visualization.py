import json
import os
from sys import getsizeof
import networkx as nx
import matplotlib.pyplot as plt

def analyze_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    graph = nx.DiGraph()

    def analyze(data, path="root"):
        if isinstance(data, dict):
            for key, value in data.items():
                child_path = f"{path}.{key}"
                graph.add_edge(path, child_path, size=getsizeof(value))
                analyze(value, child_path)
        elif isinstance(data, list):
            graph.add_edge(path, f"{path}[list]", size=getsizeof(data))
            for index, item in enumerate(data[:10]):  # Show first 10 items for clarity
                child_path = f"{path}[{index}]"
                graph.add_edge(f"{path}[list]", child_path, size=getsizeof(item))
                analyze(item, child_path)
        else:
            graph.add_edge(path, f"{path}[value]", size=getsizeof(data))

    analyze(data)

    return graph

def save_graph(graph, output_path):
    pos = nx.spring_layout(graph)
    edge_labels = {(u, v): f"{d['size']} B" for u, v, d in graph.edges(data=True)}

    plt.figure(figsize=(12, 8))
    nx.draw(graph, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=8, font_weight='bold')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=6)

    plt.title("JSON Size Breakdown")
    plt.savefig(output_path)
    plt.close()

if __name__ == "__main__":
    file_path = input("Enter JSON file path: ").strip()
    output_path = input("Enter output image path (e.g., output.png): ").strip()

    if os.path.isfile(file_path):
        graph = analyze_json(file_path)
        save_graph(graph, output_path)
        print(f"Graph saved to {output_path}")
    else:
        print("Invalid file path.")
