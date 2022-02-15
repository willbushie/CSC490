# CSC490 - Time and Space Complexity

import random
from time import sleep
import timeit
from memory_profiler import profile
import sys 
sys.setrecursionlimit(1000000)

"""
objectives:
1. 
    X Create a function to generate 1,000,000 element (in a list). 
    X Only two of the values can be repeated and positions are randomly placed each time.
2. 
    X Create own implementation of STOR and SCAN. 
    X Benchmark their performance by measuring execution time. 
    X Source data from objective one.
3. 
    X Create a data structure (dictionary) that uses less memory in constructing array B in STOR.
    X Update STOR and compare the memory usage. 
    Use test data which has max number equal to 2,000,000.
"""

class Node():
    def __init__(self,key):
        self.key = key
        self.right = None
        self.left = None

def insert(node,key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left,key)
    else:
        node.right = insert(node.right,key)
    return node

def search(root,key):
    if root is not None:
        if root.key == key:
            return True
        elif root.key > key:
            return search(root.left,key)
        elif root.key < key: 
            return search(root.right,key)
    else:
        return False

def generate(length):
    while True:
        repeatPos = random.randint(0,length-1)
        repeatInt = random.randint(0,length-1)
        if repeatInt-1 != repeatPos and repeatPos >= 0 and repeatInt >= 1:
            break
    list = []
    for count in range(length):
            list.append(count)
    list[repeatPos] = repeatInt - 1
    print(f"index to be replaced: {repeatPos} Number to repeat: {repeatInt-1}")
    random.shuffle(list)
    return list

@profile
# stor aglorithm
def STOR(list):
    hold = [0] * (len(list))
    for index in range(0,len(list)-1):
        #print(f"checking {index}")
        if hold[list[index]] != 0:
            print(list[index],index)
            return
        else:
            hold[list[index]] = 1

#@profile
# scan algorithm
def SCAN(list):
    for count in range(len(list)):
        print(f"checking {count}")
        for inner in range(count+1,len(list)):
            if list[count] == list[inner]:
                print(count,inner)
                return

def driver():
    data = generate(1000000)
    sleep(5)
    STOR(data)
    #SCAN(data)


#driver()
print("SCOR Results: ",timeit.Timer(driver).timeit(number=1))