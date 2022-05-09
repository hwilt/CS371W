class Graph:
    def __init__(self):
        self.edges = dict()     # example: {1: [3], 2: [1], 3: [1], 4: [5], 5: [6], 6: [5], 7: [7]}

    def addEdge(self, x, y):
        self.edges[x] = [y]
        if x != y:
            self.edges[y] = [x]


    def getGraph(self):
        graph = []
        for node in self.edges:
            #print(self.edges[node])
            for neighbors in self.edges[node]:
                graph.append((node, neighbors))
        return graph

    def find_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        paths = []
        for node in self.edges[start]:
            if node not in path:
                newpaths = self.find_path(node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
        return paths




    def clusterRecurse(self, node, clusters, clusterNum):
        if clusters:
            print(clusters, clusterNum)
            if node in clusters[clusterNum]:
                return
        else:
            clusters[clusterNum] = [node]
            self.clusterRecurse(self.edges[node], clusters, clusterNum)


    def findClusters(self):
        ret = 0
        clusters = dict()
        for node in self.edges:
            if node == self.edges[node]:
                clusters[ret] = [node]
                ret += 1
            else:
                self.clusterRecurse(node, clusters, ret)
                ret += 1
        return ret
        


g = Graph()
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(4, 5)
g.addEdge(6, 5)
g.addEdge(7, 7)

print(g.getGraph())
print(g.edges)
print(g.find_path(2, 3))
print(g.findClusters())