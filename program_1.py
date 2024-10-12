
# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).  
# The dice sum will be the output of this function.
import random

def randDice():
    num1 = random.randint(1,6)      #generates 2 random numbers
    num2 = random.randint(1,6)
    total = num1 + num2
    return total

def number_average():
    total_sum = 0
    for l in range(100):
        total_sum += randDice()
    average = total_sum/100



    print(f'The average number in 100 rolls is {average:.2f}')


number_average()

#########
# Then write a mainline that calls the "randDice" function 100 times in a for loop.  
# The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.