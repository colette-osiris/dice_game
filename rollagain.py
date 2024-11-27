##roll again function 

##imports
import random 

###variables needed to preform tests 
'''
##dice variables 
dice_1 = [1,2,3,4,5,6]
dice_2 = [1,2,3,4,5,6]
dice_3 = [1,2,3,4,5,6]

##dice rolls variables 
dice_1_roll = random.choices(dice_1, k=1)
#print(dice_1_roll)
dice_2_roll = random.choices(dice_2, k=1)
dice_3_roll = random.choices(dice_3, k=1)
'''

def roll_again(roll_1, roll_2=None, roll_3=None):
    "function that rolls dice, given up to 3 dice, and returns random roll values."
    scores = []
    roll_score_1 = random.choices([1,2,3,4,5], k=1)
    roll_score_1 = int(roll_score_1[0])
    print(f"you rolled a {roll_score_1} on dice 1")
    scores.append(roll_score_1)
    #print(scores)
    if roll_2 != None:
        roll_score_2 = random.choices([1,2,3,4,5], k=1)
        roll_score_2 = int(roll_score_2[0])
        print(f"you rolled a {roll_score_2}  on dice 2")
        scores.append(roll_score_2)
        #print(scores)
    if roll_3 != None:
        roll_score_3 = random.choices([1,2,3,4,5], k=1)
        roll_score_3 = int(roll_score_3[0])
        print(f"you rolled a {roll_score_3}  on dice 3")
        scores.append(roll_score_3)
        #print(scores)
    return scores


###tests

'''
results = roll_again(dice_1_roll)
print(results)

results = roll_again(dice_1_roll, dice_2_roll)
print(results)

results = roll_again(dice_1_roll, dice_2_roll, dice_3_roll)
print(results)

'''
