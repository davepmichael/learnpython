is_number = False
num = 0

while not is_number:
	is_number = True
	try:
		num = int(input("enter a number: "))
	except NameError:
		print("I said a number!")
		is_number = False

if num%2 == 0:
	print("Your number is divisible by 2")
elif num%3 == 0:
	print("Your number is divisible by 3")
elif num%5 == 0:
	print("Your number is divisible by 5")
else:
	print("Your number isn't divisible by 2, 3, or 5")

