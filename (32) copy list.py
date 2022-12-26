## Teknik menduplikat list 

a = ["Dono","Dino","Dodo"]
print(f"a = {a}")

b = a # pass by reference 
print (f"b = {b}")

# merubah member dari a 
a[1] = "Joko"
b.sort() 
print(f"a = {a}")
print (f"b = {b}")

# address dari kedua list a dan b 
print(f" address a = {hex(id(a))}")
print(f" address b = {hex(id(b))}")

# menduplikat lsit dengan copy 
print("Membuat list C dengan a.copy()")
c = a.copy() # full duplikat
print(f" address a = {hex(id(a))}")
print(f" address b = {hex(id(b))}")
print(f" address c = {hex(id(c))}")

print(f"a = {a}")
print (f"b = {b}")
print(f" c = {c}")

print("Diubahnya data 0")
c[0] = "Dadang"
print(f"a = {a}")
print (f"b = {b}")
print(f"c = {c}")

print("Diubahnya data 1")
c[0] = "Dedeng"
print(f"a = {a}")
print (f"b = {b}")
print(f"c = {c}")