import folium
import networkx as nx
import matplotlib.pyplot as plt

# ===============================
#   CONSTANTS AND DATA
# ===============================
MAX = 12

cities = [
    "Mumbai", "Delhi", "Bengaluru", "Chennai", "Kolkata", "Hyderabad",
    "Pune", "Ahmedabad", "Jaipur", "Lucknow", "Bhopal", "Chandigarh"
]

coords = [
    (19.0760, 72.8777),   # Mumbai
    (28.6139, 77.2090),   # Delhi
    (12.9716, 77.5946),   # Bengaluru
    (13.0827, 80.2707),   # Chennai
    (22.5726, 88.3639),   # Kolkata
    (17.3850, 78.4867),   # Hyderabad
    (18.5204, 73.8567),   # Pune
    (23.0225, 72.5714),   # Ahmedabad
    (26.9124, 75.7873),   # Jaipur
    (26.8467, 80.9462),   # Lucknow
    (23.2599, 77.4126),   # Bhopal
    (30.7333, 76.7794)    # Chandigarh
]

# ===============================
#   GRAPH (Adjacency Matrix)
# ===============================
graph = [
    [0,1,0,0,0,1,1,1,0,0,1,0],
    [1,0,0,0,1,0,0,0,1,1,0,1],
    [0,0,0,1,0,1,0,0,0,0,1,0],
    [0,0,1,0,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,1,0,0],
    [1,0,1,0,0,0,0,0,0,0,1,0],
    [1,0,0,0,0,0,0,1,0,0,0,0],
    [1,0,0,0,0,0,1,0,1,0,0,0],
    [0,1,0,0,0,0,0,1,0,0,0,0],
    [0,1,0,0,1,0,0,0,0,0,0,0],
    [1,0,1,0,0,1,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0,0,0]
]


# ===============================
#   QUEUE IMPLEMENTATION
# ===============================
class Queue:
    def __init__(self):
        self.array = [0] * MAX
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def enqueue(self, value):
        if self.rear == MAX - 1:
            print("Queue overflow!")
            return
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.array[self.rear] = value

    def dequeue(self):
        if self.is_empty():
            print("Queue underflow!")
            return 
        value = self.array[self.front]
        self.front += 1
        if self.front > self.rear:
            self.front = self.rear = -1
        return value


# ===============================
#   BFS SHORTEST PATH
# ===============================
def bfs_shortest_path(graph, start, end, vertices):
    visited = [0] * MAX
    parent = [-1] * MAX
    q = Queue()

    visited[start] = 1
    q.enqueue(start)

    while not q.is_empty():
        current = q.dequeue()

        if current == end:
            return reconstruct_path(parent, start, end)

        for i in range(vertices):
            if graph[current][i] == 1 and visited[i] == 0:
                visited[i] = 1
                parent[i] = current
                q.enqueue(i)

    return None


def reconstruct_path(parent, start, end):
    path = []
    v = end
    while v != -1:
        path.append(v)
        v = parent[v]
    return path[::-1]


# ===============================
#   NETWORKX GRAPH VISUALIZATION
# ===============================
def visualize_graph(path, start, end):
    G = nx.Graph()

    for i in range(MAX):
        G.add_node(cities[i])

    for i in range(MAX):
        for j in range(MAX):
            if graph[i][j] == 1:
                G.add_edge(cities[i], cities[j])

    pos = nx.spring_layout(G, seed=42)

    node_colors = []
    for i in range(MAX):
        if i == start:
            node_colors.append("limegreen")
        elif i == end:
            node_colors.append("red")
        elif i in path:
            node_colors.append("skyblue")
        else:
            node_colors.append("lightgray")

    nx.draw(G, pos, with_labels=True, node_color=node_colors,
            node_size=1800, font_size=9, font_weight="bold", edge_color="gray")

    route_edges = [(cities[path[i]], cities[path[i+1]]) for i in range(len(path)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=route_edges, edge_color="blue", width=3)

    plt.title("🗺 Shortest Path Between Indian Cities", fontsize=12)
    plt.show()


# ===============================
#   FOLIUM MAP VISUALIZATION
# ===============================
def plot_path_on_map(path, start, end):
    start_lat, start_lon = coords[start]
    m = folium.Map(location=[start_lat, start_lon], zoom_start=5)

    route_coords = []

    for index in path:
        lat, lon = coords[index]
        color = "green" if index == start else "red" if index == end else "blue"
        folium.Marker(
            [lat, lon],
            popup=f"<b>{cities[index]}</b>",
            icon=folium.Icon(color=color)
        ).add_to(m)
        route_coords.append((lat, lon))

    folium.PolyLine(route_coords, color="blue", weight=5, opacity=0.8).add_to(m)
    m.save("india_route.html")
    print("\n🗺 Map saved as 'india_route.html'. Open it in your browser.")


# ===============================
#   MENU INTERFACE
# ===============================
def main():
    while True:
        print("\n🏙  Indian Cities - Shortest Route Finder")
        print("=========================================")
        for i, name in enumerate(cities):
            print(f"{i}: {name}")

        print("\n1️⃣  Find shortest route")
        print("2️⃣  Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "2":
            print("👋 Exiting program. Goodbye!")
            break

        elif choice == "1":
            try:
                start = int(input("\nEnter start city number: "))
                end = int(input("Enter destination city number: "))

                if not (0 <= start < MAX and 0 <= end < MAX):
                    print("⚠ Invalid input. Choose numbers from 0–11.")
                    continue

                print(f"\nFinding shortest route from {cities[start]} to {cities[end]}...\n")
                path = bfs_shortest_path(graph, start, end, MAX)

                if path:
                    print("✅ Shortest Route Found:")
                    print(" → ".join(cities[i] for i in path))
                    visualize_graph(path, start, end)
                    plot_path_on_map(path, start, end)
                else:
                    print("No route found between these cities.")

            except ValueError:
                print("⚠ Please enter valid numeric input.")

        else:
            print("⚠ Invalid choice! Please select 1 or 2.")


if __name__ == "__main__":
    main()
