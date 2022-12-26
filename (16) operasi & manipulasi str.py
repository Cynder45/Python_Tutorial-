# operasi dan manipulasi string 

#  1 . menyammbunng string (Concatenate)
nama_pertama = "ucup"
nama_tengah  = "D"
nama_akhir   = "Udin"
nama_lengkap = nama_pertama + nama_tengah + nama_akhir
print(nama_lengkap)
nama_lengkap = nama_pertama + " " + nama_tengah + " ' " + nama_akhir
print(nama_lengkap)

nama_pertama = nama_pertama + " " + nama_tengah + " ' " + nama_akhir
print(nama_pertama)

# 2. menghitung panjang string 
panjang = len(nama_lengkap) #spasi dihitung 
print("panjang dari" + nama_lengkap + "=" + str(panjang))

# 3. operator untuk string 
#mengecek apakah adanya komponen char atau string di string 

d = 'd'
status = d in nama_lengkap
print('apakah adanya huruf d, dalam nama lengkap',status)

D = "D"
status = D in nama_lengkap
print('apakah adanya huruf D, dalam nama lengkap',status)

a = "a"
status = a not in nama_lengkap
print('apakah adanya huruf a, dalam nama lengkap',status)

# Mengulang string 
print("WK"*10)
print(15*"wk")

# Indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-1 : " + nama_lengkap[1])
print("index ke-2 : " + nama_lengkap[2])
print("index ke-3 : " + nama_lengkap[3])
print("index ke-4 : " + nama_lengkap[4])
print("index ke-(-1): " + nama_lengkap[-1]) #minus ambil dari belakang

# Indexing (mengambil range)
print("index ke-[0:4] : " + nama_lengkap[0:4])
print("index ke-[3:8] : " + nama_lengkap[3:8])
print("index ke-[0,2,8,10] : " + nama_lengkap[0:11:2])

# item paling kecil 
print("paling kecil : ", min(nama_lengkap))
# item paling besar
print("paling kecil : ", max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII Code untuk spasi adalah ", str(ascii_code))
data = 117
print(" char untuk ascii 117 adalah ", chr(data))
ascii_code = ord("'")
print("ASCII Code untuk kutip adalah ", str(ascii_code))

# 4. operator dalam bentuk meethod
data = "ular pagar helikopter"
jumlah = data.count("r")
print("jumlah r pada data : ", str(jumlah))
data = "ular pagar helikopter"
jumlah = data.count("a")
print("jumlah a pada data : ", str(jumlah))


