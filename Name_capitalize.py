"""Write a function that capitalizes the first and fourth letters of a name"""

def old_macdonald(name):
    first_half=name[:3] #from the begining all the way to index 3
    second_half=name[3:] #start from 3 to all the way to end 

    return first_half.capialize() + second_half.capitalize()
#check
old_macdonald('macdonald')


''' Given a sentence, return a sentence with the words reversed '''
    
def master_yoda(text):
    # first get a list of the words
    wordlist = text.split()
    reversedlist=wordlist[::-1]
    return ' '.join(reversedlist)
#checks
master_yoda('I am home')
master_yoda('we are ready')