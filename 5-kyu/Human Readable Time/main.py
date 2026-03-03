def make_readable(seconds):
    HH = seconds // 3600
    seconds %= 3600
    
    MM = seconds // 60
    seconds %= 60
    return f"{HH:02d}:{MM:02d}:{seconds:02d}"