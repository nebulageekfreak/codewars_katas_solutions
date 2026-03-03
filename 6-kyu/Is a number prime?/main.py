    # I used fermat primality method which is not ideal. 
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    
    bases = [2, 3, 5, 7, 11]
    for a in bases:
        if pow(a, num-1, num) != 1:
            return False
        return True