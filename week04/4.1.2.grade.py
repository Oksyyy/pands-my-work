grade = float(input('Enter the percentage: '))

rounded_grade = round(grade)

if rounded_grade <0 or rounded_grade >100:
    print('Please enter a bumber between 0 and 100')
elif rounded_grade < 40:
    print('Fail')
elif rounded_grade >= 40 and rounded_grade <50:
    print/('Pass')
elif rounded_grade >= 50 and rounded_grade <=59:
    print('Merit 2')
elif rounded_grade >= 60 and rounded_grade <=69:
    print('Merit 1')
else:
    print('Distinction') 