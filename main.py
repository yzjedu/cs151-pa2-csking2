# # Programmers: Cody
# # Course: CS151, Professor Zee
# # Due Date: October 23rd 2024
# # Lab Assignment: PA2
# # Problem Statement:

# import random
import random

#initialize variables
p1_count = 0
p2_count = 0
computer_count = 0
p1 = 0
p2 = 0
computer = 0
amount_of_sticks = 0

#ask user if they want to play the game
decision = input('Do you want to play the game? Enter Yes or No: ')
decision = decision.lower()

#if user wants to play the game
while decision == 'yes':
    amount_of_sticks = input('Choose number of sticks, 10-100: ')
    amount_of_sticks = int(amount_of_sticks)
    if amount_of_sticks >= 10 and amount_of_sticks <= 100:
        print('\nP1 Losses:', p1_count,  '\nP2 Losses: ', p2_count, '\nComputer Losses:', computer_count)


        while amount_of_sticks > 0:

            p1 = input('\nPlayer 1, How many sticks do you want to pick up, 1, 2, or 3? ')
            p1 = int(p1)

            if p1 == 1 or p1 == 2 or p1 == 3:
                amount_of_sticks = amount_of_sticks - p1
                print('Sticks Left: ', amount_of_sticks)

                if amount_of_sticks <= 0:
                    print("\nGAME OVER, Player 1 Loses")
                    p1_count += 1
                    print('P1 Losses:', p1_count,  '\nP2 Losses: ', p2_count, '\nComputer Losses:', computer_count)

                elif amount_of_sticks > 0:
                    p2 = input('\nPlayer 2, How many sticks do you want to pick up, 1, 2, or 3? ')
                    p2 = int(p2)

                    if p2 == 1 or p2 == 2 or p2 == 3:
                        amount_of_sticks = amount_of_sticks - p2
                        print('Sticks Left: ', amount_of_sticks)


                        if amount_of_sticks <= 0:

                            print("\nGAME OVER, Player 2 Loses")
                            p2_count += 1
                            print('P1 Losses:', p1_count,  '\nP2 Losses: ', p2_count, '\nComputer Losses:', computer_count)

                        elif amount_of_sticks > 0:
                            computer = random.randint(1, 3)
                            computer = int(computer)

                            print('\nComputer Selected: ', computer)

                            amount_of_sticks = amount_of_sticks - computer

                            print('Sticks Left: ', amount_of_sticks)

                            if amount_of_sticks <= 0:

                                print("\nGAME OVER, Computer Loses")
                                computer_count += 1
                                print('P1 Losses:', p1_count, '\nP2 Losses: ', p2_count, '\nComputer Losses:', computer_count)

                    else:
                        print("\nPick a valid number")

                else:
                    print("\nPick a valid number")

            else:
                print("\nPick a valid number")

        decision = input('\nDo you want to play the game? Enter Yes or No: ')
        decision = decision.lower()

    else:
        print('Error, Try again. ')

#if user does not want to play the game
if decision == 'no':
    print('\nNo Game Played')
    print('\nTOTAL LOSSES:\nP1 Losses:', p1_count,  '\nP2 Losses: ', p2_count, '\nComputer Losses:', computer_count)

#if user doesn't choose yes or no
else:
    print('Please select Yes or No')