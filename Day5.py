students_height=input("Enter the height\n")
students_height=students_height.split(",")
print(students_height)
sum=0
for student in students_height:
    sum+=int(student)
average=sum/len(students_height)    
print(average)

# // important we can use sum shortcut provided by python
# // or max for finding the max

# ***********************************************************
score=input("enter the score\n")
score=score.split(" ")
max=0
for s in score:
    if(int(s)>max):
        max=int(s)
print(max)    

# ***********************************************************
sum=0
for i in range(1,201,2): # 2 is just showing the step size 
    print(i)
    sum+=i
print(sum)    


# ************************************************************
sum=0
for i in range(1,101): # 2 is just showing the step size 
    if(i%2==0):
        sum+=i
print(sum)


# // *****************************************
#  Fizz Buzz

for i in range(1,101):
    if (i%3==0 and i%5==0):
        print("fizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
    
    
    
    
    
# *********************************************************

# Random password generator
import random
l=int(input("length of your password\n"))
s=int(input("how many symbols you want \n"))
n=int(input("how many numbers you want \n"))
r='A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'
r=r.split(',')
sym=['%','$','@','*']
number=['0','1','2','3','4','5','6','7','8','9']
passw=""
for i in range(1,l+1):
    random_choice=random.choice(r)
    passw+=random_choice

for i in range(1,s+1):
    random_choice=random.choice(sym)
    passw+=random_choice
for i in range(1,n+1):
    random_choice=random.choice(number)
    passw+=random_choice    

print(passw)


    
    
    

#*****************************************************
import random
l=int(input("length of your password\n"))
s=int(input("how many symbols you want \n"))
n=int(input("how many numbers you want \n"))
r='A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'
r=r.split(',')
sym=['%','$','@','*']
number=['0','1','2','3','4','5','6','7','8','9']
passw=[]
for i in range(1,l+1):
    random_choice=random.choice(r)
    passw.append(random_choice)

for i in range(1,s+1):
    random_choice=random.choice(sym)
    passw.append(random_choice)
for i in range(1,n+1):
    random_choice=random.choice(number)
    passw.append(random_choice)
rand=random.shuffle(passw)
passw=''.join(passw)
print(passw)
   