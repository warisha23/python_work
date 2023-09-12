''' Given a list of ints, return True if the array contains a 3 next to a 3 somewhere'''
def has_33(nums):
    for i in range(0,len(nums)-1):
        if nums[i] == 3 and nums[i + 1]== 3:
            return True
    return False
#check
has_33([1,3,1,3])
has_33([1,3,3])

''' Given a string, return a string where for every character in the original there are 
three characters '''

def laughter(pattern,text):
    result = ''
    for char in text:
        result += char*3
    return result
#check 
laughter('hello')
laughter('Mississippi')




