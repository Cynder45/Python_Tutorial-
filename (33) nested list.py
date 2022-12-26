data_0 = [1,2]
data_1 = [5,4]
data_list_biasa = [1,2,5,4]
print(f"list biasa {data_list_biasa}")

list_2d = [data_0,data_1,data_list_biasa]
print(f"list 2d = {list_2d}")

# contoh penggunaan 
data_peserta0 = ["Dono", 25, "Laki - Laki"]
data_peserta1= ["Dino", 10,"Laki - Laki"]
data_peserta2 = ["Dadang", 50, "wanita"]
list_peserta = [data_peserta0,data_peserta1,data_peserta2]
print(f"list peserta = {list_peserta}")
for peserta in list_peserta:
    print(f"Nama peserta\t : {peserta[0]}")
    print(f"Umur peserta\t : {peserta[1]}")
    print(f"Jenis kelamin\t: {peserta[2]}\n")

# Permasalahan dengan reference 
list_copy = list_peserta.copy()
print(f"List copy : {list_copy}")
peserta[0] = "ucup"
print(f"List copy : {list_copy}")
print(f"List copy peserta: {list_peserta}") # data berubah 