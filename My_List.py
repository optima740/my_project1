import random

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

        if self.head is None: # Если список пуст
            self.head = item  # В поле указателя на голову записываем адрес новой Node - как текущую голову списка
            self.size += 1
            self.head.index = self.size -1



        else:                       # Если список не пуст
            self.tail.next = item # записываем в поле текущей структуры Node - адрес на новый элемент Node
            self.size += 1


        self.tail = item    # В поле указателя на конец записываем адрес новой Node - как текущий конец списка
        self.tail.index = self.size - 1



    def len(self):
        return self.size

    def print_all_nodes(self):
        node = self.head
        while node != None:

            print(node.value, "index ", node.index)
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
        while node is not None:

            if node.value == val:
                print(val)

            node = node.next


        return None



    def delete(self, val, all=False):
        node = self.head

        while node is not None:
            if node.value == val:
                index_i = node.index

                break
            node = node.next
        if (index_i > 0):
            node = self.head
            for i in range (index_i-1):
                node = node.next
            to_del = node.next

            node.next = to_del.next

            del(to_del)
            self.size -=1

        else:
            self.clean_head()
            return






    def clean_head(self):
        temp = self.head
        self.head = self.head.next
        del(temp)
        self.size -= 1

    def clean(self):
        while (self.size):
            self.clean_head()
        print("Gotovo! size = ", self.size)



    def insert(self, afterNode, newNode):
        pass # здесь будет ваш код




s_List = LinkedList()


#listsize = 7
#for i in range (listsize):
    #s_List.add_in_tail(Node(random.randint(0,100)))

s_List.add_in_tail(Node(101))
s_List.add_in_tail(Node(102))
s_List.add_in_tail(Node(103))
s_List.add_in_tail(Node(104))
s_List.add_in_tail(Node(105))

s_List.delete(102)
s_List.print_all_nodes()



#s_List.find_index(0)


#s_List.clean()