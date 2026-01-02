class InvalidMarksError(Exception):
    pass

# Q1: Data types & operators
def calculate_total_avg(marks):
    total = sum(marks)
    avg = total / len(marks)
    return total, avg

def eligible(avg):
    return avg >= 60

# Q2: Program flow control (grade assignment)
def grade_from_avg(avg):
    if avg >= 80:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "Fail"

# Q3: string operations (examples)
def string_ops(activity1, activity2):
    examples = {}
    examples["index0"] = activity1[0]
    examples["last"] = activity1[-1]
    examples["slice0_4"] = activity1[0:4]
    examples["len"] = len(activity1)
    examples["find"] = activity1.find("ball")       # -1 if not found
    examples["compare"] = (activity1 == activity2)
    examples["chars"] = [ch for ch in activity1]
    return examples

# Q4: lists & tuples operations
def list_tuple_ops():
    acts = ["Dance", "Music", "Football"]
    acts.append("Art")
    acts.insert(1, "Debate")
    popped = acts.pop(2)
    sliced = acts[1:4]
    student_fixed = ("Alice", 1+1j, "B")   # tuple: (name, roll, grade)
    return {"list": acts, "popped": popped, "sliced": sliced, "tuple": student_fixed}

# Q5: dictionaries & sets
def dict_set_ops():
    registry = {}
    # adding entries
    registry["Alice"] = ["Dance", "Music"]
    registry["Bob"] = ["Football"]
    # updating
    registry["Alice"].append("Art")
    # deleting
    del registry["Bob"]
    # loop items
    items = [(k, v) for k, v in registry.items()]
    unique = set(["Dance", "Music", "Art"])
    unique.add("Football")
    unique.discard("Music")
    union = unique.union({"Chess"})
    intersection = unique.intersection({"Dance", "Chess"})
    return {"registry": registry, "items": items, "set": unique, "union": union, "intersection": intersection}

# Q6: functions (default args, *args, multiple return)
def display_student(name="Unknown", age=0, roll=0+1j, grade=""):
    return f"{name}, {age}, {roll}, {grade}"

def activities_varargs(*args):
    return list(args)

def stats_return(total, avg, grade):
    return total, avg, grade   # returns tuple

# Q7: exception handling examples
def read_student():
    try:
        name = input("Name: ")
        age_s = input("Age: ")
        age = int(age_s)             # may raise ValueError
        marks = []
        for i in range(3):
            try:
                m_s = input(f"Mark {i+1}: ")
                m = float(m_s)
                if m < 0 or m > 100:
                    raise InvalidMarksError(f"Mark {m} out of range")
                marks.append(m)
            except InvalidMarksError as ime:
                print("InvalidMarksError:", ime)
                # decide to re-ask this mark
                return None
            except ValueError:
                print("Please enter a numeric mark.")
                return None
        total, avg = calculate_total_avg(marks)
        g = grade_from_avg(avg)
        print("Total, Avg, Grade:", total, avg, g)
    except ValueError:
        print("Invalid age input.")
    except Exception as e:
        print("Unexpected error:", e)
    finally:
        print("Student read attempt finished.")
    return None

# Demonstrations for program flow constructs (for/while/break/continue/pass)
def demo_flow():
    marks = [55.0, 70.0, 80.0]
    # for loop: print each mark
    for m in marks:
        print("Mark:", m)
    # while loop: enroll until 'no'
    enrolled = []
    while True:
        resp = input("Enroll in activity (type 'no' to stop, 'skip' to skip, 'pass' to no-op): ").strip().lower()
        if resp == "no":
            print("Stopping enrollment.")
            break
        if resp == "skip":
            print("Skipping this iteration.")
            continue
        if resp == "pass":
            pass  # no-op
            print("Passed (no operation).")
            continue
        enrolled.append(resp)
        print("Enrolled:", resp)
    return enrolled

if __name__ == "__main__":
    # minimal example usage (non-interactive parts)
    # Q1 example
    name = "John"
    age = 20                # int
    marks = [72.5, 65.0, 88.0]  # floats
    roll = 12 + 1j          # complex with imaginary part 1
    total, avg = calculate_total_avg(marks)
    print("Total:", total, "Avg:", avg, "Eligible:", eligible(avg))
    # Q2 grade
    print("Grade:", grade_from_avg(avg))
    # Q3 string ops
    print("String ops:", string_ops("Basketball", "basketball"))
    # Q4 list/tuple
    print("List/Tuple ops:", list_tuple_ops())
    # Q5 dict/set
    print("Dict/Set ops:", dict_set_ops())
    # Q6 functions
    print(display_student("John", age, roll, grade_from_avg(avg)))
    print("Activities varargs:", activities_varargs("Dance", "Art"))
    print("Stats return:", stats_return(total, avg, grade_from_avg(avg)))
    # Q7: safe read (interactive)
    # read_student()
    # demo_flow()