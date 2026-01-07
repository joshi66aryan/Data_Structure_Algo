class TrieNode:
    def __init__(self):
        self.children = {} 
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertString(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.endOfString = True
        print("Successfully Inserted.")

    def searchString(self, word):
        current = self.root
        for i in word:
            ch = i 
            node  = current.children.get(ch)
            if node == None:
                return False
            current = node
        
        if current.endOfString == True:
            return True
        else:
            return False
        
def deleteString(root, word, index):
    ch = word[index]
    currentNode = root.children.get(ch)
    canThisNodeBeDeleted = False

    #1: if the current node has more than one child, we cannot delete it because other words depends on it.
    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index+1)
        return False
    
    #2: if we're are at the last character of the word
    if index == len(word) - 1:
        if len(currentNode.children) >= 1:
            currentNode.endOfString = True
            return False
        else:
            root.children.pop(ch)
            return True

    #3: this word is prefix of some other word
    if currentNode.endOfString == True:
        deleteString(currentNode, word, index+1)
        return
    
    #4: recursive delete possible
    canThisNodeBeDeleted = deleteString(currentNode, word, index+1)
    if canThisNodeBeDeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False
    

newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Appl")
print(newTrie.searchString("App"))
deleteString(newTrie.root, "App", 0)

print(newTrie.searchString("App"))


