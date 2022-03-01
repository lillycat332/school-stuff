import typing

class Node():
	def __init__(self, data = 0) -> None:
		# initializes node
		self.left  = None
		self.right = None
		self.data = data

class Tree():
	"""
	Tree class, which holds all the nodes and provides functions to manipulate the tree.
	"""
	def createNode(self, data) -> Node:
		# returns a new node
		return Node(data)

	def insertNode(self, node, data) -> Node:
		if node is None:
			return self.createNode(data)

		# inserts node at right if inserted value is greater than parent, else insert on left
		if data < node.data:
			node.left = self.insertNode(node.left, data)

		elif data > node.data:
			node.right = self.insertNode(node.right, data)

		return node

	def traverseInOrder(self, root) -> list:
		result = [ ]
		if root:
			result = self.traverseInOrder(root.left)
			result.append(root.data)
			result += self.traverseInOrder(root.right)
		return result

	def search(self, node, data):
		if node is None or node.data == data:
			return node

		if node.data < data:
			return self.search(node.right, data)
		else:
            		return self.search(node.left, data)

def main():
	tree = Tree()
	ready = False
	while not ready:
		ready = True
		try:
			dataset = [int(i) for i in input("Input a comma seperated list of integers:  ").split(",")]

		except(ValueError):
			print("Input not an Comma-seperated list of integers.")
			ready = False

	print(dataset)
	root = None
	root = tree.insertNode(root, 0)
	for value in dataset:
		tree.insertNode(root, value)
	print("In Order Traversal:")
	print(tree.traverseInOrder(root))

main()
