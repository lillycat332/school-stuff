from arrayLib import *
from typing import *

class Stack(Array):
	def __init__(self, size : int) -> None:
		self.__size = size
		self.__myArray = Array(size)
		self.__TOS = int(0)

	class StackException(Exception):
		def __init__(self, value : str) -> None:
			self.value = value;
		def toString(self) -> str:
			return self.value;

	def push(self, value : Any) -> None:
		# Push - Pushes a given value to the stack.
		# Accepts a value of any type.
		# If stack is full, then raises Stack Overflow
		if self.__TOS - 1 < self.__size:
			self.__myArray.assign(self.__TOS, value)
			#print(self.__TOS)

			self.__TOS += int(1)
			#print(self.__TOS)

		else:
			raise Exception("Stack Overflow")

	def pop(self) -> Any:
		# Pop - Removes the top element from the stack.
		# no inputs
		# returns value of the top element.
		if self.__TOS > 0:
			current = self.__myArray.get(self.__TOS - 1)
			#self.__myArray.assign(self.__TOS - 1, None)
			self.__TOS -= 1 
			return current
		else:
			raise Exception("Stack Empty")

	def printArray(self) -> None:
		# printArray - used to Print contents of an array. 
		for i in reversed(range(0,self.__size)):
			print(self.__myArray.get(i))

class RPNApp(object):
	def __init__(self) -> None:
		self.__myStack = Stack(4)
		self.__runApp = True

	def eval(self, expression : str) -> str:
		exp : list[Any] = expression.split()
		operators = ["*", "/", "-", "+"]
		for token in exp:
				if token.exp in operators:
					arg2 = self.__myStack.pop()
					arg1 = self.__myStack.pop()
					result = 1
					self.__myStack.push(result)
				else:
					self.__myStack.push(float(token))
		return str(self.__myStack.pop())

	def main(self) -> None:
		# value = str(input("Enter a value in RPN: ")) 
		# take an RPN input
		__expression = "1 2 * "
		print(eval(__expression))

PolishApp = RPNApp()
PolishApp.main()

# class App(object):
# 	def __init__(self):
# 		self.__myStack = Stack(4)
# 		self.__runApp = True

# 	def main(self):
# 		# main test application
# 		while self.__runApp == True:
# 			__choice = int(input("Enter a Value (1 - Pop, 2 - Push): ")) # take input for pop or push
# 			if __choice == 1:
# 				try:
# 					self.__myStack.pop()
# 					print("Topmost Item popped")
# 					self.__myStack.printArray()
# 				except:
# 					print("Failed to pop")
# 			if __choice == 2:
# 				try:
# 					self.__myStack.push(input("Enter an item to push to the stack: "))
# 					self.__myStack.printArray()
# 				except:
# 					print("Failed to push")
