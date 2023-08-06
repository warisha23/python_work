# Write a method that reverses a string (without using builtin reverse method), use a for loop
def reverse_string(s):
    reverse_string = ''

    for i in s:
        reverse_string = i + reverse_string 
    return reverse_string

#outside the method we will get the input from user
user_input = input("Enter a string: ")
#call the method
output = reverse_string(user_input)
print("The Reversed string is:" , output)


