drivers = []
n = int(input("How many drivers to add? "))

for _ in range(n):
    name = input("Enter driver's name: ")
    team = input("Enter team name: ")
    
    count=int(input("How many lap times to enter? "))
    lap_time = []
    for lp in range(count):
        lp=int(input(f"Enter lap time {lp + 1}: "))
        lap_time.append(lp)
    
    drivers.append({"name": name, "team": team, "laps": lap_time})
print(drivers)

