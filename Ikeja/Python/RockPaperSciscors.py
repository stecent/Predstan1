#-*-coding:utf8;-*-
#qpy:3
#qpy:console

print("Rock Paper Scissors Game Designed by Raji")
from random import randint
import statistics 

def ComputeGame():
 x=0
 list=[]
 while x<3 :
  while True:
   while True:
    try:
     range=int(input("Do you want to choose the Range of Nu	mbers \n Enter 1. if Yes \n Enter 2. if No"))
     break
    except:
     print(" Must be either 1 or 2")
     continue 
   if range == 1:
    while True:
     Num1 = input("Enter Starting Number")
     Num2 = input("Enter Ending Number")
     try:
       Num1 = int(Num1)
       Num2 = int(Num2)
       print("Computer have Generated between", Num1, "and", Num2)
       break
     except:
       print(" Must be an integer")
       continue 
    GenNumber= int(randint(Num1, Num2))
    break
   elif range == 2:
    GenNumber = int(randint(1, 50))
    print("Computer have Generated between 1 to 50")
    break
   else:
     print(" Must be either 1 or 2")
     continue
  GuessNumber= int(input("Please Enter Your Number"))
  if GuessNumber == GenNumber:
    y="Correct"
    print("You got a Correct Number")
  else:
    y="Wrong"
    print("You got it wrong")
    print("Answer is:",GenNumber)
  
  list.append(y)
  
  
  x+=1
 print("See Result:",list)
 Result=statistics.mode(list)
 if Result == "Wrong":
     print("You Lost to the Computer ")
 else:
     print("You Won the Computer")
 
     
ComputeGame()
while True:
 TryAgain=int(input("Do you want to try again? \nEnter 1. for Yes\n Enter 2. for No"))
 if TryAgain==1:
      ComputeGame()
      continue 
 else:
      break
