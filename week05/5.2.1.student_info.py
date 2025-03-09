student = {
    'name' : 'Mary',
    'courses' : [
        {
            'subject name' : 'Programming',
            'grade' : 45
        },
        {
            'subject name' : 'History',
            'grade' : 99
        }
    ]   
}
print(student['name'])

for subject in student['courses']:
    print(f'\t {subject["subject name"]} : {subject["grade"]}')