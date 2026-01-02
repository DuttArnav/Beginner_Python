print("hi welcomer to the store give me the name of products u want to get billed")
for i in range(1, 4):
    fruit =str(input("Enter the name of the fruit: "))
    print(fruit)
print("Enter the quantity of each fruit:")

for i in range(1, 4):
    qty = int(input(f"Enter quantity for {fruit}: "))
    if fruit.lower().upper() == "APPLE":
      price= 10* qty
      bill_1 =price
    elif fruit.lower().upper() == "BANANA":      
        price= 5* qty
        bill_2 =price
    elif fruit.lower().upper() == "ORANGE":
        price= 8* qty
        bill_3 =price
        print(f"total Bill is:", {bill_1 + bill_2 + bill_3})    
print("Thank you for shopping with us!")
   
