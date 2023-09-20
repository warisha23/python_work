#1.Handle the exception thrown by the code below by using try and except blocks.

try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print("There was an error")


#2. Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'

try:
    x = 5
    y = 0
    z = x/y
except:
    print("There was an error!")
finally:
    print("All done")

#3. Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.
def ask():
    while True:
        try:
            n = int(input("Please enter a number: "))     
        except:
            print("Whoops! Wrong entry, try again \n")
            continue
        else: 
            print("Thank you!")
            break
        finally:
            print("End of function")
    print("Your number squared is: ")
    print(n**2)
ask()