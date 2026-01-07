class Stack:
    # __init__
    def __init__(self):
        self.List = []
        self.Length = 0

    # __str__
    def __str__(self):
        values = [str(i) for i in list]
        return '\n'.join(values)

    # isEmpty
    def isEmpty(self):
        if self.List == []:
            return True
        return False
    
    # push
    def push(self,value):
        self.List.append(value)
        self.Length += 1
        return "The item is successfully inserted."

    # pop
    def pop(self):
        if self.List == []:
            return "The stack is empty."
        else:
            self.Length -= 1
            return self.List.pop()
    # peek
    def peek(self):
        if self.List == []:
            return "The stack is empty."
        else:
            return self.List[-1]
        
    # delete
    def remove(self):
        self.List = None

    # length
    def length(self):
        return self.Length

# These are the object of stack.
# stack  = Stack()
# print(stack.push(2))
# print(stack.push(3))
# print(stack.push(4))
# print(stack.push(5))
# print(stack.length())
# print(stack.pop())
# print(stack.peek())
# print(stack.isEmpty())
# print(stack.remove())

class StackListLimited:
    def __init__(self,maxSize):
        self.List = []
        self.maxSize = maxSize

    def __str__(self):
        values = [str(x) for x in self.List]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.List == []:
            return True
        return False
    
    def isFull(self):
        if len(self.List) == self.maxSize:
            return True
        return False
    
    # push
    def push(self,value):
        if self.isFull():
            return "The stack is full."
        else:
            self.List.append(value)
            return "The item is pushed into stack."
        
    # pop
    def pop(self):
        if self.isEmpty():
            return "The stack is empty."
        else:
            return self.List.pop()
        
    # peek
    def peek(self):
        if self.isEmpty():
            return "The stack is empty."
        else:
            return self.List[-1]
        
    # remove
    def remove(self):
        self.List == None
        self.maxSize == 0

# stackListLimited = StackListLimited(6)
# print(stackListLimited.isEmpty())
# print(stackListLimited.isFull())
# print(stackListLimited.push(20))
# print(stackListLimited.push(30))
# print(stackListLimited.push(40))
# print(stackListLimited.push(50))
# print(stackListLimited.isEmpty())
# print(stackListLimited.isFull())
# print(stackListLimited.pop())
# print(stackListLimited.peek())
# print(stackListLimited.remove())

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curr_node = self.head
        while curr_node:
            yield curr_node # pause and return the element.
            curr_node = curr_node.next

class StackLinkedList:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        return False

    def push(self,value):
        curr_vlu = Node(value)
        curr_vlu.next = self.LinkedList.head
        self.LinkedList.head = curr_vlu
        return "The item is pushed into the stack."

    def pop(self):
        if self.isEmpty():
            return "The stack is empty."
        else:
            popped_vlu = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return popped_vlu

    def peek(self):
        if self.isEmpty():
            return "The stack is empty."
        else:
            return self.LinkedList.head.value
            

    def remove(self):
        self.LinkedList.head = None


# stackLinkedList = StackLinkedList()
# print(stackLinkedList.isEmpty())
# print(stackLinkedList.push(20))
# print(stackLinkedList.push(30))
# print(stackLinkedList.push(40))
# print(stackLinkedList.push(50))
# print(stackLinkedList.push(60))
# # print(stackLinkedList.pop())
# # print(stackLinkedList.peek())
# print(stackLinkedList)

class MultiStack:
    def __init__(self, stackSize):
        self.numOfStack = 3
        self.stackSize = stackSize
        self.size = [0]*self.numOfStack
        self.array = [0] * (stackSize * self.numOfStack)
    
    def __str__(self):
        print(self.array)
        print(self.size)
        return ""

    def IndexOffset(self, stackNum):
        offset = stackNum * self.stackSize
        return offset + self.size[stackNum] - 1 
    
    #isFull
    def isFull(self,stackNum):
        if self.size[stackNum] == self.stackSize:
            return True
        return False

    # isEmpty
    def isEmpty(self, stackNum):
        if self.size[stackNum] == 0:
            return True
        return False

    # push
    def push(self, item, stackNum):
        if self.isFull(stackNum):
            raise Exception(f"The stack of number {stackNum} is full.")
        else:
            self.size[stackNum] += 1 
            self.array[self.IndexOffset(stackNum)] = item
            return f"The item {item} is pushed into the stack."

    # pop
    def pop(self, stackNum):
        if self.isEmpty(stackNum):
            raise Exception(f"The stack of number {stackNum} is empty.")
        else:
            popped_vlu = self.array[self.IndexOffset(stackNum)]
            self.array[self.IndexOffset(stackNum)] = 0
            self.size[stackNum] -= 1
            return f"The popped item {popped_vlu}"

    # peek
    def peek(self,stackNum):
        if self.isEmpty(stackNum):
            raise Exception("The stack is empty.")
        else:
            vlu = self.array[self.IndexOffset(stackNum)]
            return vlu


multiStack = MultiStack(3)
print(multiStack.push(20,0))
print(multiStack.push(30,1))
print(multiStack.push(40,2))
print(multiStack.push(50,1))
print(multiStack.push(60,0))
print(multiStack.push(80,2))
print(multiStack.pop(2))
print(multiStack.peek(2))
print(multiStack)






