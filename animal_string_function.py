""" 
write a Function takes a two-word string and returns True if both words
begin with the same letter 
"""
def animal_cracker(text):
    #split the input string into two words 
    words = text.split()
    first_word = words[0][0]
    second_word= words[1][0]
    if first_word.lower()==second_word.lower():
        return True
    else:
        return False    
#check
animal_cracker('Levelheaded, Llama')
animal_cracker('crazy Kangaroo')