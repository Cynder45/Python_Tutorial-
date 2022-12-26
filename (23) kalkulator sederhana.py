# latian kalkulator 

# masukan data user 
# cabangnya 
# hasil dan tampilannya 

print("="*5,"LATIHAN KALKU","="*5)
print("Latihan dibawah ini")

angka_pertama = float(input("Masukan angka berapapun : "))
operator = input("Masukan + - * ** / : ")
angka_kedua = float(input("Masukan angka berapapun : "))

# percabangannya 
if operator == "+":
    hasil = angka_pertama + angka_kedua
    print(f"Hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_pertama - angka_kedua
elif operator == "*":
    hasil = angka_pertama * angka_kedua
elif operator == "**":
    hasil = angka_pertama ** angka_kedua
elif operator == "/":
    hasil = angka_pertama / angka_kedua
elif operator == "//":
    hasil = angka_pertama // angka_kedua
print(f"Hasilnya adalah {hasil}")


