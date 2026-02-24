def men_from_boys(arr):
    men = list(set(x for x in arr if x % 2 == 0))
    boys = list(set(x for x in arr if x % 2 == 1))
    
    return sorted(men) + sorted(boys, reverse=True)