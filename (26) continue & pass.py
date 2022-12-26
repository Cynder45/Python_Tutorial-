#continue, pass, break 

# pass => berfungsi sebagai dummy, tidak akan dieksekusi

angka = 0 
while angka < 5:
    angka +=1 
    if angka == 3:
        pass # tidak akan dieksekusi 
    print(angka)

angka = 0 
while angka < 5:
    angka +=1 
    if angka == 3:
        print("hai")
    print(angka)


# Continue 
print("="*5,"CONTINUE","="*5)
angka = 0 
print(f"angka sekarang -> {angka}")
while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}")
    if angka == 3:
        print("cukup")
        continue #loop loncat ke step selanjutnya (Hai hilang di ganti cukup)
    print("Hai")
print("Nice")