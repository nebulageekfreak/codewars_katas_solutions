def accum(st):
    return '-'.join([(st[x] * (x + 1)).title() for x in range(len(st))])