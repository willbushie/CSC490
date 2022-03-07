# CSC490 - Merge Sort Benchmarking assignment

"""
Objectives:
X    1. Implement binary search tree in python. Including the functions:
X        a. Insert
X        b. Inorder Traversal
X        c. Search
X    2. Insert a random array from 0 to 10,000 to tree. 
X    3. Benchmark the time of searching a number comparing to searching in a sequential ordered array.
"""

# import modules
import random
import timeit
from memory_profiler import profile

# generate random array of passed size
def generate(size):
    array = []
    for count in range(size):
        array.append(count)
    random.shuffle(array)
    return array

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

def inOrderTraverse(root):
    if root: 
        inOrderTraverse(root.left) 
        print(root.key,end=" ")
        inOrderTraverse(root.right)

def buildTree(list):
    root = None
    for index in range(0,len(list)):
        root = insert(root,list[index])
    return root

def searchList(list,key):
    for index in range(len(list)):
        if list[index] is key:
            return True
    return False

# benchmark funcitons for all of the sorting methods using the same input data
data = generate(100000)
find = random.randint(0,100000-1)
root = buildTree(list(data))

@profile
def benchmarkBST():
    search(root,find)
    #print("BST complete")

@profile
def benchmarkSOA():
    searchList(list(data),find)
    #print("Sequential Sort complete")

# calling benchmarking functions, without benchmarking the algorithms
#benchmarkBST()
#benchmarkSOA()

# calling benchmarks for time and memory usage
print("Binary Search Tree Search (100,000): ",timeit.Timer(benchmarkBST).timeit(number=1))
print("Sequential Searching Search (100,000): ",timeit.Timer(benchmarkSOA).timeit(number=1))
