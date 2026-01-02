time =int(input("Enter time in secondss: "))
sec = int(time) % 60
min = int(time) // 60
print(f"{time}  seconds is {min} minutes and {sec} seconds")
