import math
#Introduction to thje grade calculator
print('**** Hello there! Welcome to the LAB grade calculator! ****\n')
#This identifies who we are grading for
name = input('Who are we calculating grades for? ==> ')
print()
#This identifies the labs grade
lab_grade = int(input('Enter the Labs grade: ==> '))
#Fixes incorrect inputs
if lab_grade > 100:
    lab_grade = 100
    print('The lab grade value should have been 100 or less. It has changed to 100.')
elif lab_grade < 0:
    lab_grade = 0
    print('The lab grade value should have been 100 or less. It has changed to 0.')
print()
#This identifies the lab exams grade
lab_exams = int(input('Enter the Lab Exams grade: ==> '))
#Fixes incorrect inputs
if lab_exams > 100:
    lab_exams = 100
    print('The lab exams value should have been 100 or less. It has changed to 100.')
elif lab_exams < 0:
    lab_exams = 0
    print('The lab exams value should have been 100 or less. It has changed to 0.')
print()
#This identifies the attendance grade
attendance = int(input('Enter the Attendance grade: ==> '))
#Fixes incorrect inputs
if attendance > 100:
    attendance = 100
    print('The attendance value should have been 100 or less. It has changed to 100.')
elif attendance < 0:
    attendance = 0
    print('The attendance value should have been 100 or less. It has changed to 0.')
print()
#This calculates the numerical value of the grade, accounting of the weighting of each category of grade
weighted_grade = ((lab_grade * (.7)) + (lab_exams * (.2)) + (attendance * (.1)))
#Each if statements covers each range and assigns a letter grade
if 90 <= weighted_grade < 100:
    letter_grade = 'A'
if 80 <= weighted_grade < 90:
    letter_grade = 'B'
if 70 <= weighted_grade < 80:
    letter_grade = 'C'
if 60 <= weighted_grade < 70:
    letter_grade = 'D'
if 0 <= weighted_grade < 60:
    letter_grade = 'F'
#States weighted grade and letter grade
print(f'The weighted grade for {name} is {weighted_grade}')
print(f'{name} has a letter grade of {letter_grade}\n')
#Conclusion
print('**** Thank you for using the LAB grade calculator! ****')

