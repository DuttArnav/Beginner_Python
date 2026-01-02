mood=[]
for i in range(5):
  m=(input("Enter the mood "))
  mood.append(m)
  
print(mood)

hap=0
sad=0
ang=0
bored=0
neutral=0      

#if "Happy" in mood:
#  hap=hap+1
    
week_days=["Monday","Tuesday","Wednesday","Thursday","Friday"]

for j in week_days:
  print(j)
  d=input("Enter your mood for the day ")
  if d in mood:
    print(f"Your mood for {j} is {d}")
    if d=="Happy":
      hap=hap+1
    elif d=="Sad":
      sad=sad+1
    elif d=="Angry":
      ang=ang+1
    elif d=="Bored":
      bored=bored+1
    elif d=="Neutral":
      neutral=neutral+1
    else:
      print("Invalid mood")
print(f"Your mood for the week is: Happy-{hap}, Sad-{sad}, Angry-{ang}, Bored-{bored}, Neutral-{neutral}") 
for j in mood:
    if j=="Angry" in week_days:
        print(j,"Take a deep breath and relax")
        
    
    