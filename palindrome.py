# simple palindrome check using while loop
s = input("Enter an integer: ").strip()
try:
    n = int(s)
except ValueError:
    print("Invalid input")
else:
    if n < 0:
        print("Not a palindrome")
    else:
        original = n
        rev = 0
        while n > 0:
            rev = rev * 10 + n % 10
            n //= 10
        print("Palindrome" if rev == original else "Not a palindrome")