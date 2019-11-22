class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи
        self.HeapSize = 0

    def size_array(self, depth):
        n = 1
        for i in range(1, depth):
            n = (n * 2) + 1
        return n

    def MakeHeap(self, a, depth):
        # создаём массив кучи HeapArray из заданного
        # размер массива выбираем на основе глубины depth
        if len(a) == 0 or depth == None:
            return
        else:
            self.HeapSize = self.size_array(depth)
            while len(a) != 0:
                item = a.pop(0)
                self.Add(item)

    def GetMax(self):
        # вернуть значение корня и перестроить кучу
        if len(self.HeapArray) == 0:
            return -1 # если куча пуста
        else:
            item_out = self.HeapArray.pop(0)
            if len(self.HeapArray) > 1:
                self.MoveMaxUp()
            return item_out

    def MoveMaxUp(self):
        # перемещает новый элемент вверх до того, как найдет
        # большего по значению родителя
        index = len(self.HeapArray) - 1
        while index != 0:
            if self.HeapArray[index] > self.HeapArray[(index - 1) // 2]:
                tmp = self.HeapArray[(index - 1) // 2]
                self.HeapArray[(index - 1) // 2] = self.HeapArray[index]
                self.HeapArray[index] = tmp
            index = (index - 1) // 2
        return

    def Add(self, key):
        # добавляем новый элемент key в кучу и перестраиваем её
        if len(self.HeapArray) == 0:
            self.HeapArray.append(key)
            return True
        elif self.HeapSize > len(self.HeapArray):
            self.HeapArray.append(key)
            self.MoveMaxUp()
            return True
        elif self.HeapSize == len(self.HeapArray):
            return False # если куча вся заполнена

    def GetAll(self):
        if len(self.HeapArray) == 0:
            return
        else:
            for item in self.HeapArray:
                print(item)

"""
my_heap = Heap()
a = [6,9,4,7,3,1,8,2,5,11]
my_heap.MakeHeap(a, 4)
my_heap.GetAll()
print('______________________________________-')
my_heap.GetMax()
my_heap.GetAll()
print('______________________________________-')
my_heap.GetMax()
my_heap.GetAll()
"""