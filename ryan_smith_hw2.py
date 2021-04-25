#ryan_smith_hw1.py
#Ryan Smith
#smithry9@oregonstate.edu
#Takes an year input from a user and determines if that year is a leap year.

#Loops asking the user for an input until it is a valid integer
while(True):
	#Prompts the user for an input
	print("Enter a year:",end=" ")
	inputVal = input()
	isInt = True
	#checks each character to make sure they are all numbers
	for character in inputVal:
		if(ord(character) < 48 or ord(character) > 57):
			isInt = False
			break
	#Exit the while loop if the input is only numbers
	if(isInt == True):
		break
	else:
		#give error and loop again if the input was not an integer
		print("Error: Input was not a valid integer")
	
#converts the input string to an int
inputVal = int(inputVal)

#checks if the input is divisible by 4
if(inputVal % 4 != 0):
	#if it isn't then it is not a leap year
	print(str(inputVal) + " is not a leap year!")
else:
	#if it is, then check if it is divisible by 100
	if(inputVal % 100 == 0):
		#if it is divisible by 100, see if it is also divisible by 400
		if(inputVal % 400 != 0):
			#if not then it isn't a leap year
			print(str(inputVal) + " is not a leap year!")
		else:
			#otherwise it is a leap year
			print(str(inputVal) + " is a leap year!")
	else:
		#if not divisible by 100, then it is a leap year
		print(str(inputVal) + " is a leap year!")

