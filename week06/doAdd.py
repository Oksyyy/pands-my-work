students = []

def doAdd(students):
    astudent = {} # initiate an emptydictunary to add a student
    astudent["name"] = input("Please enter your name: ") # add key:value pair to the student dict 
    astudent["modules"] = readModules() # refer to readModules function for modeuls since they are more complex than entering a name

    students.append(astudent) # add a student's name & modules to an empty students list

def readModules():
    modules = [] # initiate a list to add modules & grades
    module_name = input("\tEnter the first module name (blank to quit): ")
    while module_name != '':
        aModule = {}
        #modules.append(input("Enter module name: "))
        aModule["name"] = module_name
        aModule["grade"] = int(input("\t\tEnter grade for this module: "))
        modules.append(aModule)
        module_name = input("\tEnter next module name (blank to quit): ")
    return modules

doAdd(students)

print(students)