import random
print('''
_____   _______ ___   _____  _____  _______ _   ____ 
|  _\| \| __\ _\| _\  |_ _\|_|\ __\ |  _\  \|\/\| __\
| [ \|_|\  ][__ [__ \   ||| _ |  ]_ | [ \ . \   \  ]_
|___/___/___/___/___/   |/|/ |/___/ |___//\_//v\/___/                                     ''')
print("Welcome to")
print("Guess the Number Game")

computerGeneratedRandomNumber=random.randint(1,100)
print(computerGeneratedRandomNumber)

difficulty=input("Please Enter the difficulty level easy or hard\n")
attempt=0
if difficulty=="easy":
    attempt=8
elif difficulty=="hard":
    attempt=5
else:
    attempt=0

for i in range(1,attempt+1):
    usernumber=int(input("what's your number?\n"))
    if usernumber>computerGeneratedRandomNumber:
        print("should be less than the guessed Number")
    elif usernumber<computerGeneratedRandomNumber:
        print("litte higher")
    attempt-=1
    print(f"you have only {attempt} attempt left")
    if(attempt<1):
        print("You lose!")
        break
    elif usernumber==computerGeneratedRandomNumber:
        print("you win")
        break
    