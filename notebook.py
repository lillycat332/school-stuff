from dataclasses import dataclass;import datetime;from typing import *

@dataclass(unsafe_hash = True)
class page:
		title 	 : str #(hash=True)
		content	 : str
		created  : datetime
		modified : datetime

class NotebookView():
	pass

class ContentView():
	pass

class App():
	def __init__():
		__tags   =  {}
		#names  =  {}
		
	def addtag(self, t, n):
		self.tags[n] = t

	def main() -> None:
		print("fuck you")
		pass

h = App
h.main()