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


test_delete_node()













