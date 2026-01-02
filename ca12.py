marks=[]
mar=0
n=input("enter a range")
count=0
for i in range(5):
    mar=int(input("Enter the marks"))
    marks.append(mar)
    count=count+1
    print(marks)
sum=0
for j in marks:
    sum=sum+j
print(sum)
avg=0
s=0
for k in marks:
    s=s+k
    avg=s/n
print(avg)    
print(min(marks))
print(max(marks))
print(marks.sort)