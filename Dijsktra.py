#Min_Heap
class Heap:
    
    def __init__(self):
        self.heap = []
        self.size = 0
    

    def enqueue(self,item):
        self.heap.append(item)
        self.size+=1
        idx = len(self.heap) - 1
        parent = int((idx-1) / 2)
        while True:
            if self.heap[parent] <= self.heap[idx]:
                break
            else:
                self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
                idx = parent
                parent = int((idx-1) / 2)
        return
    
    def dequeue(self):
        if len(self.heap) == 1:
            
            return self.heap.pop()
        if len(self.heap) == 0:
            print("empty_queue")
            return
        #노드위치변경
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        #삭제연산해줌
        results = self.heap.pop()
        self.size-=1
        idx = 0
        left_child = int(2*idx + 1)
        right_child = int (2*idx +2)
        #자식 두개 남았을 경우
        if len(self.heap) == 2:
            if self.heap[idx] < self.heap[left_child]:
                return results
            else:
                self.heap[idx], self.heap[left_child] = self.heap[left_child], self.heap[idx]
                return results
        # 두개 이상일 경우
        while True:
            #exit conditionm
            #자식노드가 없을경우
            if left_child >= len(self.heap)-1 : #or right_child >= len(self.heap):
                break
            #찾은경우
            if self.heap[idx] <= self.heap[left_child] and self.heap[idx] <= self.heap[right_child]:
                break
            
            if self.heap[left_child] < self.heap[right_child]:
                self.heap[idx], self.heap[left_child] = self.heap[left_child], self.heap[idx]
                idx = left_child
                left_child = int(2*idx + 1)
                right_child = int (2*idx +2)
            else:
                self.heap[idx], self.heap[right_child] = self.heap[right_child], self.heap[idx]
                idx = right_child
                left_child = int(2*idx + 1)
                right_child = int (2*idx +2)
        return results

    def __str__(self):
        tmp = [str(x) for x in self.heap]
        return ",".join(tmp)
    
class Vertex:
    def __init__(self, ID=0, data=None):
        self.id = ID
        self.data = data
        
class Graph:
    def __init__(self):
        self.V = {}
        self.E = {}
        self.bfs = []
        
    def addVertex(self, vertex=None):
        if(vertex == None): return
        
        self.V[vertex.id] = vertex
        self.E[vertex.id] = []
        
        
    def addEdge(self, start_id =None, end_id=None, cost = None):
        if(start_id == None or end_id == None): return
        
        self.E[start_id].append((end_id, cost))
        
def dijstra(g,start):
    
    d = [128000 for _ in range(len(g.V)+1)]
    prev = [start for _ in range(len(g.V)+1)]
    short_path = {start}
    all_vertex = set(g.V.keys())
    
    d[start] = 0
    heap = Heap()
    for (connected, cost) in g.E[start]:
        d[connected] = cost
        heap.enqueue((d[connected],connected))
    print(heap)
    while short_path != all_vertex:
        while True:
            cost, con = heap.dequeue()
            if con in all_vertex - short_path : break
        short_path = short_path|{con}
        for v,c in g.E[con]:
            if v in all_vertex-short_path and d[con]+c<d[v]:
                d[v] = d[con] + c
                prev[v] = con
                heap.enqueue((d[v],v))
    
    for i in range(1, len(all_vertex)+1):
        p = i
        prev_list = []
        while(p != start):
            prev_list.append(chr(ord('A')+ p -1))
            p=prev[p]
        prev_list.reverse()
        print(d[i], "->".join([g.V[start].data]+prev_list))
    
    
if __name__ == '__main__':
    
    vertices = [ (1,"A"), (2,"B"), (3,"C"), (4,"D"), (5,"E"), (6,"F"), (7,"G"), (8,"H"), (9,"I"),
(10,"J") ]
    edges = [(1, 2, 10), (1, 3, 17), (1, 4, 25), (1, 5, 30), (1, 6, 23),
(2, 3, 20), (4, 3,17), (5, 2, 19), (5, 8, 24), (6, 4, 28), (6, 5, 16), (6, 8, 18), (6, 7, 39), (6, 9, 20), (7, 4, 25), (7, 9, 29), (7, 10, 40), (8, 10, 20),  (9, 10, 28) ]


            
    """mh = Heap()
    # heap test code..
    #xList = [10, 3, 4, 6, 300, 5, 1, 7, 2, 12, 66]
    xList = [(10,'a'),(12,'b'),(4,'c'),(1,'d')]
    print(sorted(xList))
    for x in xList:
        mh.enqueue(x)
    
    print(mh)
    for x in range(0,len(xList)):
        print(mh.dequeue())"""
    
    g = Graph()
    for(idx, data) in vertices:
        v = Vertex(idx, data)
        g.addVertex(v)
        
    for (s,e,c) in edges:
        g.addEdge(s,e,c)
    
    print("start : A")
    dijstra(g,1)