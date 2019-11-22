#Menu file
from add import add
from sub import sub
from mul import mul

print("This program is for add,sub,mult \n1.Addition\n2.Subtraction\n3.Multiplication")
s=int(input("Enter your choice:"))
if(s==1):
	a = int(input("Enter a value:"))
	b = int(input("Enter b value:"))
	print (add(a,b))
elif(s==2):
	a = int(input("Enter a value:"))
	b = int(input("Enter b value:"))
	print (sub(a,b))
elif(s==3):
	a = int(input("Enter a value:"))
	b = int(input("Enter b value:"))
	print (mul(a,b))


else:
	print("Invalid input")	
