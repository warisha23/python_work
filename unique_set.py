"""write a python function that takes a list and returns a new list with unique elements of the first list"""
def unique_list(lst):
    lst=[]
    for number in lst:
        if number not in lst:
            lst.append(number)
        return lst

#another way using set 
    def unique_num(x):
        return list(set(x))
    
#check
unique_list([1,1,1,1,2,2,3,3,3,3,4,5])

