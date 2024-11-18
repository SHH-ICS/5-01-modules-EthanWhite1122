# Create a program that will accept the two legs of a right-angle triangle, a and b, and display the length of the hypotenuse, c. 
# Remember to use prompts for the input and labels for the output. Use the formula a2 + b2 = c2 to calculate your answer.
import math
a= input("Enter Length of A ")
b= input("Enter Length of B ")
if a <= "1":
    print("Your numbers can not be negative or 0")
elif b <="0":
    print("Your numbers can not be negative or 0")
else:
    a=float(a)**2
    b=float(b)**2
    c=float(a)+int(b)
    c=math.sqrt(c)
    print("Your hypotenuse is:", float(c))