from arrayLib import *


class Queue(Array):
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


class testApp():
    def __init__(self, l):
        self.__myQueue = Queue(l)

    def main(self):
        while True:
            inputVal = input(
                "Please enter a value to enqueue, or nothing to dequeue: ")
            if inputVal == "":
                self.__myQueue.dequeue()
                self.__myQueue.printArray()
            else:
                self.__myQueue.enqueue(inputVal)
                self.__myQueue.printArray()


myApp = testApp(8)
myApp.main()
