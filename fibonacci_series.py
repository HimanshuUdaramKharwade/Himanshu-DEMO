# simple Fibonacci series — prints first n terms
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()

if __name__ == '__main__':
    try:
        n = int(input("How many terms? ").strip())
        if n <= 0:
            print("Enter a positive integer")
        else:
            fibonacci(n)
    except ValueError:
        print("Invalid number")