# simple calculator
def calc():
    print("Simple calculator: + - * /")
    a = input("Enter first number: ").strip()
    b = input("Enter second number: ").strip()
    op = input("Choose operation (+, -, *, /): ").strip()
    try:
        x = float(a)
        y = float(b)
    except ValueError:
        print("Invalid number")
        return
    if op == "+":
        res = x + y
    elif op == "-":
        res = x - y
    elif op == "*":
        res = x * y
 
    elif op == "/":
        if y == 0:
            print("Cannot divide by zero")
            return
        res = x / y
    else:
        print("Unknown operation")
        return
    if isinstance(res, float) and res.is_integer():
        res = int(res)
    print("Result:", res)

if __name__ == "__main__":
    calc()