def high_and_low(numbers):
    return f"{max(map(int, numbers.split()))} {min(map(int, numbers.split()))}"
