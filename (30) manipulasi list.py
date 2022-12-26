# operasi 

# index    0(-3) 1(-2)  2(-1)
data = ["Tono","Tini","Dino"]

# mengambil data dari list ini 
data_pertama = data[0]
print(f"data pertama = {data_pertama}")
data_terakhir = data[-1]
print(f"data terakhir = {data_terakhir}")

data_tono = data[-3]
print(f"data tono = {data_tono}")

# Mengambil jumlah data dalam list 
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

## Manipulasi data lsit 

# Menambah item pada list sesuai posisi 
print(f"data sebelum ditambah : \n{data}")
# data.insert(posisi,item)
data.insert(1,"Dono")
print(f"Ini data setelah di insert : \n{data}")

# Menamabh di akhir list 
data.append("Dono") # append = menambah di akhir list 
print(f"data setelah ditambah lagi : \n{data}")

# Menambahkan list dan list 
data_baru = ["Ujang","Usep","Asep"]
data.extend(data_baru) #extemnd = menambahkan 
print(f"data gabungan : \n{data}")

# Merubah data 
# Kita ubah data ke 1 ( Dono) Menjadi (Ono)
data[1] = "Ono"
print(f"data yang sudah dirubah : \n{data}")

# Menghilangkan data 
data.remove("Asep") #remove = menghilangkan data
print(f"Data setelah ada yang dihilangkan : \n{data}")

# Menghilangkan data paling belakang
data.pop() #pop untuk menghilangkan data paling belakang
print(f"data akhir : {data}")