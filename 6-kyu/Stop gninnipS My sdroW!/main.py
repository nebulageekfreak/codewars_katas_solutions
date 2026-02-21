def spin_words(sentence):
    lst = sentence.split()
    for i, v in enumerate(lst):
        if len(v) >= 5:
            lst[i] = v[::-1]
    return ' '.join(lst)