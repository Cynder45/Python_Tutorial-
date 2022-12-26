#perulangan 
"""
angka = 1
print(angka)
angka = angka + 1 
print(angka)
angka = angka + 1
print(angka)
"""

#for kondisi:
#  aksi 

# ini dengan list
"""
angka2 = [0,2,5,8,4] #Ini adalah list 
print(angka2)

for i in angka2: 
    print(f"i sekarang -> {i}")

print("akhir dari program")
"""

# ini dengan range
"""
angka_range = range(5)

for i in angka_range:
    print(f"i sekarang -> {i}")
print("akhir dari program")
"""
#angka
print("="*5,"ANGKA","="*5)
for i in range(1,9):
    print(f"ini nilai i -> {i}")
print("akhir dari program")

#kata
print("="*5,"KATA","="*5)
for i in range(1,5):
    print("Saya Rendy")
print("akhir dari program")

#menggunakan string
print("="*5,"STRING","="*5)
data_str = "Kamu Siapa , Chuaks"

for i in data_str:
    print(i)
print("akhir dari program")