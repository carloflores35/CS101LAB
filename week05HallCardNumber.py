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
def character_value(char):
    alphabetaerobics = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return alph.find(char)
def get_check_digit(string):
    alphabetaerobics = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    total = 0
    index = 0
    for i in card[0:10]:
        if i in alphabetaerobics:
            total += character_value(i)* (index + 1)
        elif i == '0':
            total += 0 * (index + 1)
        elif i == '1':
            total += 1 * (index + 1)
        elif i == '2':
            total += 2 * (index + 1)
        elif i == '3':
            total += 3 * (index + 1)
        elif i == '4':
            total += 4 * (index + 1)
        elif i == '5':
            total += 5 * (index + 1)
        elif i == '6':
            total += 6 * (index + 1)
        elif i == '7':
            total += 7 * (index + 1)
        elif i == '8':
            total += 8 * (index + 1)
        elif i == '9':
            total += 9 * (index + 1)
        index += 1
    digit = total % 10
    return digit
def verify_check_digit(string):
    if len(string) != 10:
        return (False, "The length of the number given must be 10")
    if string[0:5].isalpha() == False:
        spot = 0
        for i in string[0:5]:
            if i.isalpha() == False:
                wrong = i
                break
            num+=1
        a = f"The first 5 characters must be A-Z, the invalid character is at {spot} is {wrong}"  
        return (False, a)
    if string[7:10].isdigit() == False:
        spot1 = 7
        for i in string[7:10]:
            if i.isdigit() == False:
                wrong1 = i
                break
            spot1+=1
        b = f"The last 3 characters must be 0-9, the invalid character is at {spot1} is {wrong1}"  
        return (False, b)
    if string[5] != '1' and string[5] != '2' and string[5] != '3':
        return (False, "The sixth character must be 1 2 or 3")
    if string[6] != '1' and string[6] != '2' and string[6] != '3' and string[6] != '4':
        return (False, "The seventh character must be 1 2 3 or 4")
    if int(string[9]) != get_check_digit(string):
        c = f"Check Digit {string[9]} does not match calculated value {get_check_digit(string)}"
        return (False, c)
    else:
        return True
if __name__ == "__main__":

# main program
    print("Linda Hall")
    print("Library Card Check")
    print("========================================================")
    card = '0'
    while card != '\n':
        librarycard = input('Enter Library Card. Hit Enter to Exit ==> ')
        if verify_check_digit(librarycard) == True:
            print('Library card is valid.')
            print(get_school(librarycard))
            print(get_grade(librarycard))
            print(get_check_digit(librarycard))
            print()
            librarycard = input('Enter Library Card. Hit Enter to Exit ==> ')
        else:
            print('Library card is invalid.')
            print(get_school(librarycard))
            print(get_grade(librarycard))
            print(get_check_digit(librarycard))
            print()
            librarycard = input('Enter Library Card. Hit Enter to Exit ==> ')
