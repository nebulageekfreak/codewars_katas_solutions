def draw_stairs(n):
    stairs = []
    for x in range(1, n+1):
        stairs += f"I\n{' ' * x}" if x != max(range(1, n+1)) else "I"
    return ''.join(stairs)