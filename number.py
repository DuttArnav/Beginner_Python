#You’ve found a mysterious chest with a number lock. You need to analyze the code written on the lock.
#a) Find the sum of all digits (this unlocks the outer seal).
#b) Count how many digits are even vs. odd (this opens the second layer).
#c) Reverse the number (to read the code correctly).
#d) Check if the number is a palindrome (a clue for future puzzles).
#e) Count how many digits are divisible by 3 (used to activate a hidden mechanism).
n=int(input("Enter the digits:"))
sum = 0
while(n > 0):
     r = n % 10
     sum = int(sum + r)
     n=n//10
print("The sum of the digits is:", sum)
n=int(input("Enter the digits:"))
even=0
odd=0
while(n > 0):
    re = n % 10
    if re % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
    n = n // 10
print("The number of the digits is:",even, odd)    
r = 0

while (n != 0):
     digit = n % 10
     r = (r * 10) + digit
     n = n //10
print("The number of the digits is:",r)     
