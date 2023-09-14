"""Write a Python function that checks whether a word or phrase is palindrome or not.
A palindrome is word, phrase, or sequence that reads the same backward as forward"""

def palindrome(s):
    #remove spaces from string using replace()
    s = s.replace(' ','')
    #check is string == reversed version of the string
    return s == s[::-1]
#check 
palindrome('nurses run')

#challenge
"""Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
Pangrams are words or sentences containing every letter of the alphabet at least once"""
import string
def ispangram(str1, alphabet=string.ascii_lowercase):
    #create a set of the alphabet
    alphaset = set(alphabet)
    #remove any spaces from the input string
    str1 = str1.replace(" ","")
    #covert into all lowercase
    str1 =str1.lower()
    #grab all unique letters from the string set
    str1 = set(str1)
    #alphabet set == string set input
    return str1 == alphaset
#check
ispangram("The quick brown fox jumps over the lazy dog")
