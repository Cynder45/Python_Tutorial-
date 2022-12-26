# Membandingkan Nilai 
# setiap hasil dari hasil komparasi adalah boolean 
 # > 
# < 
# >=
# <= 
# == 
# !=
# is 
# is not 

a = 4 
b = 2 

# lebih besar dari ()>) 
print("==lebih besar==")
hasil = a > 3
print(a,'>',3,'=', hasil)
hasil = b > 3
print(b,'>',3,'=', hasil)
hasil = b > 2
print(b,'>',2,'=', hasil)

# lebih kecil dari (<) 
print("==lebih kecil==")
hasil = a < 3
print(a,'<',3,'=', hasil)
hasil = b < 3
print(b,'<',3,'=', hasil)
hasil = b > 3
print(b,'<',3,'=', hasil)

# lebih besar dari sama dengan (>=) 
print("==lebih besar dari sama dengan==")
hasil = a >= 4 
print(a,'>=',4,'=', hasil)
hasil = b >= 2
print(b,'>=',2,'=', hasil)
hasil = b >= 5
print(b,'>=',5,'=', hasil)

# lebih kecil dari sama dengan (<=) 
print("==lebih kecil dari sama dengan==")
hasil = a <= 2 
print(a,'<=',4,'=', hasil)
hasil = b <= 2
print(b,'<=',4,'=', hasil)
hasil = b <= 4
print(b,'<=',4,'=', hasil)

#  sama dengan (==) 
print("== sama dengan==")
hasil = a == 4
print(a,'==',4,'=', hasil)
hasil = b == 4
print(b,'==',4,'=', hasil)
hasil = a == 2
print(a,'==',2,'=', hasil)
hasil = b == 2
print(b,'==',2,'=', hasil)

# tidak sama dengan (!=)
print("== tidak sama dengan==")
hasil = b != 4
print(b,'!=',4,'=', hasil)
hasil = a != 4
print(a,'!=',4,'=', hasil)
hasil = b != 2
print(b,'!=',2,'=', hasil)
hasil = a != 2
print(a,'!=',2,'=', hasil)

# is sebagai komparasi object identity  
x = 5 # ini adalah assignment membuat object 
y = 5 
print('nilai x = ,',x,',id = ',hex(id(x)))
print('nilai y = ,',y,',id = ',hex(id(y)))
hasil = x is y
print(' x is y', hasil)