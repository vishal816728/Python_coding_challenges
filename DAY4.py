import random

# li=input("Give the names of your friends\n")
# l=li.split(",")
# n=random.randint(0,len(l)-1)
# payer=l[n]
# print(f"{payer} is going to pay the bill")

# row1=[1,2,3]
# row2=[4,5,6]
# row3=[7,8,9]
# newrow=[row1,row2,row3]
# # print(newrow)
# # print(f"{row1}\n{row2}\n{row3}")
# c=(input("where do you want to put treasure\n"))
# c1=int(c[0])-1
# c2=int(c[1])-1

# newrow[c1][c2]="x"
# print(newrow)




# Rock paper scissors game

l=["paper","rock","scissors"]
print("welcome to rock paper scissors game")
you=input("Enter your choice it must to rock,paper or scissors\n")
you=you.lower()
if(you=="rock"):
    print('''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
''')
elif you=="paper":
    print('''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
''')
elif you=="scissors":
    print( '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''  )
else:
    print("wrong input")
    
print("computers turn")
com=l[random.randint(0,2)]
print(com)
if(com=="rock"):
    print('''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
''')
elif com=="paper":
    print('''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
''')
elif com=="scissors":
    print( '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''  )
   # paper>rock 
# scissor>paper
# rock>scissors 

if you==com:
    print("game is tie. try again")
elif you=="rock" and com=="scissors":
    print("you wins")
elif you=="paper" and com=="rock":
    print("you wins")
elif you=="scissors" and com=="paper":
    print("you wins")
else:
    print("computer wins")









