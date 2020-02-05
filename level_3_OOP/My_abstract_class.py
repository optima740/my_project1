from abc import*

class My_Abstract_Stack(ABC):
    CONST_POP_NIL = 0   # pop() еще не вызывался
    CONST_POP_OK = 1    # последняя pop() отработала нормально
    CONST_POP_ERR = 2   # стек пуст
    CONST_PEEK_NIL = 0  # peek() еще не вызывался
    CONST_PEEK_OK = 1   # последняя peek() вернула корректное значение
    CONST_PEEK_ERR = 2  # стек пуст
    CONST_PUSH_NIL = 0  # push() еше не вызывался
    CONST_PUSH_OK = 1   # последняя push() вернула корректное значение
    CONST_PUSH_ERR = 2  # стек заполнен

    def __init__(self):
        My_Abstract_Stack()

    # команды
    @abstractmethod
    def push(self):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def clear(self):
        pass

    # запросы
    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def size(self):
        pass

    # доп запросы
    @abstractmethod
    def get_pop_status(self):
        pass

    @abstractmethod
    def get_peek_status(self):
        pass

    @abstractmethod
    def get_push_status(self):
        pass

class BoundedStack(My_Abstract_Stack):

    def __init__(self, n=32):
        self.__max_size = n
        self.clear()

    def size(self):
        return len(self.__stack)

    def push(self, item):
        if self.size() < self.__max_size:
            self.__stack.append(item)
            self.__push_status = self.CONST_PUSH_OK
        else:
            result = 0
            self.__push_status = self.CONST_PUSH_ERR
            return result

    def clear(self):
        self.__My__stack = [] * self.__max_size
        self.__peek_status = self.CONST_PEEK_NIL
        self.__pop_status = self.CONST_POP_NIL
        self.__push_status = self.CONST_PUSH_NIL

    def peek(self):
        if self.size() > 0:
            result = self.__stack[-1]
            self.__peek_status = self.CONST_PEEK_OK
        else:
            result = 0
            self.__peek_status = self.CONST_PEEK_ERR
        return result

    def pop(self):
        if self.size() > 0:
            self.__stack.pop(-1)
            self.__pop_status = self.CONST_POP_OK
        else:
            self.__pop_status = self.CONST_POP_ERR

    def get_pop_status(self):
        return self.__pop_status

    def get_peek_status(self):
        return self.__peek_status

    def get_push_status(self):
        return self.__push_status


st = BoundedStack(7)
st.push(100)
st.push(101)
st.push(102)
st.push(103)
st.push(104)
st.push(105)
st.push(106)
st.push(107)
st.push(108)
st.clear()
st.push(123)
st.peek()
st.pop()

print('push {}, peek {}, pop {}'.format(st.get_push_status(), st.get_peek_status(), st.get_pop_status()))
