"""write a function that checks whether a number is in
a given range(inclusive of high and low)"""

def ran_check(num,low,high):
    if num > low and num < high:
        return True
    else: 
        return False
#check
ran_check(5,2,7)

#another way using range
def high_low(num,low,high):
    if num in range(low,high+1):
       print(f'{num} is in range of {low} and {high}')
    else:
       print ('not in range')
