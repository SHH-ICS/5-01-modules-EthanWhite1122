# Create a program that will ask the user an addition question. 
# The program will generate two random numbers between 1 and 100, and display them as an addition question with appropriate prompts.
import random
x=(random.randint(1,101))
y=(random.randint(1,101))
print("What is the sum of", x, "+", y, "?")
try:
    z= int(x) + int(y)
    a=input()
    if int(z) == int(a):
        print("You are right go buy yourself a pizza you deserve it")
    else:
       print("You are WRONG. NO PIZZA FOR YOU!!!")
except ValueError:
    print("Why didnt you put a whole number idiot")
