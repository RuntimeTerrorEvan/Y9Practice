print("Welcome to the Movies!")
print("Please enter the ages of the customers")

for customer in range (0,10,1):
	age = int(input("Enter the customer age..."))

	if (age >= 3 and age<= 13): 
		print("This is a Child and will pay $8.99")

	elif (age>= 14 and age<= 64):
		print("This is a General Admission and will pay $12.50")

	elif age >= 65:
		print("This is a Senior and will pay $9.99")

	else: 
		print("This person goes for free!")

	print ("Thank you!")
