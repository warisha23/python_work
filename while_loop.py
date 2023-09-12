#prompt the user to enter a series of pizza toppings until they enter quit
#prompt = input("Enter the toppings you want on your pizza: ")
#prompt += "/nEnter 'quit' to end the program." 

#while True:
#	pizza = input(prompt)
#
#	if pizza == 'quit':
#		break
#	else:
#		print(f"we have added {pizza.title()} to your pizza")


#page 127 ex 7.10
responses = {}
polling_active = True

while polling_active:
	name= input("\nwhat is your name? ")
	response = input("If you could visit one place in the world, where would it be? ")

	responses[name]= response
repeat = input("Would you like another person to respond? yes or no ")
if repeat =='no':
	polling_active= False

print("\n-----Poll Results----")
for name, response in responses.item():
	print(f"{name} would like to go to {response}")


