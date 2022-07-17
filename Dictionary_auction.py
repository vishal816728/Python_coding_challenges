# dic={
#     "harry":81,
#     "rohan":90,
#     "lakh":73,
#     "vijay":89,
#     "duresh":68,
#     "sunil":54
# }
# newdic=dic
# print(newdic)
# for i in dic:
#     if dic[i]>=90:
#         dic[i]="outstanding"
#     elif dic[i]>80:
#         dic[i]="excellent"
#     elif dic[i]>70:
#         dic[i]="good"
#     elif dic[i]>60:
#         dic[i]="can be good"
#     elif dic[i]<60:
#         dic[i]="fail"
# print(dic)


# newdic={
#     "fra":["kola","coca","lunch"],
#     "dra":"dunda",
#     "hny":"viccky"
    
# }

# print(newdic["fra"][1])


# newdic=[{
#     "country":"india",
#     "visits":100,
#     "cities":["Delhi","Kanpur","Noida"]
# },{
#     "country":"russia",
#     "visits":0,
#     "cities":["moscow","dakh","ams"]
# }]

# print(newdic)

# def add_new_country(x,y,z):
#     newdic.append({"country":x,"visits":y,"cities":z})
    
# add_new_country("usa",2,["new york","new jersey"])    
# print(newdic)



# *********************Auction Program***********************


print('''
___________
 \         /
  )_______(
  |"""""""|_.-._,.---------.,_.-._
  |       | | |               | | ''-.
  |       |_| |_             _| |_..-'
  |_______| '-' `'---------'` '-'
  )"""""""(
 /_________\
 `'-------'`
.-------------.
/_______________\
''')
print("welcome to the Auction")

bidderdictionary={}

bidding=False
while not bidding:
    newUser=input("Bidder's name?\n")
    newUserBid=int(input("what will the bid amount?\n"))
    bidderdictionary[newUser]=newUserBid
    ques=input("is there any other bidder?\n")
    if(ques=="no"):
        bidding=True

print(bidderdictionary)   
max=0
name=""
for i in bidderdictionary:
    if(int(bidderdictionary[i])>max):
        max=bidderdictionary[i]
        name=str(i)

print(f"the winner of the auction is {name} with the winning amount of {max}")