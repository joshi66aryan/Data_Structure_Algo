class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
    
    def __str__(self):
        string = +str(self.value)
        if self.next:
            string += ',' + str(self.next)
        return string
    
# has min function that gives the minimum from the stack, minNode keeps track of minimum value of the stack
class StackMin:
    def __init__(self):
        self.top = None
        self.minNode = None
    
    def min(self):
        if not self.minNode:
            return None
        return self.minNode.value
    
    def push(self, item):
        if self.minNode and (self.minNode.value < item):
            self.minNode = Node(value = self.minNode.value, next =  self.minNode)
        else:
            self.minNode = Node(value = item, next = self.minNode)

    def pop(self):
        if self.top == None:
            return None
        vlu = self.top
        self.top = self.top.next
        self.minNode = self.minNode.next
        return vlu

# stack = StackMin()
# stack.push(23)
# print(stack.min())
# stack.push(43)
# print(stack.min())
# stack.push(53)
# print(stack.min())
# stack.push(63)
# print(stack.min())

## plate of stack
class StackOfStack:
    def __init__(self,capacity):
        self.capacity = capacity
        self.stack = [] # List contain stacks -- list of python list

    def __str__(self):
        return self.stack
    
    def push(self, item):
        if len(self.stack) > 0 and (len(self.stack[-1]) < self.capacity):
            self.stack[-1].append(item)
        else:
            self.stack.append([item])
        return f"The {item} is pushed into the stack."
    
    def pop(self):
        while len(self.stack) and len(self.stack[-1]) == 0:
            self.stack.pop()
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1].pop()
        
    def pop_at(self,index):
        if len(self.stack[index]) > 0:
            return self.stack[index].pop()
        else:
            return None

# stack_of_stack = StackOfStack(3)
# stack_of_stack.push(24)
# stack_of_stack.push(34)
# stack_of_stack.push(44)
# stack_of_stack.push(54)
# print(stack_of_stack.pop_at(0))

class Stack:
    def __init__(self):
        self.List = []
    
    def __len__(self):
        return len(self.List)
    
    def push(self,value):
        self.List.append(value)

    def pop(self):
        if len(self.List) == 0:
            return False
        else: 
           return self.List.pop()
    
    def peek(self):
        if len(self.List) ==0:
            return False
        else:
            return self.List.pop()

class QueueUsingStack:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()

    def enqueue(self,value):
        self.inStack.push(value)
        return "The item is inserted in Queue."

    def dequeue(self):
        while len(self.inStack):
            self.outStack.push(self.inStack.pop())
        result = self.outStack.pop()
        return result

queueUsingStack = QueueUsingStack()
print(queueUsingStack.enqueue(23))
print(queueUsingStack.enqueue(33))
print(queueUsingStack.enqueue(45))
#print(queueUsingStack.dequeue())
print(queueUsingStack.inStack.peek())

    
