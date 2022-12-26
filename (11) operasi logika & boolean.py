# operasi logika & boolean 
# not, or, and, xor

# NOT
print("==NOT==")
a = True 
c = not a
print("data a =", a)
print("---------")
print("data c = ", c)

# OR 
print("==OR==")
a = False 
b = False 
c = a or b 
print(a , "OR", b , "=", c)
print("---------")
a = True 
b = False 
c = a or b 
print(a , "OR", b , "=", c)
print("---------")
a = False 
b = True 
c = a or b 
print(a , "OR", b , "=", c)
print("---------")
a = True 
b = True
c = a or b 

# AND (Jika 2 nilai true, maka true )
print("==AND==")
a = False 
b = False 
c = a and b 
print(a , "AND", b , "=", c)
print("---------")
a = True 
b = False 
c = a and b 
print(a , "AND", b , "=", c)
print("---------")
a = False 
b = True 
c = a and b 
print(a , "AND", b , "=", c)
print("---------")
a = True 
b = True
c = a and b 
print(a , "AND", b , "=", c)
print("---------")