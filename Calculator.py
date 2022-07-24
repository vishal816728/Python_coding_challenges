# print(("this program will tell you how many days in a month").title())
# year=int(input("Enter year\n"))
# month=int(input("Enter Month\n"))

# leap_year=""

# if year%4==0 and year%100!=0:
#     leap_year="yes"
# elif year%100 and year%400==0:
#     leap_year="yes"
# else:
#     leap_year="no"

# def days_in_month():
#     if leap_year=="yes":
#         days=[31,29,31,30,31,30,31,31,30,31,30,31]
#     else:
#         days=[31,28,31,30,31,30,31,31,30,31,30,31]
#     for i in range(1,13):
#         if i==month:
#             return ((f" there will be {days[i-1]} days in a month").title())
# if(month>0 and month<=12):
#     print(days_in_month())
# else:
#     print(("wrong input").title())




# ******************************Calculator*************************
print("""
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
""")
print("Welcome to the calculator")

def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

c=""
firstNumber=float(input("What's the first Number?\n"))
total=firstNumber
def calculator_functionality():
    operator=input("pick a operator \n +\n-\n*\n/\n")
    secondNumber=float(input("what is the other number?\n"))
    if(operator=="+"):
        print(add(total,secondNumber))
        return add(total,secondNumber)
    elif(operator=="-"):
        print(sub(total,secondNumber))
        return sub(total,secondNumber)
    elif(operator=="*"):
        print(mul(total,secondNumber))
        return mul(total,secondNumber)
    else:
        print(div(total,secondNumber))
        return div(total,secondNumber)
con=True
while con:
    total=calculator_functionality()
    if total:
        c=input(f"press 'y' to continue with the {total} or press 'n' to start new calculator or press 'e' to exit from the calculator\n")
        if c=='y':
            total=calculator_functionality()
        else:
            con=False
            print("Thank you using python calculator")
        