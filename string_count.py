"""write a function that accepts a string and calculates the number of upper case
and lower case letters"""

#string methods: .isupper() and .islower()

def up_low(s):
    upper_count = 0
    lower_count = 0
#iterate through each character in the string
    for char in s:
        if char.isupper():
            upper_count+=1
        elif char.islower():
            lower_count+=1
    return upper_count, lower_count
    print(f'original string: {s}')
    print(f'uppercase count: {upper_count}')
    print(f'lowercase count: {lower_count}')
    
s= 'Hello Mr.Rogers, how are you this fine Tuesday?'
up_low(s)






