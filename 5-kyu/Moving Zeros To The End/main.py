def move_zeros(lst):
    zeros = [x for x in lst if x == 0]
    return [n for n in lst if n not in zeros] + zeros