'''
1 for snake
-1 for water
0 for gun 

'''
import random
computer = random.choice([-1,0,1])
youstr= input("Enter Your Choice : ")
youDict = { "s":1,"w":-1,"g":0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}
you = youDict[youstr]
print(f" you choice {reverseDict[you]}\n Computer choice{reverseDict[computer]}")

if(computer== you):
    print("Its a Draw")
else:
    if(computer==-1 and you==1):
     print("YOU WIN!")
    elif(computer==-1 and you==0):
      print("You LOSE")
    elif(computer==1 and you==-1):
      print("You LOSE")
    elif(computer==1 and you==0):
       print("You WIN")
    elif(computer==0 and you==-1):
      print("You WIN")
    elif(computer==0 and you==1):
      print("You LOSE")
    else:
      print("Something went Wrong")
     