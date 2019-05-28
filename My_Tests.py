from My_List import*

s_List = LinkedList()

def test_delete_end():                      #тест удаления из конца списка
    s_List.add_in_tail(Node(100))
    d = Node(103)
    s_List.add_in_tail(Node(101))
    s_List.add_in_tail(Node(102))
    s_List.add_in_tail(d)
    s_List.add_in_tail(Node(104))
    s_List.delete(104, False)
    s_List.print_all_nodes()
    if d == s_List.tail and s_List.size == 4 and d.next == None:
        print("OK delete tail")
    else:
        print("False")

def test_delete_all():                  #тест удаления нескольких элементов в списке (в том числе в начале и в конце)
    s_List.add_in_tail(Node(100))
    d = Node(103)
    s_List.add_in_tail(Node(100))
    s_List.add_in_tail(Node(100))
    s_List.add_in_tail(d)
    s_List.add_in_tail(Node(100))
    s_List.delete(100, True)
    s_List.print_all_nodes()
    if d == s_List.tail and s_List.size == 1 and d.next == None and d == s_List.head:
        print("OK delete all")
    else:
        print("False")

def test_delete_empty():                   #тест удаления в пустом списке
    s = []
    for i in range(4):
        s.append(Node(100 + i))
    s_List.add_in_tail(s[0])
    s_List.add_in_tail(s[1])
    s_List.add_in_tail(s[2])
    s_List.add_in_tail(s[3])
    s_List.print_all_nodes()
    s_List.clean()
    s_List.delete(102, False)
    if s_List.head == None and s_List.tail == None and s_List.size == 0:
        print("Spisok pust")
    else:
        print("Faile")


def test_delete_head():                    #тест удаления с головы списка

    s_List.add_in_tail(Node(100))
    d = Node(101)
    s_List.add_in_tail(d)
    s_List.add_in_tail(Node(102))
    s_List.add_in_tail(Node(103))
    s_List.add_in_tail(Node(104))

    s_List.delete(100, False)
    s_List.print_all_nodes()
    if d == s_List.head and s_List.size == 4:
        print("OK delete head")
    else:
        print("False")

def test_insert_in_head():                  #тест вставки в начало списка и в пустой список
    s = []
    for i in range(4):
        s.append(Node(100 + i))
    s_List.add_in_tail(s[0])
    s_List.add_in_tail(s[1])
    s_List.add_in_tail(s[2])
    s_List.add_in_tail(s[3])

    newNode = Node(1001)
    afterNode = None

    ins = s_List.insert(afterNode, newNode)
    s_List.print_all_nodes()
    if s_List.size == 5 and newNode == s_List.head:
        print("OK insert in head")
    else:
        print("Faile")

    newNode = Node(1001)
    afterNode = None

    s_List.clean()
    ins1 = s_List.insert(afterNode, newNode)
    if s_List.size == 1 and newNode == s_List.head and newNode == s_List.tail:
        print("OK insert in empty")
    else:
        print("Faile")

def test_insert():               #тест вставки в середину и в конец списка

    s = []
    for i in range (4):
        s.append(Node(100 + i))
    s_List.add_in_tail(s[0])
    s_List.add_in_tail(s[1])
    s_List.add_in_tail(s[2])
    s_List.add_in_tail(s[3])

    newNode = Node(1001)
    afterNode = s[3]

    ins = s_List.insert(afterNode, newNode)
    s_List.print_all_nodes()
    if s_List.size == 5 and newNode == s_List.tail:
        print("OK in end")
    else:
        print("Faile")
    newNode = Node(1002)
    afterNode = s[1]
    ins1 = s_List.insert(afterNode, newNode)
    s_List.print_all_nodes()
    if s_List.size == 6:
        print("OK insert")
    else:
        print("Faile")

def test_find_all():                    #тест поиска нескольких элементов по значению

    n1 = Node(100)
    n2 = Node(100)
    n3 = Node(100)
    s_List.add_in_tail(n1)
    s_List.add_in_tail(Node(101))
    s_List.add_in_tail(Node(102))
    s_List.add_in_tail(n2)
    s_List.add_in_tail(n3)
    f = s_List.find_all(100)
    if len(f) == 3 and n1 == f[0] and n2 == f[1] and n3 == f[2]:
        print("OK")
    else:
        print("Faile")
    print("Poisk : ", f)

def test_find_empty():                  #тест поиска по значению в пустом списке
    s_List.add_in_tail(Node(100))
    s_List.add_in_tail(Node(101))
    s_List.add_in_tail(Node(102))
    s_List.add_in_tail(Node(100))
    s_List.add_in_tail(Node(100))
    s_List.print_all_nodes
    s_List.clean()
    f = s_List.find_all(100)
    if f == None:
        print("OK - net takogo elementa - spisok pust")
    else:
        print("Faile")

def test_find_not_item():               #тест поиска по значению, которого нет в списке
    s_List.add_in_tail(Node(100))
    s_List.add_in_tail(Node(101))
    s_List.add_in_tail(Node(102))
    s_List.add_in_tail(Node(100))
    s_List.add_in_tail(Node(100))
    f = s_List.find_all(9999)
    if f == None:
        print("OK - elementa net v spiske")
    else:
        print("Faile")

def test_len():                         #тест вычисления длины списка
    s_List.add_in_tail(Node(100))
    s_List.add_in_tail(Node(101))
    s_List.add_in_tail(Node(102))
    s_List.add_in_tail(Node(100))
    s_List.add_in_tail(Node(103))
    n1 = Node(101)
    s_List.add_in_tail(n1)
    s_List.add_in_tail(Node(105))
    s_List.add_in_tail(Node(100))
    s_List.add_in_tail(Node(108))


    if s_List.size == 9:
        print("OK")
    else:
        print("Faile")
    s_List.delete(100, True)
    if s_List.size == 6:
        print("OK")
    else:
        print("Faile")
    newNode = Node(111111)
    afterNode = n1
    s_List.insert(afterNode, newNode)
    if s_List.size == 7:
        print("OK")
    else:
        print("Faile")
def test_clean():                       #тест очистки списка

    s_List.add_in_tail(Node(101))
    s_List.add_in_tail(Node(102))
    s_List.add_in_tail(Node(100))
    s_List.add_in_tail(Node(103))
    s_List.add_in_tail(Node(105))
    s_List.add_in_tail(Node(100))
    s_List.add_in_tail(Node(108))
    s_List.clean()
    if s_List.head == None and s_List.tail == None and s_List.size == 0:
        print("OK - clean")
    else:
        print("Faile")

#est_find_all()
#test_find_not_item()
#test_find_empty()
#test_delete_head()
#test_delete_end()
#test_delete_all()
#test_delete_empty()
#test_insert()
#test_insert_in_head()
#test_delete_node()
#test_len()
test_clean()

