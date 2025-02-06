import random
num = random.randint(1, 20)
trials = 0
print ("Hello! What is your name?")
a=input()
print ("Well" , a , "I am thinking of a number between 1 and 20. \nTake a guess.")
while True:
    userinput = int(input())
    trials += 1
    if userinput > num:
        print("Your guess is too high")
    elif userinput < num:
        print ("Your guess is too low")
    else:
        print ("Good job," , a , "! You guessed my number in" , trials , "guesses!")
        break