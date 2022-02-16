# CSC490 - Time and Space Complexity

import random
import timeit
from memory_profiler import profile

"""
objectives:
X    1. Create a function that can generate a random unrepeated integer array. 
        Requirements on supports parameters list:
            Lower Bound
            Upper Bound
            Size
    2. Compare bechmark results of your three sequential sorting implementations
    (selection sort, insertion sort, bubble sort).
        Use testing array generated by your function from the first seciton with sizes:
            10
            1,000
            100,000
"""

# generate algorithm, list of no repeating integers
def generate(length):
    list = []
    for count in range(length):
            list.append(count)
    random.shuffle(list)
    #print(list)
    return list


# selection sort algorithm - completed
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

# insertion sort algorithm - completed
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



# driver 
def driver():
    #selectionSort(generate(10))
    #insertionSort(generate(10))
    #bubbleSort(generate(10))
    return 0

# benchmarking functions for easy and obvious time and memory usage
data1 = generate(10)
def benchmarkSS1():
    selectionSort(data1)
def benchmarkBS1():
    bubbleSort(data1)
def benchmarkIS1():
    insertionSort(data1)

data2 = generate(1000)
def benchmarkSS2():
    selectionSort(data2)
def benchmarkBS2():
    bubbleSort(data2)
def benchmarkIS2():
    insertionSort(data2)

data3 = generate(10000)
def benchmarkSS3():
    selectionSort(data3)
def benchmarkBS3():
    bubbleSort(data3)
def benchmarkIS3():
    insertionSort(data3)

# calling driver
driver()

# calling benchmarks for time and memory usage
print("Selection Sort Results (10): ",timeit.Timer(benchmarkSS1).timeit(number=1))
print("Bubble Sort Results (10): ",timeit.Timer(benchmarkBS1).timeit(number=1))
print("Insertion Sort Results (10): ",timeit.Timer(benchmarkIS1).timeit(number=1))

print("Selection Sort Results (1000): ",timeit.Timer(benchmarkSS2).timeit(number=1))
print("Bubble Sort Results (1000): ",timeit.Timer(benchmarkBS2).timeit(number=1))
print("Insertion Sort Results (1000): ",timeit.Timer(benchmarkIS2).timeit(number=1))

print("Selection Sort Results (1000): ",timeit.Timer(benchmarkSS3).timeit(number=1))
print("Bubble Sort Results (1000): ",timeit.Timer(benchmarkBS3).timeit(number=1))
print("Insertion Sort Results (1000): ",timeit.Timer(benchmarkIS3).timeit(number=1))