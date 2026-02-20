def multiples(m: int, n: int | float) -> list[int] | list[float]:
    return [x * n for x in range(1, m+1)]