def what_century(year):
    century = int(year[:2])
    if int(year) % 100 > 0:
        century += 1   
    
    century = str(century)
    if century in ["11", '12', '13']:
        return f"{century}th"
    elif century[-1] == '1':
        return f"{century}st"
    elif century[-1] == '2':
        return f"{century}nd"
    elif century[-1] == '3':
        return f"{century}rd"
    return f"{century}th"
    