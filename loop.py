n=int(input("enter the number"))
if (n<=15):
    if(n==10):
        print("play cricket")
    else:
      print("play football")
else:
    print("dont play") 
    
# Looping Statements :-while, for.
sea_level=float(input("Enter the sea level in meteers :"))
height=float(sea_level/1000)
if (height > 690):
    print("You are at Exosphere")
elif (height > 85 and height <= 690):
    print("You are at Thermosphere") 
elif ( height > 50 and height <= 85):
    print("You are at Mesosphere")
elif (height > 20 and height <= 50):
    print("You are at Stratosphere")
else:
    print("You are at Troposphere")