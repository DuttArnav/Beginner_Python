para= "Python is a powerful programming language. It is widely used for web development, data analysis, artificial intelligence, and more. Learning Python can open up many opportunities in the tech industry. Its simple syntax makes it easy for beginners to"
vowels = "aeiouAEIOU"
count = 0   
for char in para:
    if char in vowels:
        count =count+ 1  
print(count)    
for i in range(10,0,-1):
    print(i*2)    
    
ser=input("Enter a string ")   
ser1=ser[::-1]

len1=len(ser)
print(ser1[0:len1])

if ser==ser1:
    print("Palindrome")
else:print("Not a palindrome")

    