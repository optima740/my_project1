
class Node:

    def __init__(self, v):
        self.value = v
        self.next = None
        self.index = 0

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_in_tail(self, item):
        if self.head is None:               # Если список пуст
            self.head = item                # В поле указателя на голову записываем адрес новой Node
            self.size += 1
            self.head.index = self.size -1
        else:                               # Если список не пуст
            self.tail.next = item           # записываем в поле текущей структуры Node - адрес на следующий элемент Node
            self.size += 1
        self.tail = item                    # В поле указателя на конец списка записываем адрес новой Node - как текущий конец списка
        self.tail.index = self.size - 1

    def len(self):
        return self.size

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_index(self, i):
        node = self.head
        while node is not None:
            if node.index == i:
                return node
            node = node.next

    def find_all(self, val):
        node = self.head
        self.s = []
        while node is not None:
            if node.value == val:
                self.s.append(node.value)
            node = node.next
        return self.s

    def delete_for_index(self, index_i):
        node = self.head
        if (index_i > 0):
            for i in range (index_i-1):
                node = node.next
            to_del = node.next
            node.next = to_del.next
            del(to_del)
            self.size -=1
        else:
            self.clean_head()
        node = self.head
        node.index=0
        for i in range (self.size):
            node.index = i
            node = node.next

    def delete(self, val, all=False):
        node = self.head
        while node is not None:
            if node.value == val:
                index_i = node.index
                if all == False:
                    self.delete_for_index(index_i)
                    break
                else:
                    self.delete_for_index(index_i)
            node = node.next

    def clean_head(self):
        temp = self.head
        self.head = self.head.next
        del(temp)
        self.size -= 1

        if self.size > 0:
            node = self.head
            node.index = 0
            for i in range(self.size):
                node.index = i
                node = node.next
        else: return

    def clean(self):
        while (self.size):
            self.clean_head()
        return self.size

    def insert(self, afterNode, newNode):
        newNode = Node(newNode)
        node = self.head
        if node == None or afterNode == None:
            self.head = newNode
            self.size += 1
        while node != None:
            if node.value == afterNode:
                temp = node.next
                node.next = newNode
                self.size += 1
                node = node.next
                node.next = temp
            node = node.next
        node = self.head
        node.index = 0
        for i in range(self.size):
            node.index = i
            node = node.next



