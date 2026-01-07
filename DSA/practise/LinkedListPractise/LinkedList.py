# node
# init
# str
# append
# prepend
# insert
# traverse
# search
# search 2
# get
# set_value
# pop_first
# pop
# remove

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '-->'
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
        self.length += 1
    
    def prepend(self,value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            temp.next = self.head
            self.head = temp
        self.length += 1
    
    def insert(self,value, index):
        curr = Node(value)
        if self.head is None:
            self.head = curr
            self.tail = curr
        elif index == 0:
            curr.next = self.head
            self.head = curr
        else:
            temp = self.head
            for _ in range(index-1):
                temp = temp.next
            curr.next = temp.next
            temp.next = curr
        self.length += 1

    def traverse(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def search(self, value):
        temp = self.head
        while temp is not None:
            if temp.value == value:
                return True
            temp = temp.next
        return False
    
    def search2(self, value):
        temp = self.head
        index = 0
        while temp is not None:
            if temp.value == value:
                return index
            temp = temp.next
            index +=1
        return -1

    def get(self, index):
        if index < -1 or index >= self.length:
            return False
        elif index == -1:
            return self.tail
        curr = self.head
        for _ in range(index):
            curr  = curr.next
        return curr
    
    def set_value(self, value, index):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def pop_first(self):
        if self.head is None:
            return None
        
        temp = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            temp.next = None
        self.length -= 1
        return temp
    
    def pop(self):
        popped_node = self.tail
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
            self.length -= 1
            return popped_node
    
    def remove(self,index):
        if index < -1 or index >= self.length:
            return False
        if index == 0:
            return self.pop_first()

        elif index == -1 or index == self.length:
            return self.pop() 

        temp = self.get(index - 1)
        popped_node = temp.next
        temp.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node
        



linkedList = LinkedList()
linkedList.append(30)
linkedList.append(40)
linkedList.prepend(20)
linkedList.insert(100,1)
# linkedList.traverse()
linkedList.get(1)
# print(linkedList.search2(20))
# linkedList.pop_first()
linkedList.remove(2)
#linkedList.pop()
print(linkedList)
# print(linkedList.get(1))

            
            

