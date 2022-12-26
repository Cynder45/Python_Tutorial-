data_angka = [1,3,3,4,5,6,7,8,9,10]
print(f"data angka = \n{data_angka}")

#count data 
jumlah_data_angka_4 = data_angka.count(4)
jumlah_data_angka_3 = data_angka.count(3)
print(f"Jumalh angka 4 = {jumlah_data_angka_4}")
print(f"Jumalh angka 3 = {jumlah_data_angka_3}")

# ambil posisi 
data = ["tono","dido","dino","dono","doni"]
print(f"data = {data}")

index_data_doni = data.index("doni")
print(f"Index data dudung = {index_data_doni}")

#mengurutkan lsit 
print(f"data angka sebelum sort = {data_angka}")
data_angka.sort()
print(f"data angka setelah di sort = {data_angka}")

print(f"data = {data}")
data.sort()
print(f" data sort = {data}")

# List secara terbalik
data_angka.reverse()
print(f"data angka terbalik = {data_angka}")
data.reverse()
print(f"data sort secara terbalik = {data}")
