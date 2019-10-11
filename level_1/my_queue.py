import My_stack as ms

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        # вставка в хвост

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return

    def size(self):
        return len(self.queue)

    def rotate(self, N):
        if self.size() > N:
            tmp = self.queue[0:(self.size() - N)]
            k = self.size() - N
            i = 0
            while k < self.size():
                self.queue[i] = self.queue[k]
                i+=1
                k+=1
            k = N
            i = 0
            while k < self.size():
                self.queue[k] = tmp[i]
                k+=1
                i+=1
        else:
            return

    def print_all(self):
        if self.size() != 0:
            for i in range(self.size()):
                print(self.queue[i])
        else:
            return

class QueueStack:
    def __init__(self):
        self.st1 = ms.Stack()
        self.st2 = ms.Stack()

    def enqueue(self, item):
        self.st1.push(item)

    def dequeue(self):
        while self.st1.size() > 0:
            self.st2.push(self.st1.pop())
        return self.st2.pop()

    def print_all(self):
        if self.st1.size() !=0:
            while self.st1.size() > 0:
                tmp = self.st1.pop()
                self.st2.push(tmp)
            while self.st2.size() > 0:
                print(self.st2.pop())
        elif self.st2 != 0:
            while self.st2.size() > 0:
                print(self.st2.pop())
        else:
            return


