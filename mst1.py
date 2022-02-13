# Minumum Spanning Tree Algorithm w/ MinHeap Data Structure Implementation

from collections import defaultdict
import csv
import timeit


# Heap data structure class
class Heap():
    # create empty heap tree
    def __init__(self) -> None:
        self.array = [] 
        self.size = 0 
        self.pos = [] 
    
    # create a new node
    def newMinHeapNode(self,vertex,dist):
        minHeapNode = [vertex,dist]
        return minHeapNode
    
    # swap two nodes
    def swapMinHeapNode(self,a,b):
        t = self.array[a] # record the first passed value
        self.array[a] = self.array[b] # set the first passed value to the second passed value
        self.array[b] = t # set the second passed value to the first passed value
    
    # sorts the tree to be correct
    def minHeapify(self,index):
        smallest = index # smallest equal to passed index
        left = 2*index+1 # left is equal to 2 * the index + 1 
        right = 2*index+2 # right is equal to 2 * the index + 2
        if left < self.size and self.array[left][1] < self.array[smallest][1]: # if left is smaller than size and array[left][1] is less than array[smallest][1]
            smallest = left # then smallest is the left value
        if right < self.size and self.array[right][1] < self.array[smallest][1]:# if right less than size and array[right][1] less than array[smallest][1]
            smallest = right # then smallest is the right value
        if smallest != index: # if smallest is not equal to the passed index,
            self.pos[self.array[smallest][0]] = index # set position at [array[smallest][0]] equal to passed index
            self.pos[self.array[index][0]] = smallest # set position at [array[passed index][0]] = smallest
            self.swapMinHeapNode(smallest,index) # swap the two nodes (passed index and smallest)
            self.minHeapify(smallest) # do this until tree is sorted correctly

    # grab the minum value from the tree & resort the tree
    def extractMin(self):
        if self.isEmpty() == True: # if the list is empty
            return # return, and leave the function
        root = self.array[0] # root node is the at the first index
        lastNode = self.array[self.size-1] # last node is at the end of the index
        self.array[0] = lastNode # move the last node to the root
        self.pos[lastNode[0]] = 0 # adjust position to the last node, first position and set to 0
        self.pos[root[0]] = self.size-1 # adjust position to the root, first and set to size-1
        self.size -= 1 # adjust the heap size
        self.minHeapify(0) # reorganize the tree
        return root # return the root (smallest value)

    # is the tree empty?
    def isEmpty(self):
        return True if self.size == 0 else False # if the tree is empty return true, otherwise return false

    # 
    def decreaseKey(self,vertex,dist):
        vertexPos = int(self.pos[vertex]) # set the vertex position equal to position[vertex]
        self.array[vertexPos][1] = dist
        while vertexPos > 0 and self.array[vertexPos][1] < self.array[(vertexPos-1)//2][1]:
            self.pos[self.array[vertexPos][0]] = (vertexPos-1)/2
            self.pos[self.array[(vertexPos-1)//2][0]] = vertexPos
            self.swapMinHeapNode(vertexPos,(vertexPos-1)//2)
            vertexPos = (vertexPos-1)//2

    # ensure the request is within the heap size
    def isInMinHeap(self,vertex):
        if self.pos[vertex] < self.size: # if the passed position[vertex] is less than the size
            return True # return true - inside of tree
        return False # otherwise return false - not inside of tree

# graph class
class Graph():
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    # read a csv file
    def readCSV(self,filename):
        self.filename = filename
        with open(filename,mode='r') as graph:
            csvFile = csv.reader(graph)
            src = 0
            for line in csvFile:
                index = src + 1
                while index < len(line):
                    if int(line[index]) != 0:
                        self.addEdge(src,index,int(line[index]))
                    index += 1
                src += 1
        self.verticies = src

    # add an edge 
    def addEdge(self,src,dest,dist):
        newNode = [dest,dist]
        self.graph[src].insert(0,newNode)
        newNode = [src,dist]
        self.graph[dest].insert(0,newNode)
    
    # proces and find the MST
    def PrimeMST(self):
        #print("MST time")
        count = 0
        key = [] # creates an empty list
        parent = [] # creates an empty list
        minHeap = Heap() # creates an empty heap
        for vertex in range(self.verticies): # for each vertex
            parent.append(-1) # places a -1 at the end of the list
            key.append(1e7) # places a 10,000,000 at the end of the list
            minHeap.array.append(minHeap.newMinHeapNode(vertex,key[vertex])) # append the min heap array with a new node
            minHeap.pos.append(vertex) # append the minheap position with the vertex id
        minHeap.pos[0] = 0 # set the minheap position at index 0 to 0
        key[0] = 0 # set the key value at index 0 to 0
        minHeap.decreaseKey(0,key[0]) # decrease the key value for the root vertex
        minHeap.size = self.verticies # adjust the heap size to equal the total number of verticies
        while minHeap.isEmpty() == False: # while the heap contains nodes, continue
            newHeapNode = minHeap.extractMin() # create a new node 
            extractedVertex = newHeapNode[0] # the extracted vertex is placed at the root node
            for pCrawl in self.graph[extractedVertex]: # for each list in the graph
                vertex = pCrawl[0] # obtain the vertex number
                if minHeap.isInMinHeap(vertex) and pCrawl[1] < key[vertex]: # if vertex is within the heap, and curr vertext distance < key[vertex]
                    key[vertex] = pCrawl[1] # update key at vertex with current list 
                    parent[vertex] = extractedVertex # update the parent value at vertex
                    minHeap.decreaseKey(vertex,key[vertex]) # decreaes the key value
            count += 1 # advance the count for the MST
        print(f"Minimum Spanning Tree length is: {count}") # once done, print the count for the MST
        #display the path taken
        #for count in range(1,self.verticies):
            #print(" % d  - % d" % (parent[count],count))


# test data
def driver():
    graph = Graph()
    #graph.readCSV("test.csv")
    graph.readCSV("graph1.csv")
    print(f"MST2 V1 Results with {graph.filename}:")
    graph.PrimeMST()

print(timeit.Timer(driver).timeit(number=1))
#driver()
