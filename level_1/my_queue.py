import Stack
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        # вставка в хвост

    def dequeue(self):
        if self.size() > 0:
            self.queue.pop(0)
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
        for i in range(self.size()):
            print(self.queue[i])

class QueueStack:
    def __init__(self):
        self.st1 =

qe = Queue()

n = 9

for i in range(1,9):
    qe.enqueue(i)

qe.rotate(n)

qe.print_all()

print('stop')