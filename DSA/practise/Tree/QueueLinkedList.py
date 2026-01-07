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
        self.length = 0

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

class QueueUsingLL:
    def __init__(self):
        self.queue = LinkedList()
    
    def __str__(self):
        values = [str(x.value) for x in self.queue]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.queue.head == None:
            return True
        return False
    
    def enqueue(self,value):
        curr_node = Node(value)
        if self.isEmpty():
            self.queue.head = self.queue.tail = curr_node
        else:
            self.queue.tail.next = curr_node
            self.queue.tail = curr_node
            self.queue.length += 1
        return f"The {value} is inserted." 

    def dequeue(self):
        if self.isEmpty():
            raise Exception("The stack is empty.")
        
        popped_node = self.queue.head
        if self.queue.head == self.queue.tail:
            self.queue.head = self.queue.tail = None
        else:
            self.queue.head = self.queue.head.next
        self.queue.length -= 1
        popped_node.next =  None
        return popped_node
        
    def peek(self):
        if self.isEmpty():
            raise Exception("The stack is empty.")
        return self.queue.head

# queueUsingLL = QueueUsingLL()
# queueUsingLL.enqueue(12)
# queueUsingLL.enqueue(32)
# queueUsingLL.enqueue(42)
# queueUsingLL.enqueue(52)
# print(queueUsingLL)
# print(queueUsingLL.peek())
# print(queueUsingLL.dequeue())