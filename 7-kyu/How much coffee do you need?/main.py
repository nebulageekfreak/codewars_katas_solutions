def how_much_coffee(events):
    coffee = 0
    for x in events:
        if x in 'cwcatdogmovie':
            coffee += 1
        elif x in 'CWCATDOGMOVIE':
            coffee += 2
    return coffee if coffee <= 3 else "You need extra sleep"