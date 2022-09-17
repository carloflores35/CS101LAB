print('Welcome to the Flarsheim Guesser!\n') # Start with the introduction
game = True 
while game: # Establish a big while loop that allows for the game to be played again
    print('Please think of a number between and including 1 and 100.\n') # Ask for their number without saving it to suprise them by figuring it out using remainders
    rem3 = int(input('What is the remainder when your number is divided by 3 ?')) # Asking for remainder when dividing by 3
    while rem3 != range(4): # Keeps remainder in the proper range the remainder can be
        if rem3 < 0: # Restarts if remainder input is less than 1
            print('The value entered must be 0 or greater')
            rem3 = int(input('What is the remainder when your number is divided by 3 ?'))
        elif rem3 >= 3: # Restarts if remainder input is more than or equal to 3
            print('The value entered must be less than 3')
            rem3 = int(input('What is the remainder when your number is divided by 3 ?'))
        else:
            print()
            break # Continues to find next remainder
    rem5 = int(input('What is the remainder when your number is divided by 5 ?')) # Asking for remainder when dividing by 7
    while rem5 != range(5): # Keeps remainder in the proper range the remainder can be
        if rem5 < 0: # Restarts if remainder input is less than 1
            print('The value entered must be 0 or greater')
            rem5 = int(input('What is the remainder when your number is divided by 5 ?'))
        elif rem5 >= 5: # Restarts if remainder input is more than or equal to 5
            print('The value entered must be less than 5')
            rem5 = int(input('What is the remainder when your number is divided by 5 ?'))
        else:
            print()
            break # Continues to find next remainder
    rem7 = int(input('What is the remainder when your number is divided by 7 ?')) # Asking for remainder when dividing by 7
    while rem7 != range(6): # Keeps remainder in the proper range the remainder can be
        if rem7 < 0: # Restarts if remainder input is less than 1
            print('The value entered must be 0 or greater')
            rem7 = int(input('What is the remainder when your number is divided by 7 ?'))
        elif rem7 >= 7: # Restarts if remainder input is more than or equal to 7
            print('The value entered must be less than 5')
            rem7 = int(input('What is the remainder when your number is divided by 7 ?'))
        else:
            print()
            break # Continues to find next remainder
    flarsheimNumber = -1 # Establish temporary value for the number that Flarsheim is guessing
    for seq3 in range(0 + rem3, 101, 3): # Stating that a variable is in a certain range starting with the remainder while incrementing by 3, this pinpoints the possibilities the number can be
        far5 = ((seq3 - rem5) / 5).is_integer() # Narrowing down
        far7 = ((seq3 - rem7) / 7).is_integer() # Narrowing down more
        if far5 and far7: # If they all match, (look down)
            flarsheimNumber = seq3
            print(flarsheimNumber) # Then print the number since they all meet the conditions
            break
    print('Your number was ', flarsheimNumber)
    print('How amazing is that?')
    escape = input('Do you want to play again? Y to continue, N to quit  ==>') # Initialize whether or not user is done playing
    while escape not in ['Y', 'y', 'N', 'n']: # Checks whether the input is valid or not
        escape = input('Do you want to play again? Y to continue, N to quit  ==>')
    if escape == 'Y' or escape == 'y': # Repeats the game
        game = True
        print()
    elif escape == 'N' or escape == 'n': # Ends the game
        game = False
    else:
        print()

