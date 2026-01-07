# append
# prepend
# insert
# traverse
# search
# get
# set_value
# pop_first
# pop
# remove 
# delete_all

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
    def __str__(self):
        return str(self.value)

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp = self.head
        result = ''
        while temp is not None: 
            result += str(temp.value)

            if temp.next is not None:
                result += '<-->'
            temp = temp.next
        return result
    
    def append(self, value):      
        curr_node = Node(value)
        if self.length == 0:
            self.head = self.tail = curr_node
        else:
            self.tail.next = curr_node
            curr_node.prev = self.tail
            self.tail = curr_node
        self.length += 1
    
    def prepend(self,value):
        curr_node = Node(value)
        if not self.head:
            self.head = self.tail = curr_node
        else:
            curr_node.next = self.head
            self.head.prev = curr_node
            self.head = curr_node
        self.length += 1

    def insert(self, index, value):
        if index < -1 or index > self.length:
            raise Exception("index out of range")
        
        if index == -1 or index == self.length:
            self.append(value)
        elif index == 0:
            self.prepend(value)
        else:
            curr_node = Node(value)
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            temp.next = curr_node
            curr_node.prev = temp
            curr_node.next = temp.next.next
        self.length += 1

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def reverseTraverse(self):
        temp = self.tail
        while temp:
            print(temp.value)
            temp = temp.prev

    def search(self,value):
        temp = self.head
        index = 0
        while temp:
            if temp.value == value:
                return index
            temp = temp.next
            index += 1
        return -1
    
    def get(self,index):
        if index < -1 or index > self.length:
            raise Exception("Index out of range")
        
        if index < self.length // 2:
            curr = self.head
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.length - 1, index, -1):
                curr = curr.prev
        return curr
    
    def set_value(self, index, value):
        curr_node = self.get(index)
        if curr_node:
            curr_node.value = value
            return True
        return False


    def pop_first(self):
        popped_node = self.head
        if self.length == 0:
            return False
        elif self.length == 1:
            self.head = self.tail = None
        else:
            self.head = popped_node.next
            self.head.prev = None
            popped_node.next = None
        self.length -= 1
        return popped_node


    def pop(self):
        popped_node = self.tail
        if self.length == 0:
            return False
        elif self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = popped_node.prev
            self.tail.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node  

    def remove(self, index):
        if index < -1 or index > self.length:
            raise Exception("Index out of range")

        if index == 0:
            curr = self.pop_first()
        elif index == -1 or index == self.length:
            curr = self.pop()
        else:
            curr = self.get(index)
            curr.next.prev = curr.prev
            curr.prev.next = curr.next
        self.length -=1
        return curr 

    def delete_all(self):
        self.head = self.tail = None
        self.length = 0




            


# get
# set_value
# pop_first
# pop
# remove 
# delete_all
        
        

dll = DLL()
dll.append(30)
dll.append(40)
dll.append(50)
dll.append(60)
dll.append(70)
# dll.insert(3, 100)
# print(dll.traverse())
# print(dll.reverseTraverse())
# print(dll.search(40))
# print(dll.get(1))
# print(dll.set_value(-111,100))
# print(dll.pop_first())
# print(dll.pop())
# print(dll.remove(-1))
print(dll.delete_all())
print(dll)

    



