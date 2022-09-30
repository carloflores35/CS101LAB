########################################################################
##
## CS 101 Lab
## Program #
## Name
## Email
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################


# import statements
import string
# functions
def get_school(string):
    if string[5] == '1':
        return "School of Computing and Engineering SCE"
    elif string[5] == '2':
        return "School of Law"
    elif string[5] == '3':
        return "College of Arts and Sciences"
    else:
        return "Invalid School"
def get_grade(string):
    if string[6] == '1':
        return 'Freshman'
    elif string[6] == '2':
        return 'Sophomore'
    elif string[6] == '3':
        return 'Junior'
    elif string[6] == '4':
        return 'Senior'
    else:
        return "Invalid Grade"
def character_value(val):
    return string.ascii_uppercase.index(val)
   
def get_check_digit(string):
    for index in range(len(string)):
        char = string[index]
        checkdigit += (index + 1) * character_value(char)
    finalcheckdigit = checkdigit % 10
    return finalcheckdigit

    
    
if __name__ == "__main__":

    # main program
    librarycard = input('Enter Library Card. Hit Enter to Exit ==> ')
    print(character_value("A"))
    print(get_school(librarycard))
    print(get_grade(librarycard))
    print(get_check_digit(librarycard))
    print("Main Program")

