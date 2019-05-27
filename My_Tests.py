from My_List import*



s_List = LinkedList()

'''s_List.add_in_tail(Node(101))
s_List.add_in_tail(Node(102))
s_List.add_in_tail(Node(103))



s_List.print_all_nodes()
print()
#s_List.clean()


#s_List.insert(102, 11177700)
#s_List.find(101)
"""n = s_List.find_all(111777)
if n != None:
    print(n)
else:
    print("Pusto")"""
#s_List.print_all_nodes()
#print("clean")
#s_List.clean()
d = s_List.delete(102, False)
s_List.clean()
s_List.insert(102, 11177700)

s_List.print_all_nodes()

#s_List.clean()'''




def test_delete_node():


    s_List.add_in_tail(Node(101))

    s_List.clean()
    s_List.delete(101, True)
    s_List.print_all_nodes()


#test_delete_node()

def test_insert_node():


    s_List.add_in_tail(Node(100))
    s_List.add_in_tail(Node(101))
    s_List.add_in_tail(Node(102))
    s_List.add_in_tail(Node(103))
    s_List.add_in_tail(Node(104))
    s_List.insert(None, 109999)
    s_List.print_all_nodes()
#test_insert_node()

def test_find_all():
    s_List.add_in_tail(Node(100))
    s_List.add_in_tail(Node(101))
    s_List.add_in_tail(Node(102))
    s_List.add_in_tail(Node(103))
    s_List.add_in_tail(Node(104))
    f = s_List.find_all(1009)
    print("Poisk : ", f)
test_find_all()






"""def insert(self, afterNode, newNode):
    node = self.head
    if node == None or afterNode == None:
        new_Node = Node(newNode)
        self.head = new_Node
        self.size += 1
    while node != None:
        if node.value == afterNode:
            new_Node = Node(newNode)
            temp = node.next
            node.next = new_Node
            self.size += 1
            node = node.next
            node.next = temp
        node = node.next
    self.re_index()"""





