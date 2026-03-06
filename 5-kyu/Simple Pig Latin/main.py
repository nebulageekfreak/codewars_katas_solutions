def pig_it(text):
    lst = text.split()
    for i, v in enumerate(lst):
        if v not in '!?':
            lst[i] = v[1:] + v[0] + 'ay'
    return ' '.join(lst)
