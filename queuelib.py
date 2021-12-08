from arrayLib import *
 
class queueFullException(Exception):
    """raised when a queue is full"""
    pass

class queueEmptyException(Exception):
    """raised when a queue is full"""
    pass

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
    """
    Circular Queue
    - Holds n - 1 items
    - FIFO
    - head and tail loop from n to 0
    """
    def __init__(self, l):
        self.__queue = Array(l)
        self.__max = l - 1
        self.__head = 0
        self.__tail = 0
       
    def enqueue(self, newitem):
        """
        Enqueue:
        - Adds newitem to the queue
        - Moves the tail to accomodate for the new item
        - Handles the seamless transfer from end of queue to start with the head and tail pointers
        """
        if ((self.__tail + 1) % self.__max == self.__head):
            raise queueFullException()

        elif (self.__head == -1):
            self.__head = 0
            self.__tail = 0
            self.queue.assign(self.__tail, newitem)

        else:
            self.__tail = (self.__tail + 1) % self.__max
            self.__queue.assign(self.__tail, newitem)

    def dequeue(self):
        """
        Dequeue:
        - Dequeues the next item from the queue
        - Moves the head to accomodate for the removed item
        - Handles the seamless transfer from end of queue to start with the head and tail pointers
        """
        if (self.__head == -1):
            raise queueEmptyException()

        elif (self.__head == self.__tail):
            r = self.__queue.get(self.__head)
            self.__head = -1
            self.__tail = -1
            return r

        else:
            r = self.__queue.get(self.__head)
            self.__head = (self.__head + 1) % self.__max
            return r

    def printqueue(self):
        """
        Prints contents of queue for debug purposes
        """
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
            if i.get(i) != None:
                self.__list[q].dequeue()

        
    def prin(self):
        for i in self.__list:
            print("\n")
            i.printqueue()

myq = priorityQueue(4, 4)

while True:
    myq.enqueue(1, "Cat")
    myq.prin()