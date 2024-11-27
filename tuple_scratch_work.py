##tuple scratch work 


###tuple out dice game 

##imports
import random 
import rollagain 

##game opening 
print("Hello! Welcome to the Tuple Out Dice Game! \n The object of the game is to score more points than your opponent by taking turns rolling the dice. Each player will have 5 turns, with 3 optional re-rolls each term.\n" )# Each turn, the player will attempt to roll the highest score without 'tupling' out. ")

##number of players 
#num_players = input("How many players would like to play?")

##dice variables 
dice_1 = [1,2,3,4,5,6]
dice_2 = [1,2,3,4,5,6]
dice_3 = [1,2,3,4,5,6]

##scoring variables 
round_points = 0
total_points = 0
total_points = total_points + round_points 

##flag variables 
game_round = 1
time_roll = 0

 ##scoring system outline 
while game_round <= 5:
    print(f"Round {game_round} starting now! Your total points = {total_points}")
    results = rollagain.roll_again(dice_1, dice_2, dice_3)
    print(results)
    #game_round += 1


    for index in results: 
        if len(results) <= 3:
            extracted_roll_1 = results[0]
            #print(type(extracted_roll_1))
            #print(f"extracted_roll_1 = {extracted_roll_1}")
            extracted_roll_2 = results[1]
            #print(type(extracted_roll_2))
            #print(f"extracted_roll_2 = {extracted_roll_2}")
            extracted_roll_3 = results[2]
            #print(type(extracted_roll_3))
            #print(f"extracted_roll_3 = {extracted_roll_3}")
        else:
            print("something is wrong")


    if extracted_roll_1 == extracted_roll_2 == extracted_roll_3: 
        round_points = 0
        print(f"Uh oh! You have tupled out! All of your dice rolled {extracted_roll_1}. You score {round_points} points this round. Your total points is now {total_points}. ")
    #else:
        #round_points = extracted_roll_1  + extracted_roll_2  + extracted_roll_3 
        #print(f"Your points this round = {round_points}")
        
    elif (extracted_roll_1  == extracted_roll_2) or (extracted_roll_1 == extracted_roll_3) or (extracted_roll_3 == extracted_roll_2):
        #print(f"dice roll one = {extracted_roll_1} \n dice roll two = {extracted_roll_2} \n dice roll three = {extracted_roll_3}")
        round_points = extracted_roll_1  + extracted_roll_2  + extracted_roll_3 
        #round_points = sum(round_points)
        #round_points = int(round_points)
        print(f"two of your dice rolled the same number. They are now fixed and cannot be rolled again. Your current round points = {round_points}.") # and your total points is now {total_points}.")
        time_roll = 1
        while time_roll <=3:
            roll_again = input("Would you like to risk it and roll your last dice again? type 'y' for yes or 'n' for no.")

            if roll_again == 'n':
                #total_points = total_points + round_points 
                print(f"You have decided to not roll again. Your points this round = {round_points}.") # and your total points = {total_points}")
                time_roll = 4

            elif roll_again == 'y':
                    print(f"You have chosen to roll again.")
                    if (extracted_roll_1 == extracted_roll_2):
                        results = rollagain.roll_again(extracted_roll_3, None, None)
                        for index in results: 
                            new_roll_3 = results[0]
                            print(f"new_roll_3 = {new_roll_3}")
                        round_points = extracted_roll_1 + extracted_roll_2 + new_roll_3
                        #print(type(round_points))
                        #print(type(results))
                        #round_points = sum(round_points)
                        print(f"dice three rolled a {results}. Your round points now = {round_points}.")

                    elif(extracted_roll_1 == extracted_roll_3):
                        results = rollagain.roll_again(extracted_roll_2)
                        for index in results: 
                            new_roll_2 = results[0]
                            print(f"new_roll_2 = {new_roll_2}")
                        round_points = extracted_roll_1 + new_roll_2 + extracted_roll_3
                        #round_points = int(round_points)
                        #round_points = sum(round_points)
                        print(f"dice two rolled a {new_roll_2}. Your round points now = {round_points}.")

                    elif(extracted_roll_3 == extracted_roll_2):
                        results = rollagain.roll_again(extracted_roll_1)
                        for index in results: 
                            new_roll_1 = results[0]
                            print(f"new_roll_1 = {new_roll_1}")
                        round_points = new_roll_1 + extracted_roll_2 + extracted_roll_3
                        #round_points = sum(round_points)
                        print(f"dice one rolled a {new_roll_1}. Your round points now = {round_points}.")
                    else:
                        print("error")
            time_roll += 1
    elif (extracted_roll_1 != extracted_roll_2) and (extracted_roll_1 != extracted_roll_3) and (extracted_roll_3 != extracted_roll_2):
        #print(f"dice roll one = {dice_1_roll} \n dice roll two = {dice_2_roll} \n dice roll three = {dice_3_roll}")
        round_points = extracted_roll_1 + extracted_roll_2 + extracted_roll_3
        #round_points = int(round_points)
        print(f"All of your dice rolled different numbers. Your current round points = {round_points}.") 
        time_roll = 1
        while time_roll <= 3:
            roll_3_again = input("Would you like to risk it and roll all three dice again? type 'y' for yes or 'n' for no.")
            if roll_3_again == 'n': 
                #total_points = total_points + round_points 
                print(f"You have decided to not roll again. Your points this round = {round_points}.") # and your total points = {total_points}")  
                time_roll = 4
            elif roll_3_again == 'y':
                results = rollagain.roll_again(extracted_roll_1, extracted_roll_2, extracted_roll_3)
                for index in results: 
                    if len(results) <= 3:
                        extracted_roll_1 = results[0]
                        #print(type(extracted_roll_1))
                        #print(f"extracted_roll_1 = {extracted_roll_1}")
                        extracted_roll_2 = results[1]
                        #print(type(extracted_roll_2))
                        #print(f"extracted_roll_2 = {extracted_roll_2}")
                        extracted_roll_3 = results[2]
                        #print(type(extracted_roll_3))
                        #print(f"extracted_roll_3 = {extracted_roll_3}")
                    else:
                        print("something is wrong")
                if (extracted_roll_1  == extracted_roll_2) or (extracted_roll_1 == extracted_roll_3) or (extracted_roll_3 == extracted_roll_2):
                #print(f"dice roll one = {extracted_roll_1} \n dice roll two = {extracted_roll_2} \n dice roll three = {extracted_roll_3}")
                    round_points = extracted_roll_1  + extracted_roll_2  + extracted_roll_3 
                    # round_points = sum(round_points)
                    #round_points = int(round_points)
        print(f"two of your dice rolled the same number. They are now fixed and cannot be rolled again. Your current round points = {round_points}.") # and your total points is now {total_points}.")
        time_roll = 1
        while time_roll <=3:
            roll_again = input("Would you like to risk it and roll your last dice again? type 'y' for yes or 'n' for no.")

            if roll_again == 'n':
                #total_points = total_points + round_points 
                print(f"You have decided to not roll again. Your points this round = {round_points}.") # and your total points = {total_points}")
                time_roll = 4

            elif roll_again == 'y':
                    print(f"You have chosen to roll again.")
                    if (extracted_roll_1 == extracted_roll_2):
                        results = rollagain.roll_again(extracted_roll_3, None, None)
                        for index in results: 
                            new_roll_3 = results[0]
                            print(f"new_roll_3 = {new_roll_3}")
                        round_points = extracted_roll_1 + extracted_roll_2 + new_roll_3
                        #print(type(round_points))
                        #print(type(results))
                        #round_points = sum(round_points)
                        print(f"dice three rolled a {results}. Your round points now = {round_points}.")

                    elif(extracted_roll_1 == extracted_roll_3):
                        results = rollagain.roll_again(extracted_roll_2)
                        for index in results: 
                            new_roll_2 = results[0]
                            print(f"new_roll_2 = {new_roll_2}")
                        round_points = extracted_roll_1 + new_roll_2 + extracted_roll_3
                        #round_points = int(round_points)
                        #round_points = sum(round_points)
                        print(f"dice two rolled a {new_roll_2}. Your round points now = {round_points}.")

                    elif(extracted_roll_3 == extracted_roll_2):
                        results = rollagain.roll_again(extracted_roll_1)
                        for index in results: 
                            new_roll_1 = results[0]
                            print(f"new_roll_1 = {new_roll_1}")
                        round_points = new_roll_1 + extracted_roll_2 + extracted_roll_3
                        #round_points = sum(round_points)
                        print(f"dice one rolled a {new_roll_1}. Your round points now = {round_points}.")
                    else:
                        print("error")
                    round_points = extracted_roll_1  + extracted_roll_2  + extracted_roll_3 
                    #total_points = total_points + round_points
                    print(f"Your points this round = {round_points}") #and your total points = {total_points}") 
            time_roll += 1 
    total_points = total_points + round_points 
    print(f"Your points this round = {round_points}, and your total points = {total_points}.")
    game_round += 1

                
'''
try dice = 3:

except: 

'''




