class QueueWithNoLimit:
    def __init__(self):
        self.List = []

    def __str__(self):
        values = [str(x) for x in self.List]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.List == []:
            return True
        return False

    def enqueue(self, value):
        self.List.append(value)
        return "The item is inserted in the queue."

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty.")
        else:
            value = self.List.pop(0)
            return f"The dequeue element: {value}"

    def peek(self):
        if self.isEmpty():
            raise Exception("The queue is empty.")
        else:
            return self.List[0]

    def delete(self):
        self.List = []
        return "The queue is emptied."

# queueWithNoLimit = QueueWithNoLimit()
# print(queueWithNoLimit.isEmpty())
# print(queueWithNoLimit.enqueue(23))
# print(queueWithNoLimit.enqueue(33))
# print(queueWithNoLimit.enqueue(43))
# print(queueWithNoLimit.enqueue(53))
# print(queueWithNoLimit.enqueue(63))
# print(queueWithNoLimit.enqueue(73))
# print(queueWithNoLimit.enqueue(83))
# print(queueWithNoLimit.enqueue(93))
# print(queueWithNoLimit.dequeue())
# print(queueWithNoLimit.peek())
# print(queueWithNoLimit)


class CircularQueueWithLimit:
    def __init__(self,maxSize):
        self.items = [None] * maxSize
        self.maxSize = maxSize
        self.top = -1
        self.start = -1
    
    def __str__(self):
        values = [str(x) for x in self.items]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.start == -1:
            return True
        return False
    
    def isFull(self):
        if self.start == 0 and self.top + 1 == self.maxSize:
            return True
        elif self.top + 1 == self.start:
            return True
        else:
            return False
        
    def enqueue(self, value):
        if self.isFull():
            raise Exception("The queue is full")
        if self.top + 1 == self.maxSize:
            self.top == 0
        else:
            self.top += 1
            if self.start == -1:
                self.start = 0
            self.items[self.top] = value
            return f"The item {value} is queued."
        
    def dequeue(self):
        if self.isEmpty():
            raise Exception("The queue is empty.")
        
        firstElement = self.items[self.start]
        start = self.start
        
        if self.start == self.top:
            self.top = -1
            self.start = -1
        elif self.start + 1 == self.maxSize:
            self.start = 0
        else:
            self.start += 1
        
        self.items[start] = None
        return f"The popped item {firstElement}."
    
    def peek(self):
        if self.isEmpty():
            raise Exception("The queue is empty.")
        else:
            return self.items[self.start]

    def delete(self):
        self.items = [None]*self.maxSize
        self.top = -1
        self.start = -1



# circularQueueWithLimit = CircularQueueWithLimit(5)
# print(circularQueueWithLimit.isEmpty)
# print(circularQueueWithLimit.isFull())
# print(circularQueueWithLimit.enqueue(23))
# print(circularQueueWithLimit.enqueue(44))
# print(circularQueueWithLimit.enqueue(54))
# print(circularQueueWithLimit.enqueue(65))
# print(circularQueueWithLimit.enqueue(87))
# print(circularQueueWithLimit.dequeue())
# print(circularQueueWithLimit.peek())
# print(circularQueueWithLimit)

## using queue module from python library queue.
# import queue as q
# customQueue = q.Queue(maxsize=3)
# print(customQueue.empty())
# customQueue.put(2)
# customQueue.put(3)
# customQueue.put(5)
# print(customQueue.full())
# print(customQueue.get())
# print(customQueue.qsize())

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curr  = self.head
        while curr:
            yield curr
            curr = curr.next

class QueueWithLinkedList:
    def __init__(self):
        self.items = LinkedList()
    
    def __str__(self):
        values = [str(x) for x in self.items]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.items.head == None:
            return True
        return False
    
    def enqueue(self,value):
        currNode = Node(value)
        if self.isEmpty():
            self.items.head = currNode
            self.items.tail = currNode
        else:
            self.items.tail.next = currNode
            self.items.tail = currNode

    def dequeue(self):
        if self.isEmpty():
            raise Exception("The queue is empty.")
        
        popped_node = self.items.head
        if self.items.head == self.items.tail:
            self.items.head = None
            self.items.tail = None
        else:
            self.items.head = self.items.head.next
        popped_node.next = None 
        return popped_node

    def peek(self):
        if self.isEmpty():
            raise Exception("The queue is empty.")
        else:
            return self.items.head

    def delete(self):
        self.items.head = None
        self.items.tail = None

queueWithLinkedList = QueueWithLinkedList()
queueWithLinkedList.enqueue(20)
queueWithLinkedList.enqueue(30)
queueWithLinkedList.enqueue(40)
queueWithLinkedList.enqueue(50)
print(queueWithLinkedList)
print(queueWithLinkedList.dequeue)
print(queueWithLinkedList.peek)
print(queueWithLinkedList.delete())


