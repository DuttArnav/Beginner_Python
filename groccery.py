grocerry_items = []

n=input("enter the total items bought :")
gs=input("Enter the Groccery items you bought: ")
grocerry_items.append(gs)

for i in grocerry_items(n):
    print("The items u bought are :",i)

price=[]
pr=input("enter the prices of Each Item :")
price.append(pr)

bill=0
bill=bill+int(price)

for item in grocerry_items,price:
    if price>20:
        print(f"The item of this :{price} is this{grocerry_items}")

new_bill = grocerry_items.pop()
new_price = price.pop()
print(f"The new list of items is :{new_bill} and the new price is :{new_price}")

new_bill =0
new_bill=new_bill+int(new_price)
print(f"The total bill is :{new_bill}")