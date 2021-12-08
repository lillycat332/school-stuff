from arrayLib import *
 
class naiveQueue(Array):
    def __init__(self, l):
        self.__myArray = Array(l)
        self.__head = 0
        self.__tail = 0
        self.__size = l

    def enqueue(self, v):
        self.__myArray.assign(self.__tail, v)
        self.__tail += 1

    def dequeue(self):
        r = self.__myArray.get(self.__head)
        self.__head += 1
        return r

    def printArray(self):
        # printArray - used to Print contents of an array.
        for i in range(0, self.__size):
            print(self.__myArray.get(i))

class circularQueue():
    def __init__(self, l):
        self.__queue = Array(l)
        self.__max = l - 1
        self.__head = 0
        self.__tail = 0
       
    def enqueue(self, newitem):
        if ((self.__tail + 1) % self.__max == self.__head):
            print("The circular queue is full")

        elif (self.__head == -1):
            self.__head = 0
            self.__tail = 0
            self.queue.assign(self.__tail, newitem)
        else:
            self.__tail = (self.__tail + 1) % self.__max
            self.__queue.assign(self.__tail, newitem)

    def dequeue(self):
        if (self.__head == -1):
            print("circular queue is empty")

        elif (self.__head == self.__tail):
            v = self.__queue.get(self.__head)
            self.__head = -1
            self.__tail = -1
            return v
        else:
            v = self.__queue.get(self.__head)
            self.__head = (self.__head + 1) % self.__max
            return v

    def printqueue(self):
        for i in range(0, self.__queue.getSize() - 1):
            print(self.__queue.get(i))
 
class priorityQueue():
    def __init__(self, l1, l2):
        self.__list = []
        for i in range(0, l1):
            self.__list.append(circularQueue(l2))
           
    def enqueue(self, q, n):
        self.__list[q].enqueue(n)
       
    def dequeue(self):
        for i in self.__list():
           
            self.__list[q].dequeue()
       
        
    def prin(self):
        for i in self.__list:
            print("\n")
            i.printqueue()
           
 
myq = priorityQueue(4, 4)
 
myq.enqueue(1, "Cat")
myq.prin()