planet = []

n = int(input("How many planets have you visited? "))

for i in range(n):
    p = input("Enter the name of planet u visited more than once: ")
    planet.append(p)
    
print("The planets you have visited so far are:")
for i in planet:
    print(i)

new_planet =[]
for i in new_planet:
    input("Enter the name of new planet: ")
    new_planet.append(i)
      

for k in planet:
    if k in planet==new_planet[0:]:
        print("You have already visited this planet")
    else:
        np=input("Enter the name of new planet: ")    
        new_planet.append(np)
        print("The new list of planets is:",new_planet)
        
        