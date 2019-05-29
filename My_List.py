
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
        if self.head is None:               # Если список пуст.
            self.head = item                # В поле указателя на голову записываем адрес новой Node
            self.size += 1
            self.head.index = self.size -1
        else:                               # Если список не пуст
            self.tail.next = item           # записываем в поле текущей структуры Node - адрес на следующий элемент Node
            self.size += 1
        self.tail = item                    # В поле указателя на конец списка записываем адрес новой Node - как текущий конец списка
        self.tail.index = self.size - 1

    def insert_in_head(self, item):
        temp = self.head.next
        temp_head = self.head
        self.head = item
        self.head.next = temp_head
        self.size += 1
        self.re_index()

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
                self.s.append(node)
            node = node.next
        if (len(self.s)):
            return self.s
        else:
            return self.s

    def clean_tail(self):
        node = self.tail
        node1 = self.head
        temp = node1
        for i in range (node.index - 1):
            node1 = node1.next
            temp = node1
        to_del = node1.next
        temp.next = None
        self.tail = temp
        del(to_del)
        self.size -= 1
        self.re_index()

    def delete_for_index(self, index_i):
        node = self.head
        if (index_i < self.size-1 and index_i > 0):
            for i in range (index_i-1):
                node = node.next
            to_del = node.next
            node.next = to_del.next
            del(to_del)
            self.size -=1
            self.re_index()
        elif index_i == 0:
            self.clean_head()
        elif (index_i == self.size-1):
            self.clean_tail()


    def re_index(self):
        node = self.head
        if node !=None:
            node.index = 0
            for i in range(self.size):
                node.index = i
                node = node.next
        else:
            return

    def delete(self, val, all=False):
        node = self.head
        while node is not None:
            if node.value == val:
                index_i = node.index
                if all == False:
                    self.delete_for_index(index_i)
                    return
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
        else:
            self.tail = None
            return

    def clean(self):
        while (self.size):
            self.clean_head()
        if self.head == None:
            return

    def insert(self, afterNode, newNode):
        node = self.head
        if node == None:
            #new_Node = Node(newNode)
            self.head = newNode
            self.tail = newNode
            self.size += 1
            self.re_index()
            return
        elif afterNode == None:
            self.insert_in_head(newNode)
            return
        while node != None:
            if node.index == afterNode.index:
                #new_Node = Node(newNode)
                temp = node.next
                node.next = newNode
                self.size += 1
                node = node.next
                node.next = temp
                if node.next == None:
                    self.tail = newNode
            node = node.next
        self.re_index()


