
print("Enter the votes of 1st candidate")
candidate=["candidate1","candidate2","candidate3","candidate4"]
sum=0
sum1=0
for i in candidate:
    print(i)
    for j in range(4):
        vote=int(input("Enter the votes of 1st candidate: "))
        sum=sum+vote
    print(f"The total votes of {i} is {sum}")
for k in candidate:
    print(k)
    for m in range(4):
        vote1=int(input("Enter the votes of 2nd candidate: "))
        sum1=sum1+vote1
    print(f"The total votes of {k} is {sum}")
if sum1>sum:
    print(f"The winner is candidate2 with {sum1} votes")
else:
    print(f"The winner is candidate1 with {sum} votes")       
    