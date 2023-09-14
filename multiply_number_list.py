"""write a python function to multiply all the numbers in a list"""
def multiply(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result
#check
multiply([1,2,3,-4])