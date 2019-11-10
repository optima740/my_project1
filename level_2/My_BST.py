class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок


class BSTFind:  # промежуточный результат поиска

    def __init__(self):
        self.Node = None  # None если
        # в дереве вообще нету узлов

        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


class BST:

    def __init__(self, node=None):
        self.Root = node  # корень дерева, или None
        self.count_leaf = 0
        self.levels = 0

    def FindNodeByKey(self, key):
        itemFind = BSTFind()
        if self.Root == None:
            itemFind.Node = None
            return itemFind
        else:
            def find(node, key):
                if node.NodeKey < key and node.RightChild != None:
                    find(node.RightChild, key)
                elif node.NodeKey < key and node.RightChild == None:
                    itemFind.NodeHasKey = False
                    return itemFind
                elif node.NodeKey > key and node.LeftChild != None:
                    find(node.LeftChild, key)
                elif node.NodeKey > key and node.LeftChild == None:
                    itemFind.NodeHasKey = False
                    return itemFind
                else:
                    itemFind.NodeHasKey = True
                    itemFind.Node = node
                    return itemFind
                return itemFind
            return find(self.Root, key)
        # ищем в дереве узел и сопутствующую информацию по ключу
        # возвращает BSTFind

    def AddKeyValue(self, key, val):
        if self.Root == None:
            newNode = BSTNode(key, val, None)
            self.Root = newNode
        else:
            def add(node, key):
                if node.NodeKey < key and node.RightChild != None:
                    node = node.RightChild
                    add(node, key)
                elif node.NodeKey < key and node.RightChild == None:
                    newNode = BSTNode(key, val, node)
                    node.RightChild = newNode
                    newNode.Parent = node
                    return
                elif node.NodeKey > key and node.LeftChild != None:
                    node = node.LeftChild
                    add(node, key)
                elif node.NodeKey > key and node.LeftChild == None:
                    newNode = BSTNode(key, val, node)
                    node.LeftChild = newNode
                    newNode.Parent = node
                    return
                else:
                    return False
            return add(self.Root, key)
        # добавляем ключ-значение в дерево
        return False  # если ключ уже есть

    def FinMinMax(self, FromNode, FindMax):

        # ищем максимальное/минимальное (узел) в поддереве
        return None

    def DeleteNodeByKey(self, key):
        if self.Root == None:
            return False
        else:
            del_node = self.FindNodeByKey(key)
            if del_node == False:
                return False
            elif del_node.Node.RightChild == None and del_node.Node.LeftChild == None: # если в удаляемом узле нет потомков
                if del_node.Node.Parent.LeftChild == del_node.Node:
                    del_node.Node.Parent.LeftChild = None
                    del_node.Node.Parent = None

                else:
                    del_node.Node.Parent.RightChild = None
                    del_node.Node.Parent = None

            elif del_node.Node.RightChild != None or del_node.Node.LeftChild != None: # если в удаляемом узле есть один потомок
                if del_node.Node.Parent.LeftChild == del_node.Node:
                    pass


        # удаляем узел по ключу
        return False  # если узел не найден

    def Count(self):
        if self.Root == None:
            return 0
        else:
            list_count = []
            def find(count, node):
                count.append(1)
                if node.RightChild != None and node.LeftChild != None:
                    child = []
                    child.append(node.LeftChild)
                    child.append(node.RightChild)
                    for i in child:
                        find(count, i)
                elif node.RightChild != None and node.LeftChild == None:
                    find(count, node.RightChild)
                elif node.RightChild == None and node.LeftChild != None:
                    find(count, node.LeftChild)
                elif node.RightChild == None and node.LeftChild == None:
                    return count
                return count
            return len(find(list_count, self.Root))

          # количество узлов в дереве

My_BTS = BST()
My_BTS.AddKeyValue(70, 700)
My_BTS.AddKeyValue(93, 930)
My_BTS.AddKeyValue(31, 310)
My_BTS.AddKeyValue(94, 940)
My_BTS.AddKeyValue(73, 730)
My_BTS.AddKeyValue(14, 140)
My_BTS.AddKeyValue(23, 230)
print(My_BTS.Count())
findNode = My_BTS.FindNodeByKey(70)
print(findNode.NodeHasKey)
print('ok')
"""
My_BTS.AddKeyValue(93, 930)
My_BTS.AddKeyValue(31, 310)
My_BTS.AddKeyValue(94, 940)
My_BTS.AddKeyValue(73, 730)
My_BTS.AddKeyValue(14, 140)
My_BTS.AddKeyValue(23, 230)
"""