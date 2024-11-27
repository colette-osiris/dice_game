#README FILE FOR DICE GAME PROGRAM ANS UTILITIES 


Program Version 1.0 11/26/2024

USAGE NOTES 
#######

    This program allows users to play the 'Tupled Out Dice Game'. The object of the game is to score the most points by rolling the dice. Each player will have 5 turns, with 3 optional re-rolls each term. Each turn, the player will attempt to roll the highest score without 'tupling out', which means rolling the same number on each dice. 

PROCESS WALK THROUGH NOTES
#######
    When you start the program, it greets the user with a short description of the function of the program and provides a brief overview of the rules of the game. It then notifies the user that round one is starting and their current total points is equal to zero. 

    For Round One:

        It then automatically rolls all three dice and shows the values of the rolls. 
        
        If all three rolls are equal, the user has 'tupled out.' In this case, the round is automatically over and the user recieves a score of 0. 

        If two dice roll the same value, they are considered 'frozen' and cannot be rolled again this round. The program will announce this, along with the user's round points should they choose to keep this roll as their final one for the round. The program then asks the user to choose whether they would like roll the last dice again by typing 'y' or 'n', for yes or no, respectively. 

            If they chose neither, or failed to type 'y' or 'n', the program will alert them to this and offer an oppertunity to try again until either 'y' or 'n' is typed. 

            If they chose 'y' the program will immediately roll the dice and report the score again, before repeating the re-roll question. The user has up to three re-rolls per round. If they choose to reroll a third time, the program will use that as their round points score and end the round, regardless of if the user scored better previously. 

            If they chose 'n', the program will immediately end the round, reporting the round points and total points before proceeding to the next round.


        If all three dice rolls are different, the program will announce this, along with the user's round points should they choose to keep this roll as their final one for the round. The program then asks the user to choose whether they would like roll all three dice again by typing 'y' or 'n', for yes or no, respectively. 

            If they chose neither, or failed to type 'y' or 'n', the program will alert them to this and offer an oppertunity to try again until either 'y' or 'n' is typed. 

            If they chose 'y' the program will immediately roll the dice and report their scores again, before repeating the re-roll question. The user has up to three re-rolls per round. If they choose to reroll a third time, the program will use that as their round points score and end the round, regardless of if the user scored better previously. 

            If they chose 'n', the program will immediately end the round, reporting the round points and total points before proceeding to the next round.

            Please note that is this version of the game, if user decides to reroll all three dice, in the event that two dice have equal values, the program will not "freeze" them. Rather, the user will have the option to re-roll all or none of the dice. 


INSTALLATION NOTES
####### 

 - make sure you have the lastest versions of Python, Homebrew, and Conda, and Git installed 
 - make sure rollagain.py is downloaded and located in the same folder as .py file 
 - make sure the file or directory you would like to preform count on is downloaded and located in the same folder as .py and rollagain.py files 


FUNCTION PARAMETERS NOTES
####### 

 (1) roll_again function:

    Arguments: roll_1, roll_2, roll_3
        - The variable 'roll_1':
            - integer
            -  represents whether the roll value of dice 1
         - The variable 'roll_2':
            - integer
            - optional
            -  represents whether the roll value of dice 2
         - The variable 'roll_3':
            - integer
             - optional
            -  represents whether the roll value of dice 3

    Returns: scores 
        - The variable 'scores':
            - a list
            - represents the re-rolled values of 1-3 dice depending on optional arguments 


WHY THIS IS HELPFUL NOTES
####### 

This README is helpful because it can:

    - help users troubleshoot initial errors regarding initial set up 
    - explain the purpose and design of functions used 
    - provides support for usage-based questions and errors 

For example, if you were to copy the program .py file without also copying the function .py file (rollagain.py), the program would produce an "Import not Found" error. Without the README file, the user may not know how to proceed, but with it included, the User can reference the file for this potential error, ensure both files are in the same directory, and proceed without error. 

Another example could be if you were unclear about the parameters of the roll_again function. Since this function returns a list, the user may need a bit of clarification beyond the docstring, or otherwise risk incorrectly setting parameters. If the user were to check this README file, they would find that function parameter notes section may clear up any confusion between sensitivity and upper variables. 

Another example could be if you were confused about the difference between 'roll_1' and 'scores' variables of open_file_or_directory function, you could use the README.md document to get clarification on the difference by consulting the function parameter notes. 