n=int(input("Enter the total number of customer"))
custom=[]
cus=0
it=0
item=[]
for i in range(n):
    cus=input("Enter the number of customer")
    custom.append(cus)
    print(custom)
for i in custom:    
 for j in range(n):
    it=input("Enter the item purchased by each customer ")
    item.append(it)
    print(f"for {i} customer he purchased {it} item")
    break
sales=0
dis=0
price=0 
count=0       
for k in item:
    count=count+1
print(count)    
    
if (count>10):
 print("10% Discount are applied")
if(count>5 and count<10):
 print("5 % Discount")
if(count<5):
 print("No Discount")  
for k in item: 
    price=input("enter price of each item")
    sales=sales+price
    if(sales>250 and count>10):
     dis=(10*sales)/100 
     print(sales-dis)
    if(sales>250 and count<10 ):
      dis=(5*sales)/100 
      print(sales-dis)
    if(sales>250 and count<0 ):
      print("not valid")
print(sales,"Thank for shoppin")             
        
               
    