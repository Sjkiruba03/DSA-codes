class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, value):
        if value not in self.adj_list.keys():
            self.adj_list[value] = []
            return True
        return False
    
    def print_graph(self):
        v_list = []
        for vertex in self.adj_list:
            v_list.append(vertex)
        v_list.sort()
        for v in v_list:
            print(v, ':', self.adj_list[v])

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False 

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass    
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for edge in self.adj_list[vertex]:
                self.adj_list[edge].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False




new_graph = Graph()
new_graph.add_vertex(1)
new_graph.add_vertex(2)
new_graph.add_vertex(3)
new_graph.add_vertex(4)

new_graph.add_edge(1, 2)
new_graph.add_edge(1, 3)
new_graph.add_edge(2, 3)
new_graph.add_edge(1, 4)
new_graph.add_edge(2, 4)
new_graph.add_edge(3, 4)

# new_graph.remove_edge(1, 4)

new_graph.remove_vertex(4)
print(new_graph.print_graph())