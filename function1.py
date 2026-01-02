def input_marks():
    marks_input = input("Enter marks separated by spaces: ")
    marks_list = [int(m) for m in marks_input.split()]
    return marks_list

def wsum():
    marks = input_marks()
    return wsum(marks)

print("The sum of marks is:", wsum())

