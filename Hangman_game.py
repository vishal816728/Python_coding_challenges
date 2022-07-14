import random

wordlist=["bootcamp","houselab","course","webflex"]

display=[]

randomword=wordlist[random.randint(0,len(wordlist)-1)]

for i in range(0,len(randomword)):
    display.append("_")
print(randomword)    
print(display)    

end_of_game=False
life=6

while not end_of_game:
  
    guess=input("guess a letter\n").lower()
    
    for i in range(len(randomword)):
        
        letter=randomword[i]
        if letter==guess:
            display[i]=letter
    if guess not in randomword:
        life=life-1
        if life==0:
           end_of_game=True
           print("You are not able to save the man")
    print(life)    
    print(display)
    if "_" not in display:
        end_of_game=True
        print("You save the Man")
    
        