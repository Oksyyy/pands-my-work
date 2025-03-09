# 5.2.2.student_info1.py
# Program Program that reads in studen name and their subjects and grades and store this information as dict
# Author: Oksana Abrosimova

student = {
    'name' : 'name_input',
    'courses' : []
}
# set a dictionary with key name and it's value to be updated by the input to student name
# set an empty list for courses inside the dict for student to enter several subjects

student['name'] = input('Please enter your name: ')
# update student name using input function

while True: # we need to use while loop becasue the initial courses list is empty, so for loops can't be used
# if value is not 0, empty, None it's always True. Using True in while loops ensures it runs infinitely until it's stopped
    subject_name = input('Please enter a subject name: ')
    if subject_name == '':
        break
    grade = input('Please enter grade for this subject: ')
    student['courses'].append({'subject name': subject_name , 'grade' : grade}) 

print (student)
