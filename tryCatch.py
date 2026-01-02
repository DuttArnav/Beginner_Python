try:    
  try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    result=num1/num2
    print("Error: Division by zero is not allowed.")
    f=open("abc.txt","r")
    print(f.read())
    f.close()
    
    print(f"The result of {num1} divided by {num2} is {result}")
  except ValueError:
    print("Invalid input. Please enter numeric values.")
  except ZeroDivisionError:
     print("zeroerror") 
except FileNotFoundError:
    print("lauda")       
    