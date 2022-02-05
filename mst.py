# CSC490 - Minimum Spanning Trees Algorithm

# import necessary packages
import csv
import timeit
import threading

# THINGS TO ADD
# add a funciton to import a csv
# improve the performance of the code (in some way)
# benchmark the code before and after the performance boost

# graph class
class graph:
    def __init__(self) -> None:
        pass

    # read function graph.read([])
    def read(self,verticies):
        self.data = verticies
        self.size = len(verticies)

    # read a csv file
    def readCSV(self,filename):
        self.data = []
        # read in the file
        with open(filename,mode='r') as graph:
            csvFile = csv.reader(graph)
            for line in csvFile:
                tempList = []
                for element in range(len(line)):
                    item = int(line[element])
                    tempList.append(item)
                self.data.append(tempList)
        self.size = len(self.data)

    # print the data values
    def display(self):
        for line in self.data:
            print(line)

    # find the shortest one - this can be optimized
    def findMin(self,E):
        val = E[0]
        for i in range(len(E)):
            if val[2] > E[i][2]:
                val = E[i]
            elif E[i][2] == 1:
                return val
        return val

    # process the data
    def process(self):
        T = [False] * self.size
        L = []
        E = []
        # do the algorithm
        for i in range(self.size):
            if (i == 0):
                T[i] = True
            else:
                for j in range(self.size):
                    for k in range (j,self.size):
                        if T[j] != T[k]:
                            E.append([j, k, self.data[j][k]])
                targetEdge = self.findMin(E)
                L.append(targetEdge)
                T[targetEdge[0]] = True
                T[targetEdge[1]] = True
                E = []
        # output
        #print(L)
        length = 0
        for ele in L:
            length = length + ele[2]
        print("Minimum Spanning Tree length is:",length)



# main
def benchmark():
    print("MST V2:")
    g = graph()
    g.readCSV('graph.csv')
    g.process()

print(timeit.Timer(benchmark).timeit(number=1))
