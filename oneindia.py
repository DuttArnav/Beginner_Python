techtalks={"Aman","Riya","kabir","Fatima","Zara"}
sportsfest = {"Zara", "Rohan", "Kabir", "Aman", "Nina"}
culturalnite = {"Fatima", "Riya", "Nina", "Zoya"}

# Students who participated in all three events
all_events = techtalks & sportsfest & culturalnite
print("Students who participated in all three events:", all_events)

# Students who participated in at least one event
at_least_one = techtalks | sportsfest | culturalnite
print("Students who participated in at least one event:", at_least_one)

# Maximum students participating in one of the three events
max_students = max(len(techtalks), len(sportsfest), len(culturalnite))
print("Maximum students participating in one of the three events:", max_students)
