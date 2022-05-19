from multiprocessing.dummy import Array


class Graph: 

    def __init__(self, numberOfNodes: int) -> None:
        self.numberOfNodes = numberOfNodes
        self.graph = [0] * self.numberOfNodes * self.numberOfNodes
        self.markItself()
    
    def markItself(self) -> None:
        for i in range(0, self.numberOfNodes):
            self.graph[i * self.numberOfNodes + i] = 1

    def addEdge(self, u: int, v: int) -> None:
        targetIndex = u * self.numberOfNodes + v
        self.graph[targetIndex] = 1

    def addUndirectedEdge(self, u: int, v: int) -> None:
        self.addEdge(u, v)
        self.addEdge(v, u)
    
    def minEdgeBetweenTwoNodes(self, start: int, end: int) -> int:
        visitedNodes = [False] * self.numberOfNodes
        distances = [0] * self.numberOfNodes
        visitedNodes[start] = True
        queue = [start]
        bfsResult = []

        while(len(queue) > 0):
            node = queue.pop(0)
            bfsResult.append(node)
            
            startIndex = node * self.numberOfNodes
            endIndex = startIndex + self.numberOfNodes

            for i in range(startIndex, endIndex):
                realNode = i - node * self.numberOfNodes
                if (self.graph[i] == 1 and realNode != node):
                    nodeToVisit = i - node * self.numberOfNodes
                    if not visitedNodes[nodeToVisit]:
                        queue.append(nodeToVisit)
                        visitedNodes[nodeToVisit] = True
                        distances[nodeToVisit] = distances[node] + 1
        
        return distances[end]



g = Graph(9)
g.addUndirectedEdge(0, 1)
g.addUndirectedEdge(0, 7)
g.addUndirectedEdge(1, 7)
g.addUndirectedEdge(1, 2)
g.addUndirectedEdge(2, 3)
g.addUndirectedEdge(2, 5)
g.addUndirectedEdge(2, 8)
g.addUndirectedEdge(3, 4)
g.addUndirectedEdge(3, 5)
g.addUndirectedEdge(4, 5)
g.addUndirectedEdge(5, 6)
g.addUndirectedEdge(6, 7)
g.addUndirectedEdge(7, 8)

print(g.minEdgeBetweenTwoNodes(1, 5))