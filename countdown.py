n=int(input("Enter the number of seconds for countdown: "))
if n < 0:
    print("does not exist")
while n >= 0:
    print(n)
    n =n- 1
print("Countdown finished!")  
