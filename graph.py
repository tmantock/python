import heapq

class Node(object):
    def __init__(self, name = ''):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name = ''):
        self._name = name

    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src = None, dest = None, weight = 0):
        self._source = src
        self._destination = dest
        self._weight = weight

    @property
    def source(self):
        return self._source
    
    @source.setter
    def source(self, value = None):
        self._source = value
    
    @property
    def destination(self):
        return self._destination
    
    @destination.setter
    def destination(self, value = None):
        self._destination = value
    
    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, value = 0):
        self._weight = value
    
    def __lt__(self, other):
        return self._weight < other.weight

    def __str__(self):
        return str(self.source) + '->' + str(self.destination)

class Digraph(object):
    def __init__(self):
        self.nodes = set([])
        self.edges = {}

    def addNode(self, node):
        if node.name in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.source
        dest = edge.destination

        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')

        self.edges[src].append((dest, edge.weight))

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.nodes

    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = res + str(k) + '->' + str(d[0]) + '\n'
        return res[:-1]

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.destination, edge.source, edge.weight)
        Digraph.addEdge(self, rev)
    
    def dijkstras(self, start = None, end = None):
        if start is None or end is None:
            raise ValueError('A start and end node is required')
        if start == end:
            return [str(start)]
        
        total_costs, previous_nodes, min_queue, visited = {}, {}, [(0, start)], set([])

        total_costs[start] = 0
        previous_nodes[start] = start
        heapq.heapify(min_queue)

        for node in self.nodes:
            if node != start:
                total_costs[node] = float('inf')
                previous_nodes[node] = None
        
        while min_queue:
            _, smallest = heapq.heappop(min_queue)
            visited.add(smallest)

            for node, weight in self.childrenOf(smallest):
                if node in visited:
                    continue
                
                alternative = total_costs[smallest] + weight

                if alternative < total_costs[node]:
                    total_costs[node] = alternative
                    previous_nodes[node] = smallest

                    index = -1

                    for i, (n, _) in enumerate(min_queue):
                        if n == node:
                            index = i
                            break
                    
                    if index > -1:
                        del min_queue[index]

                    heapq.heappush(min_queue, (alternative, node))

        for key, value in total_costs.items():
            print(str(key), value)
        for key, value in previous_nodes.items():
            print(str(key), str(value))


def test():
    nodes = []
    for name in range(10):
        nodes.append(Node(str(name)))

    g = Graph()

    for n in nodes:
        g.addNode(n)

    g.addEdge(Edge(nodes[0],nodes[1], 10))
    g.addEdge(Edge(nodes[1],nodes[2], 2))
    g.addEdge(Edge(nodes[2],nodes[3], 3))
    g.addEdge(Edge(nodes[3],nodes[4], 4))
    g.addEdge(Edge(nodes[3],nodes[5], 5))
    g.addEdge(Edge(nodes[0],nodes[2], 6))
    g.addEdge(Edge(nodes[1],nodes[1], 7))
    g.addEdge(Edge(nodes[1],nodes[0], 8))
    g.addEdge(Edge(nodes[4],nodes[0], 9))

    # print('The graph:')
    # print(g)
    g.dijkstras(nodes[0], nodes[5])

test()