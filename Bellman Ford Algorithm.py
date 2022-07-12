class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []


    def add_edge(self, t, d, w):
        self.graph.append([t, d, w])


    def print_solution(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    def bellman_ford(self, src):

        dist = [float("Inf")] * self.V

        dist[src] = 0


        for _ in range(self.V - 1):
            for t, d, w in self.graph:
                if dist[t] != float("Inf") and dist[t] + w < dist[d]:
                    dist[d] = dist[t] + w


        for t, d, w in self.graph:
            if dist[t] != float("Inf") and dist[t] + w < dist[d]:
                print("Graph contains negative weight cycle")
                return

        self.print_solution(dist)


g = Graph(5)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 4)
g.add_edge(1, 3, 3)
g.add_edge(2, 1, 6)
g.add_edge(3, 2, 2)

g.bellman_ford(0)













