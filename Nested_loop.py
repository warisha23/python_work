''' return the sum of the numbers in the array, except ignore sections of numbers startign with 
6 and extending to the next 9 (every 6  will be followed by at least one 9) return 0 for no numbers '''

def numbr_69(arr):
    total = 0
    add = True 

    for num in arr:
        while add:
            if num!=6:
                total += num
                break 
            else:
                add= False
        while not add:
            if num!=9:
                break
            else:
                add = True 
                break 
    return total
#check 
numbr_69([1,3,5])
numbr_69([4,5,6,7,8,9])
numbr_69([2,1,6,9,11])
