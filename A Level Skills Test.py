def showMenu():
  #displays the main menu
  print("1. Show all records")
  print("2. Search by name")
  print("3. Search by department")
  print("4. Search by salary")
  print("5. Add employee")
  print("6. Delete all employees")
  print("7. Exit")
	
def getChoice():
	#returns the users choice
  ok = False
  while not(ok):
    c = int(input("--->"))
    if c>=1 and c<=7:
      ok = True
    else:
      return "Please enter a number between 1 and 7"
  return c

def showRecord(r):
	#shows a single record
	print("--------------------")
	print("Name:\t\t"+r[0])
	print("Department:\t"+r[1])
	print("Age:\t\t"+str(r[2]))
	print("Salary:\t\t"+str(r[3]))

def showAllRecords(alist):
	#Shows all records in alist
	for r in alist:
		showRecord(r)

def searchByName(name, alist):
  for i in range(0,len(alist)):
    if [i][0] == name:
      return(employeelist[i])
    else:
      pass
    
def searchByDept(dept):
	pass

def searchBySal(sal):
	pass

def addEmployee(name, role, age,  sal, alist):
  alist.append([name, role, age, sal])
  return("Added Employee")

####### MAIN PROGRAM #########

employeelist = [ ["Alice", "Director", 43,80000], ["Bob", "Finance", 58,50000], ["Cat", "Marketing", 34,32000], ["Des", "IT", 23,45000],["Dan","IT",30,65000],["Nic","IT",30,65000],["Tim","IT",30,100000],["Jeff","Marketing",30,45000],["George","Finance",30,55000] ]

while True:
  showMenu()
  user = getChoice()
  if user == 1:
  	showAllRecords(employeelist)
  elif user == 2:
  	searchname = input("Please input the name you would like to search for: ")
  	print(searchByName(searchname, employeelist))
  elif user == 3:
  	searchdept = input("Please input the department you would like to search for: ")
  elif user == 4:
  	searchsal = input("Please input the salary you would like to search for: ")
  elif user == 5:
    employeeName = input("Please input the new employee's name: ")
    employeeRole = input("Please input the new employee's role: ")
    employeeAge = input("Please input the new employee's age: ")
    employeeSalary = input("Please input the new employee's salary: ")
    print(addEmployee(employeeName, employeeRole, employeeAge, employeeSalary, employeelist))
  elif user == 6:
    employeelist = []
  elif user == 7:
    exit()
