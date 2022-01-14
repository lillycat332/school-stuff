from dataclasses import *;import datetime;import time;from typing import *;from sys import argv;from os import system, name; import threading
import pyfiglet # type: ignore

"""
	 📝 Notebook app ✨
	 - Simple note taking 📝 app with dictionaries 
	 TODO:
	 - Implement a full UI 👀 (Ideally a full native ui, but CLI  will do)
	 - Implement saving to disk using Pickle 💾
"""

@dataclass(unsafe_hash = True)
class page:
	"""
	This is the page dataclass (which is basically the python version of structs, i guess) that is used to hold the data of a page.
	"""
	title     :  str
	content	  :  str
	created   :  float
	#modified  :  datetime

class cmds:
	def help(self):
		print("""
Welcome to TwoNote!
- To view a list of available commands, type ls command
- To learn how to use TwoNote, type tntutor
- To exit, type qa
		""")

	def ls(self, arg):
		if arg == "cmds" or arg == "commands":
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

		elif arg == "notes" or arg == "pages":
			print(run.notebook)

	def write(self):
		pass

	def find(self):
		pass

	def clear(self):
		# clear clears the screen, but i can't just call system("clear") because windows is annoying and doesn't do clear, it does cls for whatever reason
		if name == 'nt':
			_ = system('cls')
		# for good operating systems, it calls clear 
		else:
			_ = system('clear')

	# Aliases - these are just to provide multiple names for one command without writing it out several times
	h    =  help
	w    =  write
	wo   =  write
	save =  write
	f    =  find

class App():
	def __init__(self):
		self.notebook : Dict = {"none" : None}

	def addpage(self, t : str, c : str = "", tags : List = []) -> None:
		"""
		addpage()
		- adds a new page named t with optional content c and optional tags t to the notebook
		- returns None (void)
		"""
		self.notebook[t] = page(title = t, content = c, created = time.time())

	# def addtag(self, t, n) -> None:
	# 	"""
	# 	addtag() 
	# 	- add tag t to notebook n
	# 	- returns None
	# 	"""
	# 	self.tags[n] = t

	def ContentView(self) -> None:
		banner = pyfiglet.figlet_format("TwoNote")
		print(banner)
		print("Welcome to TwoNote! \nType help or h to see more information, or type qa to quit.\n")
		lCmds = cmds()
		Alive = True

		while Alive:
			command : str = input("->  ")
			if command == "qa":
				confirm = input("really wanna quit? (y / n):  ")
				if confirm in "Yy":
					print("goodbye!")
					Alive = False
				else:pass;

			elif command == "new":
				self.EditorView()

			else:
				if " " in command:
					strarg  : str = str(command.split(" ")[1])
					command = str(command.split(" ")[0])
					try: method = getattr(lCmds, command)
					except: print("Unrecognized command %s. Enter h or help for information." % command)
					else:
						try: method(str(strarg));
						except Exception as e: print("Trailing argument %s in command %s. exception raised: %s" %(strarg, command, e))

				else:
					try: method = getattr(lCmds, command)
					except: print("Unrecognized command %s. Enter h or help for information." % command)
					else:
						try: method();
						except: print("Command %s requires an argument." % command)

	def EditorView(self) -> None:
		__Alive : bool = True
		while __Alive:
			name    = input("Enter the name of the note ->  ")
			content = input("Enter the content of the note ->  ")
			tags    = input("Enter some tags (seperated by commas)->  ").split(",")
			self.addpage(name, content, tags)
			__Alive = False

run = App()
run.ContentView()