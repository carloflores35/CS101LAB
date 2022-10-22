import math
def invalidinput(str):
    numnum = int(input(str))
    while numnum != range(0, 101):
        if numnum < 0:
            print('Your input must a valid number, it can not be less than 0')
            numnum = int(input(str))
        else:
            break
    return numnum
def grademenu():
    print(f'{"Grade Menu":>22}')
    print('1 - Add Test')
    print('2 - Remove Test')
    print('3 - Clear Tests')
    print('4 - Add Assignment')
    print('5 - Remove Assignment')
    print('6 - Clear Assignments')
    print('D - Display Scores')
    print('Q - Quit')
def mean(lst):
    try:
        sumvalues = sum(lst)
        numvalues = len(lst)
        avg = sumvalues/numvalue
        avg = round(avg, 2)
        return avg
    except ZeroDivisionError:
        avg = 0
        return avg
def std(lst, avg):
    u = 0
    for n in lst:
        numerator = (n - avg) ** 2
        u += numerator
    insqrt = u / (len(lst))
    std = math.sqrt(insqrt)
    std = round(std, 2)
    return std
def notavailable(sixty, forty):
    if sixty == []:
        print(f'{"Tests":<19}{"0":<8}{"n/a":<8}{"n/a":<8}{"n/a":<8}{"n/a":<8}')
    else:
        print(f'{"Tests":<19}{len(sixty):<8}{min(sixty):<8}{max(sixty):<8}{mean(sixty):<8}{std(sixty, mean(sixty)):<8}')
    if forty == []:
        print(f'{"Programs":<19}{"0":<8}{"n/a":<8}{"n/a":<8}{"n/a":<8}{"n/a":<8}')
    else:
        print(f'{"Programs":<19}{len(forty):<8}{min(forty):<8}{max(forty):<8}{mean(forty):<8}{std(forty, mean(forty)):<8}') 
def scores(sixty, forty):
    print(f'{"Type":<19}{"#":<8}{"min":<8}{"max":<8}{"avg":<8}{"std":<8}')
    print('=' * 54)
    notavailable(tests, assignments)
grademenu()
print()
tests = []
assignments = []
gminput = input('==> ')
print()
while gminput != 'Q':
    if gminput == '1':
        addtest = invalidinput('Enter the new Test score 0-100 ==> ')
        tests.append(addtest)
        print()
        grademenu()
        print()
        gminput = input('==> ')
    elif gminput == '2':
        try:
            removetest = invalidinput('Enter the Test to remove 0-100 ==> ')
            tests.remove(removetest)
            print()
            grademenu()
            print()
            gminput = input('==> ')
        except:
            print('Could not find that score to remove')
            grademenu()
            print()
            gminput = input('==> ')
    elif gminput == '3':
        tests.clear()
        print()
        grademenu()
        print()
        gminput = input('==> ')
    elif gminput == '4':
        addassignment = invalidinput('Enter the new Assignment score 0-100 ==> ')
        assignments.append(addassignment)
        print()
        grademenu()
        print()
        gminput = input('==> ')
    elif gminput == '5':
        try:
            removeassignment = invalidinput('Enter the Assignment to remove 0-100 ==> ')
            tests.remove(removeassignment)
            print(assignments)
            grademenu()
            print()
            gminput = input('==> ')
        except:
            print('Could not find that score to remove')
            grademenu()
            print()
            gminput = input('==> ')
    elif gminput == '6':
        assignments.clear()
        print()
        grademenu()
        print()
        gminput = input('==> ')
    elif gminput == 'D':
        scores(tests, assignments)
        print()
        weightedscore = (mean(tests) * 0.6) + (mean(assignments) * 0.4)
        print('The weighted score is       ', weightedscore)
        print()
        grademenu()
        print()
        gminput = input('==> ')
    else:
        break
    
