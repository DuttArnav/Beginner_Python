try:  
  list1=[ "apple", "banana", "cherry"]
  list2=[]
  for fruits in list1:
    price=int(input(f"Enter price for {fruits}: "))
    list2.append(price)
    print(sum(list2))

except ValueError:
    print("Invalid input. Please enter a numeric value.")
        