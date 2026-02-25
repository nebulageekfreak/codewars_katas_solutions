def duplicate_count(text):
    text = text.lower()
    return len({x for x in text if text.count(x) > 1})