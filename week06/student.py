# student_py
# Function that allows to add and view students infation
# Author: Oksana Abrosimova

def menu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) Vew students")
    print("\t(q) Quit")
    option = input("Type one letter (a/v/q): ")
    return option

def doAdd(students):
    astudent = {} # initiate an empty dictunary to add a student
    astudent["name"] = input("Please enter your name: ") # add key:value pair to the student dict 
    astudent["modules"] = readModules() # refer to readModules function for modules since they are more complex than entering a name

    students.append(astudent) # add a student's name & modules to an empty students list

def readModules():
    modules = [] # initiate a list to add modules & grades
    module_name = input("\tEnter the first module name (blank to quit): ") # prompt the user for an option to add a module name
    while module_name != '': # if module name is not blank, then create a module
        aModule = {} # initiate empty module
        aModule["name"] = module_name # assigned value (user's input) to the key  aModule["name"] 
        aModule["grade"] = int(input("\t\tEnter grade for this module: ")) # prompt the user to entar a grade for this module
        modules.append(aModule) # add created module dictionary to modules list
        module_name = input("\tEnter next module name (blank to quit): ") # ask the user to enter next module
    return modules # function returns a list of student dictionaries representing modules with grages


def doView(students):
     for student in students: # iterate over each student in students list
         print(student["name"]) # show student's name 
         displayModules(student["modules"]) # call displayModules() function to show modules for this student

def displayModules(modules): # this function exists to show student modules under doView() function
    print(f"\tModule name t\Grade") 
    for module in modules: # iterate over modules for a student that is being viewed and show their modules and grades
        print(f"\t{module['name']} \t{module['grade']}")


students = [] 
choice = menu()

while choice != 'q':
    # print(choice)
    if choice == 'a':
        doAdd(students)
        # print(choice)
    elif choice == 'v':
         doView(students)
         # print(choice)
    elif choice != 'q':
        print("PLease select either a, v, or q")
    choice = menu()

