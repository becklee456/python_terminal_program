# simple calculator

running=True
print("choose operation")

print("    1. Add \n    2. Subtract \n    3. Multiply \n    4. Divide \n    5. Q \n")


def addFunc(a,b):
   sum=a+b
   print(sum)
def subtractFunc(a,b):
   subtract=a-b
   print(subtract)
def multiplyFunc(a,b):
   multiply=a*b
   print(multiply)
def divideFunc(a,b):
   divide=a/b
   print(divide)


while running :
 
 operation=int(input("plase choose operation : "))
 if operation == 5 :
      ask=input("are you sure you want to quit y/n")
      if ask == "y" :
        break
      else:
        continue
      
 num1=int(input("please enter first number : "))
 num2=int(input("please enter second number : "))
 
 match (operation) :
    case 1:
      addFunc(num1,num2)
    case 2:
      subtractFunc(num1,num2)
    case 3:
      multiplyFunc(num1,num2)
    case 4:
      divideFunc(num1,num2)
    
    case _:
      print("invalid input")