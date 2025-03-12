a=float(input("Enter a: "))
b=float(input("Enter b: "))
def check(func):
    def wrapper(a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            return "Inputs must be numbers"
        if b == 0:
            return "Denominator can't be zero"
        return func(a, b)
    return wrapper

@check
def div(a, b):
    return a / b
result = div(a, b)
print("Result:", result)
