marks =int(input("Enter tger marks out of 100: "))
print(f"Marks: {marks}")
marks2 =int(input("Enter tger marks out of 100: "))
print(f"Marks2: {marks2}")

total = marks + marks2

weight3 = float(0.50* total)
#print((f"your percentage in exams{float(marks+marks2)*100/200}"))
print("f{weight3} %")

print("now moving to the next level of the game")
performance =float(input("Enter your performance score out of 100: "))
weight2= float(0.20 * performance)
print("f{weight2} %")

print("now moving to the 3rd level of the game")
activity1 = float(input("Enter your activity score out of 100: "))
activity2 = float(input("Enter your 2nd activity score out of 100: "))
activity3 = float(input("Enter your 3rd activity score out of 100: "))

weight1= float(0.30 * (activity1 + activity2 + activity3) / 3)
print("f{weight1} %")

final_score = weight1 + weight2 + weight3
print(f"Your final score is: {final_score:.2f}")

result =float(weight3+weight2 + weight1)*100/300
print(f"Your final result is: {result:.2f}%")



