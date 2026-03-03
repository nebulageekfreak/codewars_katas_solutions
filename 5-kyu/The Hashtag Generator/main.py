def generate_hashtag(s):
    generator = '#' + ''.join([x.title() for x in s.split()])
    return generator if 1 < len(generator) <= 140 else False 