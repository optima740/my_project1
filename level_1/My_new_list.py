class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def add_in_head(self, item):
        if self.head is None:
            self.head = item
            self.head.next = None
            self.tail = item
        else:
            tmp = self.head
            self.head = item
            self.head.next = tmp

    def delete(self, val, all=False):

        if self.len() != 0:
            if (all):
                pass
            else:
                node = self.head
                while node != None:

                    if node.value == val:
                        tmp = node.next
                        #del(self.head)
                        node = tmp
                    else:
                        node = node.next
        else:
            return




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

    def find_all(self, val):
        return [] # здесь будет ваш код

    def delete(self, val, all=False):
        pass # здесь будет ваш код

    def clean(self):
        pass # здесь будет ваш код

    def len(self):
        if self.head is None:
            return 0
        else:
            count = 0
            node = self.head
            while node != None:
                count+=1
                node = node.next
            return count

    def insert(self, afterNode, newNode):
        pass # здесь будет ваш код

my_list = LinkedList()


my_list.add_in_head(Node(100))
my_list.add_in_tail(Node(101))
my_list.add_in_tail(Node(102))
my_list.add_in_head(Node(99))
my_list.print_all_nodes()
print(my_list.len())
my_list.delete(101, False)
print(my_list.len())
