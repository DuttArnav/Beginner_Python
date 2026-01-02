lis=[1,2,3,[1,2,3]]
print(lis[3][1])  # this will print 2
lis2=["orange", "banana", "apple"]
lis2.append("grape")
print(lis2)  
list1=[1,2,3,4,5]
list1.insert(2,10)

print(list1)
sum_list=sum(list1)
print("The sum is:", sum_list)
max
num=max(list1)
print("The maximum number is:", num)    

list1.clear()

list1.extend("6,7,8")
list1.insert(1,9)
print(list1.pop(0))

list1.index
print(list1)

print(list1)

tuple1=(1,2,3,4,5)
tuple1.count(2)
print(tuple1)

drivers={
    "name":"Lando Norris",
    "team":"McLaren",
    "laps":[82.5, 81.3, 80.9]
}
drivers.items()
for j,k in drivers.items():
    print(j,k)
print(drivers.keys())
print(drivers.values())
print(drivers.get("team"))
print(drivers.pop("team"))
print(drivers.popitem())
print(drivers.update({"name":"gandu"}))
print(drivers.items())
print(drivers.clear()) 



string="immortal gay man entered into the dungeon of doom"  
words=string.split()
print(words)
str=len(words)
print(string[:-4])
string.lower()
string.upper()
string.capitalize()
string.replace("dungeon","castle")
string.startswith("immortal")
string.endswith("doom")
string.find("immortal")# if not found -1
string.find("imm")
string.isalnum()
string.isalpha()
string.isdigit()
string.isspace()
string.join(words)
string.lstrip()
string.rstrip()    
for ch in string:
    print(ch)
print(",".join(words))


set1={1,2,3,4,5,10}
for j in set1:
    print(set1)
set1.add(6)
set1.remove(3)
print(set1)

set1.discard(10) # no error if not found
print(set1)

print(set1.union({7,8,9}))

print(set1.intersection({4,5,6,7}))

print(set1.difference({4,5}))



set1.clear()

import pickle

f=open("data.bin","wb")
pickle.dump([1,2,3,4],f)
f.close()
f=open("data.bin","rb")
data=pickle.load(f)
print(data)
f.close()

f=open("data.txt","w")
f.write("Hello, World!\n")  
f.close()
f=open("data.txt","r")
content=f.read()    
print(content)
f.close()