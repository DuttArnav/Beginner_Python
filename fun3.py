drivers=[
   { "name":"Lando Norris",
    "team":"McLaren",
    "laps":[82.5, 81.3, 80.9]}
   {
    "name":"Daniel Ricciardo",
    "team":"McLaren",
    "laps":[83.1, 82.7, 81.5]
   }
]
for d in drivers:
    if d["name"]=="Lnado Norris":
        d["laps"].append(90.5)
        avg = sum(d["laps"]) / len(d["laps"])
        print(avg)
  
def addlaps(drivers,name,team,lap_time):
   drivers=[
      {
          "name":name,
          "team":team,
          "laps":[lap_time]
      } 
   ]
   return drivers

def names(drivers,name,team,lap_time):
    for d in drivers:
        d["name"]=input("Enter driver's name: ",name)
        drivers.append(name)
        d["team"]=input("Enter team name: ",team)
        drivers.append(team)
        d["laps"]=input("Enter lap time: ",lap_time)
        drivers.append(lap_time)
    return drivers  

def average_lap(drivers, name):
    best_avg = None
    for d in drivers:
        if d.get("name") != name:
    

 
   