# testing environment

import csv
import timeit

# read a csv file
def readCSV():
    filename = "test.csv"
    data = []
    with open(filename,mode='r') as graph:
        csvFile = csv.reader(graph)
        for line in csvFile:
            tempList = []
            for element in range(len(line)):
                item = int(line[element])
                tempList.append(item)
            data.append(tempList)
    size = len(data)
    # create all the edges
    edges = []
    src = 0
    for line in data: # for each horizontal line
        dest = 0
        for distance in line: # for each index in that line
            if src != dest:
                if distance != 0: # if distance not equal to 0
                    newList = [src,dest,distance]
                    newList2 = [dest,src,distance]
                    if newList in edges or newList2 in edges: # if no repeats
                        pass
                    else:
                        #print(f"creating new node: [{src},{dest},{distance}]")
                        edges.append([src,dest,distance]) # add edge
            dest += 1
        src += 1
    #for edge in edges:
        #print(edge)

# read a csv file
def readCSV2():
    filename = "test.csv"
    #data = []
    edges = []
    with open(filename,mode='r') as graph:
        csvFile = csv.reader(graph)
        src = 0
        for line in csvFile:
            #tempList = []
            index = src + 1
            while index < len(line):
                if int(line[index]) != 0:
                    #print(f"creating new node: [{src},{index},{int(line[index])}]")
                    edges.append([src,index,int(line[index])])
                #item = int(line[element])
                #tempList.append(item)
           # data.append(tempList)
                index += 1
            src += 1
    #for edge in edges:
        #print(edge)

def benchmark():
    #print("original implementation: ",timeit.Timer(readCSV).timeit(number=1000))
    #print("secondary implementation: ",timeit.Timer(readCSV2).timeit(number=1))
    original = timeit.Timer(readCSV).timeit(number=1000)
    secondary = timeit.Timer(readCSV2).timeit(number=1000)
    print(f"times: original: {original} secondary: {secondary} total: {original+secondary}")
    

benchmark()
#print("original version:")
#readCSV()
#print("secondary version:")
#readCSV2()