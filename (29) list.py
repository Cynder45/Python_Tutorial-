# LIST

"""
angka = 1 
angka = 2
angka = 3

#Diatas tidak efektif untuk kumpulan" data 
"""

# Kumpulan data numbers
data_angka = [1,6,4,2,3]
print(data_angka)

# Kumpulan data string 
data_str = ["ucup","tono","tini"]
print(data_str)

# Kumpulan data boolean
data_bool = [True,False,False,True]
print(data_bool)

# Kumpulan campuran 
data_campuran = [1,"Bala-bala",2,"Bakso","Tono",True,"Tini",False]
print(data_campuran)

# Cara alternatif membuat list 
data_range = range(0,10,2) # jika (0,10,2) -> berarti yang genap saja #(start,stop,step)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dngn for loop, list comprehension
data_list_for = [i for i in range(0,10)]
print(data_list_for)
data_list_for = [i**2 for i in range(0,10)]
print(data_list_for)

# Membuat lsit pakai for dan if 
list_for_if = [i for i in range(0,10) if i != 5] # angka 5 tidak ada 
print(list_for_if)

# Membuat list pakai if dan for, untuk hasil ganjil 
list_for_if = [i for i in range(0,10) if i%2 != 0 ] #untuk mengampilkan yang ganjil sajah 
print(list_for_if)

# Membuat list pakai if dan for, untuk hasil genap 
list_for_if = [i for i in range(0,10) if i%2 == 0  ] #untuk mengampilkan yang genap
print(list_for_if)

