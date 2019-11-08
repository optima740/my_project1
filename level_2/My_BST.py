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
            add(self.Root, key)


        # добавляем ключ-значение в дерево
        return False  # если ключ уже есть

    def FinMinMax(self, FromNode, FindMax):
        # ищем максимальное/минимальное (узел) в поддереве
        return None

    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу
        return False  # если узел не найден

    def Count(self):
        return 0  # количество узлов в дереве