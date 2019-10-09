class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() != 0:
            return self.stack.pop(0)
        else:
            return None # если стек пустой

    def push(self, value):
        if self.size() != 0:
            self.stack.insert(0, value)
        else:
            self.stack.append(value)

    def peek(self):
        if self.size() != 0:
            return self.stack[0]
        else:
            return None  # если стек пустой

def skobki(string):
    st1 = Stack()
    count_open = 0
    count_close = 0
    if len(string) != 0:
        for i in range(len(string)-1,-1,-1):
            st1.push(string[i])
        if st1.peek() == ')':
            return False
        else:
            st1.pop()
            count_open += 1
            while st1.size() > 0:
                itm = st1.pop()
                if itm == '(':
                    count_open += 1
                elif itm == ')':
                    count_close += 1
                if st1.size()==0 and itm == '(':
                    return False
            if count_open == count_close:
                return True
            else:
                return False
    else:
        return

def StackToStack(string):
    st1 = Stack()
    st2 = Stack()
    if len(string) != 0:
        for i in range(len(string)-1,-1,-1):
            if string[i] != ' ':
                st1.push(string[i])
        while st1.size() > 0:
            tmp = st1.pop()
            if (tmp != '+') and (tmp != '*') and (tmp != '='):
                st2.push(int(tmp))
            elif tmp == '+' and st2.size != 0:
                rez = st2.pop() + st2.pop()
                st2.push(rez)
            elif tmp == '*' and st2.size != 0:
                rez = st2.pop()*st2.pop()
                st2.push(rez)
            elif tmp == '=':
                return st2.pop()
    else:
        return




