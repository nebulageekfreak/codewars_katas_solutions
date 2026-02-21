def square_digits(num):
    #   verbose solution 
#     squared = '' 
#     for x in str(num):
#          squared += str(int(x) ** 2)
#     return int(squared)
    # one-line solution
    return int(''.join(str(int(x) ** 2) for x in str(num)))