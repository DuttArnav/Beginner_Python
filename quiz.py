ques = []
for i in range(4):
    q = input("Enter question ")
    ques.append(q)

real_ans = ["23", "24", "25", "26"]

ans = []
for j in range(4):
    a = input("Enter answer for question ")
    ans.append(a)

print(real_ans[0:])

for k in ans:
    if k in ans==real_ans[0:]:
        print("Correct")
    else:
        print("Wrong")