def calculate(num1, operation, num2):
    if operation in '+-*':
        return eval(f"{num1} {operation} {num2}")
    elif operation == '/' and num1  and num2:
        return eval(f"{num1} {operation} {num2}")
    else:
        return None
    
    # using try/except
#     try:
#         return eval(f"{num1} {operation} {num2}")
#     except:
#         return None