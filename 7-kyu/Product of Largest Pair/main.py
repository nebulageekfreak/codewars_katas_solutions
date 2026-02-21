def max_product(a):
    largest = max(a)
    secondLargest = a[0]
    for x in a:
        if x < largest and x > secondLargest:
            secondLargest = x
    return largest * secondLargest
