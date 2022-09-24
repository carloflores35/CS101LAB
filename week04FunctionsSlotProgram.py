########################################################################
##
## CS 101 Lab
## Program #4
## Carlo Flores
## cafg2t@umsystem.edu
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

#import modules needed
import random
# This function allows the program to repeat or end
def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    temp_value = 'N' # A temporary value so we can change it in the while loop
    while temp_value in ('Y', 'YES', 'N', 'NO'):
        userAnswer = input('Do you want to play again? ==>')
        userAnswer = userAnswer.upper()
        if userAnswer == 'Y' or userAnswer == 'YES':
            return True
        elif userAnswer == 'N' or userAnswer == 'NO':
            return False
        else:
            print()
            print('You must enter Y/YES/N/NO to continue. Please try again')

def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    wager = int(input('How many chips do you want to wager? ==>'))
    while wager != range(1, bank):
        if wager < 0: # Covers if the wager is negative or 0
            print('The wager amount must be greater than 0.  Please enter again. ')
            wager = int(input('How many chips do you want to wager? ==>'))
        elif wager > bank: #Covers if the wager exceeds the amount in their bank
            print('The wager amount cannot be greater than how much you have. ', bank)
            wager = int(input('How many chips do you want to wager? ==>'))
        else:
            break
    return wager       
# This function uses the import module random to get a number in the range 1 to 10 for our slot machine
def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    one = random.randint(1,10)
    two = random.randint(1,10)
    three = random.randint(1,10)
    return one, two, three

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if reela == reelb and reela == reelc and reelb == reelc:
        return 3
    elif reela == reelb or reela == reelc or reelb == reelc:
        return 2
    else:
        return 0
# Function establishes how much we start out with 
def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    bank = int(input('How many chips do you want to start with ==>'))
    total_bank = bank
    while bank != range(1, 101):
        if bank < 0:
            print('Too low a value, you can only choose 1 - 100 chips')
            bank = int(input('How many do you want to start with ==>'))
        elif bank >= 101:
            print('Too high a value, you can only choose 1 - 100 chips')
            bank = int(input('How many do you want to start with ==>'))
        else:
            return bank

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 3:
        return (wager * 10) - wager
    elif matches == 2:
        return (wager * 3) - wager
    else:    
        return wager * -1

if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()
        spin = 0
        total_bank = bank
        
        while bank != 0:  # Prints payout and results as long as they don't run out of money
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
            spin += 1
            totalPayout = abs(payout * spin)
        # A conclusion-like statement, as it reads out final results and also asks the play_again() function to see how the user wants to continue
        print("You lost all", total_bank, "in", spin, "spins")
        print("The most chips you had was", totalPayout)
        playing = play_again()
