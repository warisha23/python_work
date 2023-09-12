''' Write a function that returns the number of prime numbers that exist up to and including a given number'''
# by convention we will treat 0 and 1 as NOT prime

def count_prime(num):
    #check for 0 and 1 input
    if num <2:
        return 0
    # if 2 or greater 
    #store the prime numbers 
    primes = [2]
    #counter going up to the input num
    x=3
    #x is going through every number upto input number/ check if x is prime
    while x <= num:
        #check if x is prime
        for y in range (3,x,2):
            if x%y == 0:
                x+=2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return(len(primes))
#check 
count_prime(100) #25

    
