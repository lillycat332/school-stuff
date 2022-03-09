from typing import *

class dfs():
	def __init__(self) -> None:
		self.__visited : Set[Any] = set()

	def depthFirstRecursive(self, graph, node) -> Set[Any]:
		"""
		Depth first traversal - recursive
		"""
		if node not in self.__visited:
			self.__visited.add(node)
			print(node)
			for neighbor in graph[node]:
				self.depthFirstRecursive(graph, neighbor)
		return self.__visited

maze = {0: [1,5,4], 1:[2,0], 2:[3,1,6], 3:[2], 4:[0,8], 5:[0,6,9,8], 6:[2,7,9,5], 7:[6], 8:[4,5,9], 9:[8,5,6]}
inst = dfs()

print("Visited nodes: %s" % inst.depthFirstRecursive(maze, 0))
