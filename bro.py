try:
 print("This is a wlecoming message")
 
 except value_error :
    print("An error occurred:", str(e))
   def return_students(name,roll_no,marks):
    subject={
        "name":name,
        "roll_no":roll_no,
        "marks":[]
        
    } 
    return subject   
 def return_show(students,name,roll_no,marks,subject):
    for s in [subject]:
        name=input("Enter student's name: ",name)
        name.append(name)
        roll_no =input("Enter roll number: ",roll_no)
        roll_no.append(roll_no)
        s["marks"]=input("Enter marks: ",marks)
        students.append(marks)
    return students
  def sum_show(students,name,roll_no,marks,subject):
    print(sum(marks))  
    