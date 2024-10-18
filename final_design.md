# Final Design Document

1. Import Random Module
2. Initialize variables
    1. p1_count = 0
   2. p2_count = 0
   3. computer_count = 0
   4. p1 = 0
   5. p2 = 0
   6. computer = 0
   7. amount_of_sticks = 0

3. Ask the user if they want to play the game, store in decsion


 #   4. While decision == "yes"
    1. output amount of losses from each player to user
        2. set amount_of_sticks to 0

    2. While amount_of_sticks > 0
        I. ask player 1 to enter how many sticks they want, store in p1
        
        II. if p1 is 1, 2 or 3
            a.subtract p1 from amount_of_sticks, store back in amount_of_sticks
            
            b. output sticks left to the user
            
            c. if amount_of_sticks <= 0
                i. ouput game over to user, player 1 loses
                ii. += 1 to p1_count
                iii. ouput to user total losses
            
            d. otherwise if amount_of_sticks > 0
                i. ask player 2 to enter how many sticks they want, store in p2
                ii. subtract p2 from amount_of_sticks
                iii. output sticks left to user
                iv. if amount of sticks <= 0
                    a. output to user game over, player 2 loses
                    
                    b.  += 1 to p2_count
        
                    c. output to user total losses

                v. otherwise if amount_of_sticks > 0
                    a. computer selects random integer, 1, 2, or 3, store under computer

                    b. print the computer selected number

                    c. subtract computer from amount_of_sticks

                    d. output to user sticks left
                    
                    e. if amount_of_sticks <= 0
                        i. output game over, computer loses
                    
                        ii. += 1 to computer_count

                        iii. output to user total loses

                vi. otherwise
                    output to user to pick a valid number
            
            e. otherwise
                output to user to pick a valid number
        
        III. otherwise
            output to user to pick a valid number
     
    3. ask user to input if they want to play the game again

4. if decision == "no"
    1. output that no game is played
    2. output total losses to the user

5. otherwise
    1. ask user to select yes or no
   