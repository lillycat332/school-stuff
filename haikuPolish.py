from arrayLib import *
import operator


class Stack(Array):
    def __init__(self, size):
        self.__size = size
        self.__myArray = Array(size)
        self.__TOS = int(0)

    class StackException(Exception):
        def __init__(self, value): self.value = value
        def toString(self): return self.value

    def push(self, value):
        # Push - Pushes a given value to the stack.
        # Accepts a value of any type.
        # If stack is full, then raises Stack Overflow
        myvalue = value
        if self.__TOS - 1 < self.__size:
            self.__myArray.assign(self.__TOS, myvalue)
            # print(self.__TOS)

            self.__TOS += int(1)
            # print(self.__TOS)
        else:
            raise Exception("Stack Overflow")

    def pop(self):
        # Pop - Removes the top element from the stack.
        # no inputs
        # returns value of the top element.
        if self.__TOS > 0:
            current = self.__myArray.get(self.__TOS - 1)
            self.__myArray.assign(self.__TOS - 1, None)
            self.__TOS -= 1
            return current
        else:
            raise Exception("Stack Empty")

    def printArray(self):
        # printArray - used to Print contents of an array.
        for i in reversed(range(0, self.__size)):
            print(self.__myArray.get(i))


class RPNApp():
    # Comments are overrated
    def __init__(self, expression):
        self.__operators = {'+': operator.add, '-': operator.sub,
                            '*': operator.mul, '/': operator.truediv}
        self.__Stack = Stack(4)
        self.__tokenList = expression.split(" ")

    def main(self):
        while True:
            for token in self.__tokenList.split():
                if token in self.__operators:
                    op1, x = self.__Stack.pop(), self.__Stack.pop()
                    op2 = self.__operators[token](op1, y)
                else:
                    result = float(token)
                self.__Stack.push(result)
            if Stack.getTos:
                print(self.__Stack.pop())
                return self.__Stack.pop()


testvar = input("Enter an expression: ")
test = RPNApp(testvar)
print(test.main())
