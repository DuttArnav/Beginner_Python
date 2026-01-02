n=int(input("Enter the digit u want to reverse: "))
if (n < 0):
    print("not valid")
    r = 0
else:
    r = 0
    while (n != 0):
        digit = n % 10
        r = (r * 10) + digit
        n = n //10
    print("The reverse of the number is:", r)              