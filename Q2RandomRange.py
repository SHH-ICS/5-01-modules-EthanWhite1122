# Create a program that accepts 2 numbers from the user. 
# Your program will output a random number between the range given by the user.
import random
x=input("Enter first number:  ")
y=input("Enter second number: ")
if float(x) > float(y):
    print(" First number must be smaller than second number.")
else:
    print(random.randint(int(x),int(y)))
