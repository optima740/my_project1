class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов

class SimpleTree:

    def __init__(self, root=None):
        self.Root = root  # корень, может быть None
        self.count_leaf = 0
        self.levels = 0

    def AddChild(self, ParentNode, NewChild):
        if ParentNode == None and self.Root == None:
            self.Root = NewChild
            self.Root.Parent = None

        elif ParentNode == None and self.Root != None:
            NewChild.Parent = None
            self.Root.Parent = NewChild
            temp_root = self.Root
            self.Root = NewChild
            self.Root.Children.append(temp_root)
        elif ParentNode != None:
            ParentNode.Children.append(NewChild)
            NewChild.Parent = ParentNode
        # код добавления нового дочернего узла существующему ParentNode

    def DeleteNode(self, NodeToDelete):
        if NodeToDelete == self.Root:
            self.Root = None
        else:
            temp_parent = NodeToDelete.Parent
            for i in temp_parent.Children:
                if i == NodeToDelete:
                    temp_parent.Children.remove(i)
            NodeToDelete.Parent = None
        # код удаления существующего узла NodeToDelete

    def GetAllNodes(self):
        list_all_nodes = []
        if self.Root == None:
            return []
        elif len(self.Root.Children) == 0:
            list_all_nodes.append(self.Root)
            return list_all_nodes
        else:
            def find(struct):
                list_all_nodes.append(struct)
                if len(struct.Children) > 0:
                    for child in struct.Children:
                        find(child)
                return list_all_nodes
            return find(self.Root)
        # код выдачи всех узлов дерева в определённом порядке

    def FindNodesByValue(self, val):
        if self.Root == None:
            return []
        else:
            list_find_nodes = []
            def find(struct, val):
                if len(struct.Children) > 0 and struct.NodeValue != val:
                    for child in struct.Children:
                        if child.NodeValue == val:
                            list_find_nodes.append(child)
                            return list_find_nodes
                        find(child, val)
                elif struct.NodeValue == val:
                    list_find_nodes.append(struct)
                    return list_find_nodes
                else:
                    return []
            find(self.Root, val)
            return list_find_nodes
        # ваш код поиска узлов по значению

    def MoveNode(self, OriginalNode, NewParent):
        if len(self.Root.Children) == 0 or OriginalNode == self.Root or self.Count() == 0:
            return
        else:
            temp_parent = OriginalNode.Parent
            for child in temp_parent.Children:
                if child == OriginalNode:
                    temp_parent.Children.remove(child)
            NewParent.Children.append(OriginalNode)
            OriginalNode.Parent = NewParent

        # код перемещения узла вместе с его поддеревом --
        # в качестве дочернего для узла NewParent

    def Count(self):
        list_count = []
        if self.Root == None:
            return 0
        else:
            def find(struct):
                list_count.append(1)
                if len(struct.Children) > 0:
                    for node in struct.Children:
                        find(node)
                return list_count
            size = len(find(self.Root))
            return size
        # количество всех узлов в дереве

    def LeafCount(self):
        if self.Root == None:
            return 0
        elif len(self.Root.Children) == 0:
            return 1
        else:
            def find(struct, count):
                if len(struct.Children) > 0:
                    for child in struct.Children:
                        count = find(child, count)
                else:
                    count += 1
                return count
            return find(self.Root, self.count_leaf)
        # количество листьев в дереве
    def GetLevel(self, start_node):
        if start_node == None:
            return 0
        elif len(start_node.Children) == 0:
            return 1
        list_current_nods = self.GetAllNodes()
        list_count = []
        for node in list_current_nods:
            count = 0
            while node.Parent != None:
                node = node.Parent
                count += 1
            list_count.append(count)
        return max(list_count)

    def SubCount(self, start_node):
        list_count = []
        if start_node == None:
            return 0
        else:
            def find(struct):
                list_count.append(1)
                if len(struct.Children) > 0:
                    for node in struct.Children:
                        find(node)
                return list_count
            size = len(find(start_node))
            return size
        # количество всех узлов в под-дереве
    def CheckEven(self, start_node):
        if start_node == None:
            return
        else:
            if (self.SubCount(start_node) % 2) == 0:
                return True
            else:
                return False
        # проверка дерева на четность

    def EvenTrees(self):
        if self.Root == None or (self.Count() % 2) != 0:
            return []
        else:
            result_list = []
            nextNode_list = []
            start_node = self.Root
            while True:
                if len(start_node.Children) != 0:
                    for child in start_node.Children:
                        nextNode_list.append(child)
                        if self.CheckEven(child) == True:
                            result_list.append(start_node)
                            result_list.append(child)
                if len(nextNode_list) != 0:
                    start_node = nextNode_list.pop(0)
                else:
                    break

        return result_list
"""    
node1 = SimpleTreeNode(1, None)
node2 = SimpleTreeNode(2, None)
node3 = SimpleTreeNode(3, None)
node4 = SimpleTreeNode(6, None)
node5 = SimpleTreeNode(5, None)
node6 = SimpleTreeNode(7, None)
node7 = SimpleTreeNode(4, None)
node8 = SimpleTreeNode(8, None)
node9 = SimpleTreeNode(10, None)
node10 = SimpleTreeNode(11, None)
node11 = SimpleTreeNode(9, None)
node12 = SimpleTreeNode(12, None)
node13 = SimpleTreeNode(13, None)
node14 = SimpleTreeNode(15, None)

My_tree = SimpleTree(node1)
My_tree.AddChild(node1, node2)
My_tree.AddChild(node1, node3)
My_tree.AddChild(node1, node4)
My_tree.AddChild(node2, node5)
My_tree.AddChild(node2, node6)
My_tree.AddChild(node3, node7)
My_tree.AddChild(node4, node8)
My_tree.AddChild(node5, node9)
My_tree.AddChild(node6, node10)
My_tree.AddChild(node7, node11)
My_tree.AddChild(node8, node12)
My_tree.AddChild(node8, node13)
My_tree.AddChild(node11, node14)

node1 = SimpleTreeNode(1, None)
node2 = SimpleTreeNode(2, None)
node3 = SimpleTreeNode(3, None)
node6 = SimpleTreeNode(6, None)
node5 = SimpleTreeNode(5, None)
node7 = SimpleTreeNode(7, None)
My_tree = SimpleTree(node1)

node3 = SimpleTreeNode(3, None)
node6 = SimpleTreeNode(6, None)
node5 = SimpleTreeNode(5, None)
node7 = SimpleTreeNode(7, None)
node4 = SimpleTreeNode(4, None)
node8 = SimpleTreeNode(8, None)
node10 = SimpleTreeNode(10, None)

node9 = SimpleTreeNode(9, None)


My_tree = SimpleTree(node1)

My_tree.AddChild(node1, node2)
My_tree.AddChild(node1, node3)
My_tree.AddChild(node1, node6)
My_tree.AddChild(node2, node5)
My_tree.AddChild(node2, node7)
My_tree.AddChild(node3, node4)
My_tree.AddChild(node6, node8)
My_tree.AddChild(node8, node9)
My_tree.AddChild(node8, node10)


My_tree.AddChild(node1, node2)
My_tree.AddChild(node1, node3)
My_tree.AddChild(node1, node6)
My_tree.AddChild(node2, node5)
My_tree.AddChild(node2, node7)


res = My_tree.EvenTrees()
for i in res:
    print(i.NodeValue, ' ', end='')
#print(My_tree.Count())