# Initial Design Document
#### PLEASE! PLEASE! PLEASE! READ the [README.md](README.md) File carefully

# 1. Prompt user to select how many sticks needed to play 10-100, store under stick
# 2. While decision == "Yes"
    i. Ask user if they want to play the game, decision, "Yes", "No"
    ii. if user selects "Yes"
#       3. While stick != 0
            i. Display to users how many wins each player has
            ii. Prompt player 1 to select how many sticks they want to pick up (1,2, or 3), store under p1
                if p1 == 1 or == 2 or ==3
                    a. subtract p1 from stick
                    b. if stick == 0
                        i. stop game
                        ii. add 1 to p2 count and c_choice count
                    c.otherwise
                        i. Prompt player 2 to select how many sticks they want to pick up (1,2, or 3), store under p2
                            if p2 == 1 or == 2 or == 3
                                a. subtrack p2 from stick
                                b. if stick == 0
                                i. stop game
                                ii. add 1 to p1 count and c_choice count
                                    otherwise
                                i. have computer select random number, store under c_choice
                                ii. subtract c_choice from stick
                                iii. if stick == 0
                                iv. stop game
                                v. add 1 to p1 count and p2 count
                            otherwise 
                                output to user to select a valid value
                otherwise
                    output to user to select a valid value
                    
    iii. otherwise
        end the game, display the number of times each player loses

    