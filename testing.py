# testing
import timeit
from memory_profiler import profile
import random

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
# old stor aglorithm
def STOR1(list):
    hold = [0] * (len(list))
    for index in range(0,len(list)-1):
        #print(f"checking {index}")
        if hold[list[index]] != 0:
            print(list[index],index)
            return
        else:
            hold[list[index]] = 1

@profile
# updated use of python array features
def STOR2(list):
    hold = []
    for index in range(0,len(list)):
        if list[index] in hold:
            print(list[index],index)
            return
        else:
            hold.append(list[index])

@profile
# third attempt at the STOR algo
def STOR3(list):
    root = None
    for index in range(0,len(list)):
        if search(root,list[index]) == True:
            print(list[index],index)
            return
        else:
            root = insert(root,list[index])

src = generate(1000000)

def driver():
    STOR1(src)
    STOR2(src)
    STOR3(src)

def benchmarkSTOR1():
    STOR1(src)
def benchmarkSTOR2():
    STOR2(src)
def benchmarkSTOR3():
    STOR3(src)

# memory profiler
#driver()
# timing them all
print("STOR1 Time: ",timeit.Timer(benchmarkSTOR1).timeit(number=1))
print("STOR2 Time: ",timeit.Timer(benchmarkSTOR2).timeit(number=1))
print("STOR3 Time: ",timeit.Timer(benchmarkSTOR3).timeit(number=1))
