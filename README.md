🏙️ Indian Cities Shortest Path Finder — BFS
A Python-based Shortest Path Finder that uses the Breadth-First Search (BFS) algorithm to find the shortest route between major Indian cities represented as an unweighted graph.
The project also provides graph visualization using NetworkX and Matplotlib and an interactive geographical map using Folium.
📌 Project Overview
This project models a network of 12 Indian cities as an unweighted graph.
Each city represents a vertex, while connections between cities represent edges.
The application uses Breadth-First Search (BFS) to determine the shortest path between a selected starting city and destination city.
Cities Included
- Mumbai
- Delhi
- Bengaluru
- Chennai
- Kolkata
- Hyderabad
- Pune
- Ahmedabad
- Jaipur
- Lucknow
- Bhopal
- Chandigarh
🧠 Algorithm Used
Breadth-First Search (BFS)
BFS is used because the graph is unweighted.
The algorithm:
1. Starts from the selected source city.
2. Marks it as visited.
3. Adds it to a queue.
4. Explores its neighboring cities.
5. Records the parent of every newly visited city.
6. Continues until the destination is reached.
7. Reconstructs the shortest path using the parent array.
Time Complexity
For a graph with V vertices and E edges:
Time Complexity: O(V + E)
Space Complexity: O(V)
🗺️ Visualizations
The application provides two visualizations after finding a route.
1. Network Graph
Uses:
- NetworkX
- Matplotlib
The visualization displays:
- All cities as nodes
- Connections as edges
- Starting city in green
- Destination city in red
- Cities belonging to the shortest route in blue
2. Interactive Map
Uses Folium to create an interactive geographical map.
The selected route is displayed as a blue line connecting the cities.
The generated map is saved as:
india_route.html

Open this file in a web browser to view the route interactively.
⚙️ Technologies Used
- Python 3
- Breadth-First Search (BFS)
- Graphs
- Queue Data Structure
- NetworkX
- Matplotlib
- Folium
📁 Project Structure
Indian-Cities-Shortest-Path-Finder/
│
├── ds.py
├── india_route.html
└── README.md

india_route.html is generated automatically after finding a route.

🚀 Installation
1. Clone the repository
git clone https://github.com/armaan-syed/Indian-Cities-Shortest-Path-Finder-BFS-visualization.git

2. Navigate into the project
cd Indian-Cities-Shortest-Path-Finder-BFS-visualization

3. Install dependencies
pip install folium networkx matplotlib

▶️ Running the Application
Run:
python ds.py

You will see:
🏙 Indian Cities - Shortest Route Finder
=========================================

0: Mumbai
1: Delhi
2: Bengaluru
3: Chennai
4: Kolkata
5: Hyderabad
6: Pune
7: Ahmedabad
8: Jaipur
9: Lucknow
10: Bhopal
11: Chandigarh

1️⃣ Find shortest route
2️⃣ Exit

Select option 1 and enter the source and destination city numbers.
Example
Enter start city number: 0
Enter destination city number: 1

Output:
Finding shortest route from Mumbai to Delhi...

✅ Shortest Route Found:
Mumbai → Delhi

The application will then:
1. Display the shortest path.
2. Open the NetworkX graph visualization.
3. Generate india_route.html.
4. Display the route on an interactive map.
🔍 Example
Input
Start: Mumbai
Destination: Delhi

Output
Shortest Route Found:
Mumbai → Delhi

For another example:
Start: Mumbai
Destination: Jaipur

The BFS algorithm determines the shortest route based on the connections defined in the adjacency matrix.
🧩 Graph Representation
The cities are represented using an adjacency matrix.
Example:
graph = [    [0,1,0,0,0,1,1,1,0,0,1,0],    [1,0,0,0,1,0,0,0,1,1,0,1],    ...]


A value of:
1 → connection exists
0 → no direct connection

📊 Key Features
- ✅ BFS shortest-path algorithm
- ✅ Custom queue implementation
- ✅ Adjacency matrix graph representation
- ✅ 12 Indian cities
- ✅ Shortest route calculation
- ✅ Network graph visualization
- ✅ Interactive geographical map
- ✅ Input validation
- ✅ Handles unreachable destinations
- ✅ Simple menu-driven interface
🎯 Learning Objectives
This project demonstrates practical implementation of:
- Graph data structures
- Breadth-First Search
- Queue implementation
- Adjacency matrices
- Shortest-path algorithms
- Graph visualization
- Geographical data visualization
- Python programming
