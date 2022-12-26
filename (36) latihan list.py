# contoh daftar buku 
# program list buku
list_buku = []
while True:
    judul = input("masukan judul buku\t:")
    penulis = input('masukan penulis\t:')
    buku_baru = [judul,penulis] 
    list_buku.append(buku_baru)
    print(list_buku)

    print("No.\t| Judul Buku\t |Penulis")
    for index, buku in enumerate(list_buku): 
        print(f"{index}\t|{buku[0]}\t\t |{buku[1]}")

    print("\n\n"+"="*5)
    if Lanjut == "n":
        break
print("PROGRAM SELESAI")


