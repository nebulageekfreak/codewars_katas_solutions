def delete_nth(order,max_e):
    lst = []
    for x in  order:
        if max_e > lst.count(x):
            lst.append(x)
    return lst