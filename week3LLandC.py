game = True
while game:
    print('Welcome to the Flarsheim Guesser!\n')
    userNumber = int(input('Please think of a number between and including 1 and 100.\n'))
    rem3 = int(input('What is the remainder when your number is divided by 3 ?'))
    while rem3 != range(4):
        if rem3 < 0:
            print('The value entered must be 0 or greater')
            rem3 = int(input('What is the remainder when your number is divided by 3 ?'))
        elif rem3 >= 3:
            print('The value entered must be less than 3')
            rem3 = int(input('What is the remainder when your number is divided by 3 ?'))
        else:
            userNumber3 = userNumber / 3
            print()
            break
    rem5 = int(input('What is the remainder when your number is divided by 5 ?'))
    while rem5 != range(5):
        if rem5 < 0:
            print('The value entered must be 0 or greater')
        elif rem5 >= 5:
            print('The value entered must be less than 5')
        else:
            userNumber5 = userNumber / 5
            print()
            break
    rem7 = int(input('What is the remainder when your number is divided by 7 ?'))
    while rem7 != range(6):
        if rem7 < 0:
            print('The value entered must be 0 or greater')
        elif rem7 >= 7:
            print('The value entered must be less than 5')
        else:
            userNumber7 = userNumber / 7
            print()
            break
    flarsheimNumber = ((round(userNumber3) * 3) + rem3) or ((round(userNumber5) * 5) + rem5) or ((round(userNumber7) * 7) + rem7)
    print('Your number was ', flarsheimNumber)
    print('How amazing is that?')
    escape = input('Do you want to play again? Y to continue, N to quit  ==>')
    while escape in range('Y', 'y', 'N', 'n'):
        if escape != 'Y' or num != 'y':
            escape = input('Do you want to play again? Y to continue, N to quit  ==>')
        elif escape != 'N' or num != 'n':
            escape = input('Do you want to play again? Y to continue, N to quit  ==>')
        else:
            game = False
