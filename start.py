texts = "TWO ROADS DIVERGED IN A YELLOW WOOD"
pat = "ROADS"

file = open("macbeth.txt")
line = file.read()
file.close()
texts = line
pat = "kings"

def BrutalForce(text, pattern):
    m = len(pattern)
    n = len(text)
    if m > n:
        return 0
    for i in range(n - m + 1):
        k = 0
        while k < m:
            if text[i + k] == pattern[k]:
                k += 1
            else:
                break
        if k == m:
            print("Pattern found at index ", i)

def KMP(text, pattern):
    m = len(pattern)
    n = len(text)
    if m > n:
        return 0;
    i = 0
    while i < n - m + 1:
        dict = KMP_sub(text, pattern, i)
        if dict["pass"] is True:
            print("Pattern found at index ", i)
        i += dict["next"]

def KMP_sub(text, pattern, index):  #return a dictionary {"pass": True, "next": 1}
    m = len(pattern)
    n = len(text)
    arr = [True] * m    #arr[i] holds if pattern matches 0 holds all matches, 1 holds text[index + 1:] matches
    for i in range(m):
        for j in range(i + 1):
            if arr[j] is True and (index + i + j >= n or text[index + i + j] != pattern[i]):
                arr[j] = False
    dict = {
        "pass": arr[0],
        "next": m
    }
    for i in range(1, m):
        if arr[i] is True:
            dict["next"] = i
            break
    return dict


class Node:

    def __init__(self, key):
        self.key = key
        self.children = {}
        self.index = []

class Trie:
    root = None

    def __init__(self):
        self.root = Node(None)

    def search(self, pattern):
        if pattern[0] in self.root.children.keys():
            return self.searchNode(self.root.children[pattern[0]], pattern)
        else:
            return None

    def searchNode(self, node, pattern):
        if len(pattern) == 1:
            if node.key == pattern[0]:
                return node
            else:
                return None
        else:
            if node.key == pattern[0] and pattern[1] in node.children.keys():
                newString = pattern[1:]
                return self.searchNode(node.children[pattern[1]], newString)
            else:
                return None

    def insert(self, str, index):
        currNode = self.root
        for i in range(len(str)):
            newStr = str[:i + 1]
            if i == 0:
                found = self.search(newStr)
                if found is None:
                    node = Node(newStr)
                    currNode.children[newStr] = node
                    currNode = node
                else:
                    currNode = found
            else:
                key = str[i]
                if key in currNode.children.keys():
                    currNode = currNode.children[key]
                else:
                    node = Node(key)
                    currNode.children[key] = node
                    currNode = node
        currNode.index.append(index)


    def patchInsert(self, text, windowSize):
        n = len(text)
        for i in range(n - windowSize + 1):
            str = text[i: i + windowSize]
            self.insert(str, i)


BrutalForce(texts, pat)
KMP(texts, pat)


trie1 = Trie()
trie1.patchInsert(texts, len(pat))
n = trie1.search(pat)
if n is None:
    print("not found")
else:
    print("found at ", n.index)