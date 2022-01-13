from dataclasses import dataclass;import datetime;import gc;import time;from typing import *;from sys import argv;import pyfiglet

"""
	 📝 Notebook app ✨
	 - Simple note taking app with dictionaries 
	 TODO: 	
	 - Implement a GUI 👀(Ideally a full native ui, but cli will do)
	 - Implement saving to disk using Pickle 💾
"""

@dataclass(unsafe_hash = True)
class page:
	"""
	This is the page dataclass (which is basically the python version of structs, i guess) that is used to hold the data of a page.
	"""
	title     :  str
	content	  :  str
	created   :  datetime
	modified  :  datetime

class cmds():
	def yyxy(self):
		print("stan loona for clear skin")
	def help(self):
		print("""
Welcome to TwoNote!
- To view a list of available commands, type ls command
- To learn how to use TwoNote, type tntutor
- To exit, type qa
		""")

	def ls(self, arg):
		if arg == "cmds" or "commands":
			print("""
Commands:
h or help: print help
n or new: new page
w or write or save or wo: write out pages to disk
qa: quit all (WARNING: DOES NOT FLUSH DATA! MAKE SURE TO SAVE BEFORE!)
f or find or search: search for pages based on tags and titles
ls command: list available commands
ls page: list pages
			""")

	def write(self):
		pass

	def find(self):
		pass

	def new(self):
		pass

	# Aliases - these are just to provide multiple names for one command without writing it out several times
	h    =  help
	w    =  write
	wo   =  write
	save =  write
	f    =  find
	n    =  new

class App():
	def __init__(debug : bool = False):
		__debugEnabled__ = debug
		__notebook__ = {}


	def addpage(self, t : str, c : str = "", tags : List = []) -> None:
		"""
		addpage() (public function)
		- adds a new page to the notebook
		- returns None (void)
		"""
		self.__notebook__[t] = page(title = t, content = c, created = time.time())

	def addtag(self, t, n) -> None:
		"""
		addtag() 
		- add tag t to notebook n
		- returns None
		"""
		self.tags[n] = t

	def main(self) -> None:
		banner = pyfiglet.figlet_format("TwoNote")
		print("Welcome to TwoNote! \nType help or h to see more information, or type qa to quit.\n")
		print(banner)
		lCmds = cmds()
		Alive = True
		while Alive == True:
			command : str = input("->  ")
			if command == "qa":
				confirm = input("really wanna quit? (y / n):  ")
				if confirm in "Yy":
					print("goodbye!")
					Alive = False
				else:pass;

			else:
				if " " in command:
					strarg  : str = str(command.split(" ")[1])
					command = str(command.split(" ")[0])
					try:
						method = getattr(lCmds, command)
					except:
							print("Unrecognized command %s. Enter h or help for information." % command)
					else:
						try:method(str(strarg));
						except: print("Trailing argument %s in command %s." %(strarg, command))

				else:
					try:
						method = getattr(lCmds, command)
					except:
							print("Unrecognized command %s. Enter h or help for information." % command)
					else:
						try:method();
						except: print("Command %s requires an argument." % command)

run = App()
run.main()