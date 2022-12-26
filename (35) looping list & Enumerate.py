#looping dari list 

# for loop 
print('\n for loop')
kumpulan_angka = [4,3,5,6,1]
for angka in kumpulan_angka:
    print(f"angka = {angka}")

peserta = ["tono","dono","rono","tomo","lono"]
for nama in peserta:
    print(f"nama = {nama}")

#for loop and range (cara lama)
print("\n" + "="*5,"for loop","="*5)
kumpulan_angka = [10,5,4,2,6,5]
panjang = len(kumpulan_angka)
for i in range(panjang):
    print(f"kumpulan angka = {i}")

# while 
print("\nwhile")
kumpulan_angka = [10,5,4,2,6,5]
panjang = len(kumpulan_angka)
i = 0 
while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1

# list comprehension (cara cepat / gampang)
print('\n list comprehension')
data = ['ucup',1,2,3,'otong']
[print (i) for i in data]

#enumerate 
print('\n enumerate')
data_list = ['ucup',1,2,3,'otong']
for index, data in enumerate(data_list):
    print(f'index = {index}, data = {data}')