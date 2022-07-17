# *************************cipher***************************

direction=input("Do you want to encode the word or decode the word\n")

word=input("enter the word here\n")
wordlist=list(word)
newwordlist=[]
shift=int(input("enter the shift here\n"))

ciphervalue=""

if direction=="encode":
     for i in wordlist:
         newwordlist.append(chr(ord(i)+shift))
     print("Your encoded value is "+''.join(newwordlist))         
elif direction=="decode":
    for i in wordlist:
        newwordlist.append(chr(ord(i)-shift))
    print("Your decoded value is "+''.join(newwordlist))      
else:
    print("only two options are allowed")