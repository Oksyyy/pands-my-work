# student_py
# Function that allows to add and view and save students information
# Author: Oksana Abrosimova

import json # import json module for doSave() function that saves students details

def menu(): # create a function to dysplay menu options for a user to pick and enter
    print("What would you like to do?")
    print("\t(a) Add new student") # \t prints on a new line
    print("\t(v) View students")
    print("\t(s) Save students")
    print("\t(l) Load students")
    print("\t(q) Quit")
    option = input("Type one letter (a/v/q): ") # prompt a user to enter their selected choice
    return option # return to the main program user's menue choice

def doAdd(students): # create a function to add students
    astudent = {} # initiate an empty dictunary to add a student
    astudent["name"] = input("Please enter your name: ") # add key:value pair to the student dict, where key is name & value is user input
    astudent["modules"] = readModules() # refer to a separate readModules function for adding modules since they are more complex than entering a name

    students.append(astudent) # add student's name & modules to an empty students list

def readModules(): # create a function to add modules for a student
    modules = [] # initiate a list to add modules & grades
    module_name = input("\tEnter the first module name (blank to quit): ") # prompt the user to add a module name
    while module_name != '': # if module name is not blank, then create a module
        aModule = {} # initiate empty dictionary for a module
        aModule["name"] = module_name # assign value (user's input) to the key  aModule["name"] 
        aModule["grade"] = int(input("\t\tEnter grade for this module: ")) # prompt the user to enter a grade for this module
        modules.append(aModule) # add created module dictionary to the modules list
        module_name = input("\tEnter next module name (blank to quit): ") # ask the user to enter next module
    return modules # function returns a list of student dictionaries representing modules with grages


def doView(students):  # create a function to students
     for student in students: # iterate over each student in students list
         print(student["name"]) # show student's name 
         displayModules(student["modules"]) # call displayModules() function to show modules for this student

def displayModules(modules): # this function exists to show student modules under doView() function
    print(f"\tModule name t\Grade") 
    for module in modules: # iterate over modules for a student that is being viewed and show their modules and grades
        print(f"\t{module['name']} \t{module['grade']}")

def doSave(students): # create a function to save a student (dictionary object) into an existing file
    with open('studentData.json', 'w') as f: # open file for writing 
        print("Students saved") # give a message to a user that student information was saved
        return json.dump(students, f) # use dump function to save a dict (student) as json into a file

def doLoad(students):
    with open('studentData.json', 'r') as f: 
        readStudent = json.load(f)
        print(students)
        return readStudent

students = [] # initiate an empti list to add students as part of doAdd() function
choice = menu() # call menue function

while choice != 'q': # call functions based on user's choie
    if choice == 'a':
        doAdd(students)

    elif choice == 'v':
         doView(students)

    elif choice =='s':
        doSave(students)
    
    elif choice =='l':
        doLoad(students)

    elif choice != 'q':
        print("PLease select either a, v, or q")

    choice = menu()

