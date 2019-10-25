import My_HashTable as ht
# наследуйте этот класс от HashTable
# или расширьте его методами из HashTable
class PowerSet(ht.HashTable):

    def __init__(self):
        super(PowerSet, self).__init__(20000, 1)
        self.util_index = []
        self.size_count = 0
    def size(self):
        return self.size_count
        # количество элементов в множестве
    def seek_slot(self, value):
        count = 0
        index = self.hash_fun(value)
        while count <= self.size - 1:
            if self.slots[index] == None or self.slots[index] == value:
                return index
            if index + self.step > self.size-1:
                index = (index+self.step) - (self.size)
            else:
                index += self.step
            count += 1
        # находит индекс пустого слота для значения, или индекс слота с таким-же значением, и возвращает этот индекс, или None - в противном случае.
        return None

    def put(self, value):
        value = str(value).strip()
        index_put = self.seek_slot(value)
        if index_put != None and self.slots[index_put] == value:
            self.slots[index_put] = value
        elif index_put != None:
            self.slots[index_put] = value
            self.size_count += 1
            self.util_index.append(index_put)
            return index_put
        else:
            return None
        # всегда срабатывает

    def get(self, value):
        value = str(value).strip()
        if self.slots[self.seek_slot(value)] == value:
            return True
        else:
            return False
        # возвращает True если value имеется в множестве,
        # иначе False


    def remove(self, value):
        value = str(value).strip()
        index_remove = self.seek_slot(value)
        if self.slots[index_remove] == value:
            self.slots[index_remove] = None
            self.size_count -= 1
            self.util_index.remove(index_remove)
            return True
        else:
            return False
        # возвращает True если value удалено
        # иначе False

    def intersection(self, set2):
        # пересечение текущего множества и set2
        set3 = PowerSet()
        for i in self.util_index:
            value = self.slots[i]
            if set2.get(value):
                set3.put(value)
        return set3

    def union(self, set2):
        # объединение текущего множества и set2
        set3 = PowerSet()
        for i in self.util_index:
            value = self.slots[i]
            if set2.get(value) == False:
                set3.put(value)
        for i in set2.util_index:
            value = set2.slots[i]
            if self.get(value) == False:
                set3.put(value)
        return set3

    def difference(self, set2):
        # разница текущего множества и set2
        set3 = PowerSet()
        for i in self.util_index:
            value = self.slots[i]
            if set2.get(value) == False:
                set3.put(value)
        return set3

    def issubset(self, set2):
        for i in set2.util_index:
            value = set2.slots[i]
            if self.get(value) == False:
                return False
        return True
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
