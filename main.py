# CSC490 - Merge Sort Benchmarking assignment

"""
Objectives:
X    1. Implement Merge Sort algorithm.
X    2. Compare performance between Merge, Selection, Bubble, Insertion, Heap using 1000 elements.
X    3. Explain which algorithm I prefer and why. 
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

# minimum heap tree class
class MinHeap:
    array = []
    count = 0
    def __init__(self) -> None:
        self.array.append({"value": 0,"index": 0,"connect": 0})

    # add a node to the tree
    def HeapPush(self, value, index, connect):
        self.array.append({"value": value,"index": index,"connect": connect})
        self.count += 1
        self.HeapifyUp(self.Size())

    # remove the root value of the tree and heapify
    def ExtrudeMin(self):
        returnNode = self.GetNode(1)
        lastNode = self.array.pop()
        self.count -= 1
        if self.count > 0:
            self.array[1] = lastNode
        self.HeapifyDown(1)
        return returnNode

    # heapify the tree (bottom to top)
    def HeapifyUp(self, position):
        if position <= 1:
            return
        parentPosition = position // 2
        parentNode = self.GetNode(parentPosition)
        leftPosition = parentPosition * 2
        leftNode = self.GetNode(leftPosition)
        rightPosition = parentPosition * 2 + 1
        rightNode = self.GetNode(rightPosition)
        node = 0
        if leftNode is not None and leftNode["value"] < parentNode["value"]:
            node = 1
        if rightNode is not None and ((node == 1 and rightNode["value"] < leftNode["value"]) or (node == 0 and rightNode["value"] < parentNode["value"])):
            node = 2
        if node == 1:
            self.array[leftPosition], self.array[parentPosition] = self.array[parentPosition], self.array[leftPosition]
        elif node == 2:
            self.array[rightPosition], self.array[parentPosition] = self.array[parentPosition], self.array[rightPosition]
        if node != 0:
            self.HeapifyUp(parentPosition)

    # heapify the tree (top to bottom)
    def HeapifyDown(self, position):
        parentPosition = position
        parentNode = self.GetNode(parentPosition)
        leftPosition = parentPosition * 2
        leftNode = self.GetNode(leftPosition)
        rightPosition = parentPosition * 2 + 1
        rightNode = self.GetNode(rightPosition)
        node = 0
        if leftNode is not None and leftNode["value"] < parentNode["value"]:
            node = 1
        if rightNode is not None and ((node == 1 and rightNode["value"] < leftNode["value"]) or (
                node == 0 and rightNode["value"] < parentNode["value"])):
            node = 2
        if node == 1:
            self.array[leftPosition], self.array[parentPosition] = self.array[parentPosition], self.array[leftPosition]
            self.HeapifyDown(leftPosition)
        elif node == 2:
            self.array[rightPosition], self.array[parentPosition] = self.array[parentPosition], self.array[rightPosition]
            self.HeapifyDown(rightPosition)

    # obtain the size of the heap tree
    def Size(self):
        return self.count

    # get the node at a specified position
    def GetNode(self, position):
        if position > self.count:
            return None 
        else:
            return self.array[position]

# take an array and use heap sort to sort the array values
@profile
def HeapSort(array):
    heap = MinHeap()
    for item in array:
        heap.HeapPush(item, item, item)
    counter = 0
    while heap.Size() > 0:
        array[counter] = heap.ExtrudeMin()["value"]
        counter += 1
    return array

# selection sort algorithm
@profile
def selectionSort(list):
    # print original list
    #print(list)
    # find min value & replace with current index
    for index in range(len(list)):
        minimum = (min(list[index:len(list)]))
        minIndex = list.index(minimum)
        # swap
        currValue = list[index]
        list[index] = list[minIndex]
        list[minIndex] = currValue
    # return sorted list
    #print(list)
    return list

# bubble sort algorithm
@profile
def bubbleSort(list):
    # print the original list
    #print(list)
    while True:
        # begin at the beginning of the list
        changes = 0 
        rightIndex = 1
        right = list[rightIndex]
        left = list[rightIndex-1]
        while rightIndex < len(list)-1:
            # check the two buckets
            if right < left:
                # swap and increment changes
                changes += 1
                list[rightIndex] = left 
                list[rightIndex-1] = right
            # increment right, left, and rightIndex
            rightIndex += 1
            right = list[rightIndex]
            left = list[rightIndex-1]
        if right < left:
            list[rightIndex] = left
            list[rightIndex-1] = right 
            # increment changes
            changes += 1
        if changes == 0:
            break
    # return sorted list
    #print(list)
    #return list

# insertion sort algorithm
@profile
def insertionSort(list):
    # print the original list
    #print(list)
    # begin at the first index
    for index in range(len(list)):
        currIndex = index
        currIndexEval = index - 1 
        while currIndexEval >= 0 and list[currIndex] < list[currIndexEval]:
            # swap
            currValue = list[currIndexEval] 
            list[currIndexEval] = list[currIndex] 
            list[currIndex] = currValue 
            # decrement values
            currIndexEval -= 1
            currIndex -= 1
    # return sorted list
    #print(list)
    return list

# merge sort algorithm
@profile
def mergeSort(list):
    if len(list) > 1:
        middle = len(list) // 2
        left = list[:middle]
        right = list[middle:]
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1


# benchmark funcitons for all of the sorting methods using the same input data
data = generate(10000)
def benchmarkSS():
    #print("selection sort")
    #print("data before: ", data)
    selectionSort(list(data))
    #print("data after: ", data)
def benchmarkBS():
    #print("bubble sort")
    #print("data before: ", data)
    bubbleSort(list(data))
    #print("data after: ", data)
def benchmarkIS():
    #print("insertion sort")
    #print("data before: ", data)
    insertionSort(list(data))
    #print("data after: ", data)
def benchmarkHS():
    #print("heap sort")
    #print("data before: ", data)
    array = HeapSort(list(data))
    #print("data after: ", data)
def benchmarkMS():
    #print("merge sort")
    #print("data before: ", data)
    mergeSort(list(data))
    #print("data after: ", data)

# calling benchmarking functions, without benchmarking the algorithms
#benchmarkSS()
#benchmarkBS()
#benchmarkIS()
#benchmarkHS()
#benchmarkMS()

# calling benchmarks for time and memory usage
print("Selection Sort Results (1,000): ",timeit.Timer(benchmarkSS).timeit(number=1))
print("Bubble Sort Results (1,000): ",timeit.Timer(benchmarkBS).timeit(number=1))
print("Insertion Sort Results (1,000): ",timeit.Timer(benchmarkIS).timeit(number=1))
print("Heap Sort Results (1,000): ",timeit.Timer(benchmarkHS).timeit(number=1))
print("Merge Sort Results (1,000): ",timeit.Timer(benchmarkMS).timeit(number=1))