# append
# prepend
# insert
# traverse
# search
# search2
# get
# set_value
# pop_first
# pop
# remove 
# delete_all

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularSLL:
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
            if temp == self.head:
                break
            result += '-->'
        return result
        
    def append(self, value):
        curr_node = Node(value)
        if self.length == 0:
            self.head = self.tail = curr_node
            curr_node.next = curr_node
        else:
            self.tail.next = curr_node
            curr_node.next = self.head
            self.tail = curr_node
        self.length += 1

    def prepend(self,value):
        curr_node = Node(value)
        if self.length == 0: 
            self.head = self.tail = curr_node
            curr_node.next = curr_node
        else:
            curr_node.next = self.head
            self.tail.next = curr_node
            self.head = curr_node
        self.length += 1

    def insert(self, index, value):
        if index < -1 or index > self.length:
            raise Exception("Index out of range")

        vlu_node = Node(value)

        if index == 0: 
            if self.length == 0:
                self.head = self.tail = vlu_node
                vlu_node.next = vlu_node
            else:
                vlu_node.next = self.head
                self.tail.next = vlu_node
                self.head = vlu_node
        elif index == self.length:
            self.tail.next = vlu_node
            vlu_node.next = self.head
            self.tail = vlu_node
        else:
            temp = self.head
            for _ in range(index-1):
                temp = temp.next
            vlu_node.next = temp.next.next
            temp.next = vlu_node
        self.length += 1

    def traverse(self):
        if not self.head:
            return 
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            if temp == self.head:
                break

    def search(self, value):
        if self.length == 0: 
            return
        temp = self.head
        while temp is not None:
            if temp.value == value:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False
    
    def search2(self,value):
        if self.length == 0:
            return False
        temp = self.head
        index = 0
        while temp is not None:
            if temp.value == value:
                return index
            temp = temp.next
            if temp == self.head:
                break
            index += 1
        return False
    
    def get(self, index):
        if index < -1 or index > self.length:
            return False
        elif index == -1 or index == self.length:
            return self.tail
            
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        curr_vlu = self.get(index)
        if curr_vlu:
            curr_vlu.value = value
            return True
        return False
    
    def pop_first(self):
        if self.length == 0:
            return False
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            self.tail.next = temp.next
            self.head = temp.next
            temp.next = None
        self.length -= 1
        return temp
    
    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            temp.next = self.tail.next
            self.tail = temp
            popped_node.next = None
        self.length -= 1
        return popped_node
            
    def remove(self, index):
        if index < -1 or index > self.length:
            raise Exception("Index out of range")
        if index == 0:
            if self.length == 0:
                return None
            popped_node = self.head
            if self.length == 1:
                self.head = self.tail = None
            else:
                self.tail.next = popped_node.next
                self.head = popped_node.next
                popped_node.next = None
            self.length -= 1
            return popped_node
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            popped_node = temp.next
            temp.next = popped_node.next
            popped_node.next = None
            self.length -= 1
            return popped_node
        
    def delete_all(self):
        if self.length == 0:
            return True
        else:
            self.tail.next = None
            self.head = self.tail = None
            self.length = 0



circularSLL = CircularSLL()
circularSLL.append(40)
circularSLL.append(50)
circularSLL.append(60)
circularSLL.prepend(100)
#circularSLL.insert(1, 555)
# print(circularSLL.search2(60))
# print(circularSLL.get(2))
# print(circularSLL.set_value(2,80))
# print(circularSLL.pop_first())
# print(circularSLL.pop())
# print(circularSLL.remove(-1))
print(circularSLL.delete_all())
print(circularSLL)