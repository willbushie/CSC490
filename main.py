# CSC490 - String Searching using Hash Table implementation

"""
Objectives:
X    1. Select a hash function (modulo or multiplication).
X    2. Select a collision function (speration chaining or open addressing).
X    3. Use the provided poem (read it into the program).
    4. Insert the poem into the hash table.
    5. Use the hash table for string searching.
"""

# imports
import random

# modulo for hashing and chaining for collision
class HashTable: 
    M = 31
    def __init__(self) -> None:
        self.array = [[],] * self.M # we have 31 buckets here

    def Hash(self,key):
        return key % self.M

    def insert(self,key,value):
        hashcode = self.Hash(key)
        dictionary = {"key":hashcode,"index":[],"value":value}
        found = len(self.array[hashcode]) > 0
        if found is True:
            for count in range(len(self.array[hashcode])): # looking at each item in the chain
                if self.array[hashcode][count]["key"] == key:
                    self.array[hashcode][count]["index"].append(value)#["index"][0])
                    return hashcode
            # add the new value on to the chain
            self.array[hashcode].append(dictionary)
            return hashcode
        else:
            self.array[hashcode].append(dictionary)
    
    def search(self,key):
        hashcode = self.Hash(key)
        if len(self.array[hashcode]) > 0:
            for count in range(len(self.array[hashcode])):
                if self.array[hashcode][count]["key"] == key:
                    return self.array[hashcode][count]["key"], self.array[hashcode][count]["index"], self.array[hashcode][count]["value"]
            return None
        else:
            return None

# read in a file and return a list
def readFile(filename):
    with open(filename) as file:
        contents = file.readlines()
    for line in range(len(contents)-1):
        contents[line] = contents[line][:-1]
    return contents


# calling each hash methods - testing purposes
def test1():
    testlist = ["yes","no","maybe","so","this","is","a","testtt"]
    table1 = HashTable()
    for index in range(len(testlist)):
        table1.insert(index,testlist[index])
    for count in range(len(testlist)):
        print(table1.search(count))

def test2():
    list = readFile("poem.txt")
    table = HashTable()
    for index in range(len(list)):
        table.insert(random.randint(0,30),list[index])
    print(table.search(5))
    for count in range(len(table.array)):
        print(table.search(count))

test2()