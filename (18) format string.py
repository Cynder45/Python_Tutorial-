# format string 

# contoh generic 
#string
nama = "Rendy"
str = "hello" + nama 
print(str)

nama = "Doni"
format_str = f"hello {nama}"
print(format_str)

# Boolean 
boolean = True 
format_str = f"boolean = {boolean}"
print(format_str)

boolean = False 
format_str = f"boolean = {boolean}"
print(format_str)

# angka
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat 
angka = 15 
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan ribuan 
angka = 2000
format_str = f"ribuan =  {angka:,}"
print(format_str)

# bilangan ordo ribuan 
angka = 2000000
format_str = f"ribuan =  {angka:,}"
print(format_str)

# bilangan desimal 
angka = 200.54321
format_str = f"desimal = {angka:.2f}" #2f untuk 2 angka diblkng koma 
print(format_str)
angka = 200.54321
format_str = f"desimal = {angka:.4f}" #2f untuk 4 angka diblkng koma 
print(format_str)

# menampilkan leading zero 
angka = 200.54321
format_str = f"desimal = {angka:8.2f}" #
print(format_str)
angka = 200.54321
format_str = f"desimal = {angka:08.2f}" #
print(format_str)

# menampilkan tanda + / - 
angka_minus = -10 
angka_plus = 10 
format_minus = f"minus = {angka_minus:+d}" # :+d -> untuk mengeluarkan tandanya
format_plus = f"plus = {angka_plus:+d}"
print(format_minus)
print(format_plus)

# memformat persen 
presentase = 0.045 
format_persen = f"persen = {presentase:.2%}" #.2 untuk belakang koma ada berapa
print(format_persen)

# melakukan operasi aritmatika di dalam place holder 
harga = 100000
jumlah  = 5 
format_str = f"harga total = Rp {harga*jumlah:,}"
print(format_str)

# format angka lain (binary, octal, hexadecimal)
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)

