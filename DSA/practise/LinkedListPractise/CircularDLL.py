class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class CircularDLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp = self.head
        result = ''
        while temp is not None:
            result += str(temp.value)
            temp = temp.next
            if temp == self.head: break
            else: result += '<-->'
        return result
    
    # append
    def append(self,value):
        curr_node = Node(value)
        if self.length == 0:
            self.head = self.tail = curr_node
            curr_node.next = curr_node
            curr_node.prev = curr_node
        else:
            self.tail.next = curr_node
            self.head.prev = curr_node
            curr_node.prev = self.tail
            curr_node.next = self.head
            self.tail = curr_node
        self.length += 1

    # prepend
    def prepend(self, value):
        curr_node = Node(value)
        if self.length == 0:
            self.head = self.tail = curr_node
            curr_node.next = curr_node
            curr_node.prev = curr_node
        else:
            self.head.prev = curr_node
            self.tail.next = curr_node
            curr_node.next = self.head
            curr_node.prev = self.tail
            self.head = curr_node
        self.length += 1

    # traverse
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
            if temp == self.head:
                break

    # reverse traverse
    def reverseTraverse(self):
        temp = self.tail
        while temp:
            print(temp.value)
            temp = temp.prev
            if temp == self.tail:
                break
    # search
    def search(self, target):
        temp = self.head
        index = 0
        while temp:
            if temp.value == target:
                return index
            temp = temp.next
            index += 1
            if temp == self.head:
                break
    # get
    def get(self, index):
        if index < -1 or index > self.length:
            raise Exception("Index out of range")
        
        if index < self.length // 2:
            curr_node = self.head
            for i in range(index):
                curr_node = curr_node.next
        else:
            curr_node = self.tail
            for i in range(self.length -1, index, -1):
                curr_node = curr_node.prev
        return curr_node

    # set_value
    def set_value(self, index, value):
        curr_node = self.get(index)
        if curr_node:
            curr_node.value = value
            return True
        return False
    
    # insert
    def insert(self, index, value):
        if index < -1 or index > self.length:
            raise Exception("Index is out of range")
        
        if self.length == 0:
            self.prepend()
            return
        
        if index == -1 or index == self.length:
            self.append()
            return
        
        curr_node = self.get(index - 1)
        vlu_node = Node(value)

        vlu_node.next = curr_node.next
        curr_node.next.prev = vlu_node
        curr_node.next = vlu_node
        vlu_node.prev = curr_node

        self.length += 1

    # pop_first
    def pop_first(self):
        popped_node = self.head
        if self.length == 0 :
            return False
        
        if self.length == 1:
            self.head = self.tail = None

        else:
            self.head = self.head.next
            popped_node.next = popped_node.prev = None
            self.head.prev = self.tail
            self.tail.next = self.head

        self.length -= 1
        return popped_node
    
    # pop
    def pop(self):
        if self.length == 0:
            return False
        
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            popped_node.next = popped_node.tail = None
            self.tail.next = self.head
            self.head.prev = self.tail
        self.length -= 1
        return popped_node

    # remove 
    def remove(self, index):
        if self.length == 0:
            return False
        
        if index == 0:
            return self.pop_first()

        elif index == -1 or index == self.length:
            return self.pop()
        
        popped_node = self.get(index)
        popped_node.prev.next = popped_node.next
        popped_node.next.prev = popped_node.prev
        self.length -= 1
        return popped_node

        
    # delete_all
    def delete_all(self):
        self.head = self.tail = None
        self.length = 0 


circularDLL = CircularDLL()
circularDLL.append(30)
circularDLL.append(40)
circularDLL.append(50)
circularDLL.append(60)
circularDLL.prepend(80)
# print(circularDLL.traverse())
# print(circularDLL.reverseTraverse())
# print(circularDLL.search(50))
# print(circularDLL.get(2).value)
# print(circularDLL.set_value(2,999))
# print(circularDLL.insert(2,44))
# print(circularDLL.pop_first().value)
# print(circularDLL.pop().value)
# print(circularDLL.remove(4).value)
# print(circularDLL.delete_all())
print(circularDLL)


