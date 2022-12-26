#Break
angka = 0
while angka < 5:
    angka += 1
    print(f"Smngt lanjutkan -> {angka}")
    if angka == 3: 
        print("Naisu!")
        break #
        
    print("Cukup")
print("finish")

#contoh 
data_int = int(input("hitung sampai = "))

angka = 0 
while True:
    angka += 1 
    print(f"count = {angka}")
    
    if angka == data_int:
        print("Cukup")
        break
    print("Akhir dari berhitung")
print("Akhir dari kode")