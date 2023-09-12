"""
Write a function that returns the lesser of two given number
if both numbers are even, but returns the greater if one or both numbers 
are odd 
"""

def lesser_of_two_even(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    else:
        return max(a,b)
#check
lesser_of_two_even(2,4)
lesser_of_two_even(2,5)


''' given two integers, return True if it sum of the integers is 20 or if one of the 
integers is 20. If not return False'''

def makes_twenty(n1,n2):
    if n1 + n2==20:
        return True
    elif n1== 20 or n2==20:
        return True         
    else:
        return False
#single-line code 
#return(n1+n2)== 20 or n1 ==20 or n2==20
#check  
makes_twenty(20,10)
makes_twenty(12,8)
makes_twenty(2,3)