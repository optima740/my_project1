class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False

class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for i in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v):
        # ваш код добавления новой вершины
        # с значением value
        # в свободное место массива vertex
        for i in range(len(self.vertex)):
            if self.vertex[i] != None and self.vertex[i].Value == v:
                return
            if self.vertex[i] == None:
                my_vertex = Vertex(v)
                self.vertex[i] = my_vertex
                return

    def AddEdge(self, v1, v2):
        # добавление ребра между вершинами v1 и v2
        index_v1 = v1
        index_v2 = v2
        if index_v1 != None and index_v2 != None:
            self.m_adjacency[index_v1][index_v2] = 1
            self.m_adjacency[index_v2][index_v1] = 1

    def IsEdge(self, v1, v2):
        # True если есть ребро между вершинами v1 и v2
        index_v1 = v1
        index_v2 = v2
        if (index_v1 != None and index_v2 != None) and (self.m_adjacency[index_v1][index_v2] == 1) and (self.m_adjacency[index_v2][index_v1] == 1):
            return True
        else:
            return False

    def RemoveVertex(self, v):
        index_vertext = v
        if index_vertext != None:
            for vert in self.vertex:
                if vert != None and self.IsEdge(index_vertext, self.vertex.index(vert)) == True:
                    self.RemoveEdge(index_vertext, self.vertex.index(vert))
            self.vertex[index_vertext] = None

        # ваш код удаления вершины со всеми её рёбрами
    def RemoveEdge(self, v1, v2):
        # удаление ребра между вершинами v1 и v2
        index_v1 = v1
        index_v2 = v2
        if index_v1 != None and index_v2 != None:
            self.m_adjacency[index_v1][index_v2] = 0
            self.m_adjacency[index_v2][index_v1] = 0

    def PrintAllAdjacency(self):
        print('Vertext:')
        for vert in self.vertex:
            if vert != None:
                print(vert.Value,' ', end ='')
            else:
                print('None ', end='')
        print()
        print('m_adjacency:')
        for i in self.m_adjacency:
            for j in i:
                print ("{:4d}".format(j), end ="")
            print()

    def DepthFirstSearch(self, VFrom, VTo):
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету
        if self.vertex[VFrom] == None or self.vertex[VTo] == None:
            return []
        else:
            vertex_stack = []
            current_vertex = VFrom
            while True:
                self.vertex[current_vertex].Hit = True
                vertex_stack.append(current_vertex)
                for j in range(len(self.m_adjacency)):
                    if self.m_adjacency[current_vertex][j] == 1 and j == VTo:
                        vertex_stack.append(j)
                        return vertex_stack
                for j in range(len(self.m_adjacency)):
                    if self.m_adjacency[current_vertex][j] == 1 and self.vertex[j].Hit == False:
                        current_vertex = j
                        break

"""
my_graph = SimpleGraph(5)
my_graph.AddVertex('A')
my_graph.AddVertex('B')
my_graph.AddVertex('C')
my_graph.AddVertex('D')
my_graph.AddVertex('E')

my_graph.AddEdge(0,1)
my_graph.AddEdge(0,2)
my_graph.AddEdge(0,3)
my_graph.AddEdge(1,0)
my_graph.AddEdge(1,3)
my_graph.AddEdge(1,4)
my_graph.AddEdge(2,0)
my_graph.AddEdge(2,3)
my_graph.AddEdge(3,3)
my_graph.AddEdge(3,0)
my_graph.AddEdge(3,1)
my_graph.AddEdge(3,2)
my_graph.AddEdge(3,4)
my_graph.AddEdge(4,3)
my_graph.AddEdge(4,1)
my_graph.RemoveEdge(0, 3)

my_graph.RemoveEdge(3, 1)

my_graph.PrintAllAdjacency()

path = my_graph.DepthFirstSearch(0, 4)
for item in path:
    print(item, ' ', end='')

"""