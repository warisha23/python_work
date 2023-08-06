#Write a method thar returns a modified string 
#A function that takes input as its parameter 
def modified_string(input):

#Initilize an empty list
    modified = []
    current_char = input[0]
    count = 1
# A for loop that iterates through the input starting from index 1
    for char in input[1:]:
        if char == current_char:
            count += 1
        else:
            modified.append(current_char)
            if count > 1:
                modified.append(str(count))
            current_char = char
            count = 1

    modified.append(current_char)
    if count > 1:
        modified.append(str(count))
# implement the join method to concatenate all the characters 
    return ''.join(modified)

input = input("Enter a string: ")
modified_string = modified_string(input)
print("Original:", input )
print("Modified:", modified_string)


    
    
