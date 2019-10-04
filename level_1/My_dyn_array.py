import ctypes


class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if self.__len__()!=0:
            if i > self.count or i < 0:
                raise IndexError('Index is out of bounds')
            elif i == self.count:
                self.append(itm)

            else:
                if self.count == self.capacity:
                    self.resize(2 * self.capacity)

                tmp_loc = self.make_array(self.count-i)
                j = 0
                for k in range(i, self.count):
                    tmp_loc[j] = self.array[k]
                    j+=1
                self.array[i] = itm
                j = 0
                for k in range(i+1, self.count+1):
                    self.array[k] = tmp_loc[j]
                    j+=1
                self.count +=1
        else:
            raise IndexError('Index is out of bounds')
            return


    def delete(self, i):
        if self.__len__()!=0:
            if i >= self.count or i < 0:
                raise IndexError('Index is out of bounds')
            elif i == (self.count-1):
                tmp_loc = self.make_array(self.count-1)
                for k in range(0, i):
                    tmp_loc[k] = self.array[k]
                self.array = tmp_loc
                self.count -=1
                if self.count < (0.5 * self.capacity):
                    self.resize(int(self.capacity/1.5))
                return
            else:
                tmp_loc = self.make_array(self.count-1)

                j = 0
                for k in range(self.count):
                    if k != i:
                        tmp_loc[j] = self.array[k]
                        j+=1
                self.array = tmp_loc
                self.count -=1
                if self.count < (0.5 * self.capacity):
                    self.resize(int(self.capacity/1.5))
                return
        else:
            raise IndexError('Index is out of bounds')
            return

"""
da = DynArray()
for i in range(16):
    da.append(i)
    #print(da[i])
print('count:', da.count)
da.insert(12,99)
print('count:', da.count)
print('capacity:', da.capacity)
for i in range(da.count):
    print(da[i])

print('count:', da.count)
print('capacity:', da.capacity)

da.delete(12)
da.delete(15)

print('count:', da.count)
print('capacity:', da.capacity)
for i in range(da.count):
    print(da[i])
for i in range(15, 22):
    da.append(i)

print('count:', da.count)
print('capacity:', da.capacity)

"""