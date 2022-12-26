# operasi yang dilakukan dengan penyingkatan 
# operasi ditambah dengan assingment

from operator import truediv


a = 5 # ini adalah assignment 
print("nilai a = ", a)

a += 1 
print("nilai a = a + 1",a )

a -= 2 
print("nilai a - 2 = ", a)

a *=3 
print("nilai a * 3 = ", a)

a /= 6 
print("nilai a / 6 = ", a)

b = 10 
print("\n nilai b = ", b)
b %= 3 
print("nilai b % 3 = ", b)

b = 10 
b //= 3
print("nilai b // 3 = ", b)


a = 5 
print("nilai a = ",a)
a **= 3
print("nilai a ** 3 = ", a)

#operasi bitwise 
c = True 
print("\nini nilai c",c)
c |= False  
print("nilai  c OR  false = ", c)
