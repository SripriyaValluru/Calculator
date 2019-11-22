#Menu file
import addition,subtract,multiplication,division



print("This program is for add,sub,mult and divide\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
s=int(input("Enter your choice:"))
if(s==1):
	print(addition.add())
elif(s==2):
	print(subtract.sub())
elif(s==3):
	print(multiplication.mult())
elif(s==4):
	print(division.div())

else:
	print("Invalid input")	