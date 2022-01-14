from dataclasses import *;import time;from typing import *;from os import system, name;import threading;from pyfiglet import figlet_format

"""
	 📝 Notebook app ✨
	 - Simple note taking 📝 app with dictionaries 
	 TODO:
	 - Implement a full UI 👀 (Ideally a full native ui, but CLI will do)
	 - Implement saving to disk using Pickle 💾
"""

@dataclass()
class page:
	"""
	This is the page dataclass (which is basically the python version of a hashable struct, i guess?) that is used to hold the data of each page.
	"""
	title     :  str
	content	  :  str
	created   :  float
	#modified  :  datetime

class strings():
	helpmsg = "Welcome to TwoNote!\n- To view a list of available commands, type ls command\n- To learn how to use TwoNote, type tntutor\n- To exit, type qa"

	cmds = """Commands:
h or help: print help
n or new: new page
w or write or save or wo: write out pages to disk
qa: quit all (WARNING: DOES NOT FLUSH DATA! MAKE SURE TO SAVE BEFORE!)
f or find or search: search for pages based on tags and titles
ls command: list available commands
ls page: list pages"""

class cmds:
	strn = strings()
	def help(self) -> None:
		print(strn.helpmsg)

	def ls(self, arg : str) -> None:
		if arg == "cmds" or arg == "commands":
			print(strn.cmdslist)

		elif arg == "notes" or arg == "pages":
			print(run.notebook)
		else: print("ls: unrecognized argument %s" % arg)

	def write(self) -> None:
		pass

	def find(self) -> None:
		pass

	def clear(self) -> None:
		""" clear clears the screen, but i can't just call system("clear") because windows is annoying and doesn't do clear, it does cls for whatever reason so this is just a check whether on a posix (good) os or a windows (awful) os"""
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

class App(object):
	def __init__(self) -> None:
		self.notebook : Dict[str, Any] = {}

	def addpage(self, t : str, c : str = "", tags : List[str] = []) -> None:
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
		banner = figlet_format("TwoNote")
		print(banner)
		print("Welcome to TwoNote! \nType help or h to see more information, or type qa to quit.\n")
		lCmds = cmds()
		Alive = True

		while Alive:
			command : str = input("->  ")
			if command == "qa":
				confirm = input("really wanna quit? any unsaved changes will be lost! (y / n):  ")
				if confirm in "Yy":
					print("goodbye!")
					Alive = False
				else:pass;

			elif command == "new":
				self.NewNoteView()

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

	def NewNoteView(self) -> None:
		__Alive : bool = True
		while __Alive:
			name    = input("Enter the name of the note ->  ")
			content = input("Enter the content of the note ->  ")
			tags    = input("Enter some tags (seperated by commas)->  ").split(",")
			self.addpage(name, content, tags)
			__Alive = False

run = App()
run.ContentView()