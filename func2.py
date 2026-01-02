def m_function(food):
    for i in food:
        print(i)
fruit=["apple","banana","cherry"]        
m_function(fruit)

def m_function(x):
    return x + 5
print(m_function(10))

def tri_recursion(x):
    if(x>0):
        result = x + tri_recursion(x - 1)
        print(result)
    else:
        result = 0  
    return result

x= lambda a : a + 10
print(x(5))