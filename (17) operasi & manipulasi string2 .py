#operasi dalam bentuk methods 

## merubah case dari string 

#merubah semua ke uppercase 
salam = "hi bro!"
print("normal text = ", salam)
salam = salam.upper()
print("uppercase = ", salam)

#merubah semua ke lowercase 
salam = "Belalai Gajah PaNjang"
print('normal text = ', salam)
salam = salam.lower()
print('lowercase = ', salam)

#pengecekan dengan isX method 
# contoh pengecekan lowercase 
salam = 'hi sis!'
apakah_lower = salam.islower() #hasil boolean 
print(salam, 'is lower = ', str(apakah_lower))
apakah_upper = salam.isupper()
print(salam, 'is upper = ', str(apakah_upper))

#semua hasil dibwah ini hasilnya adalah boolean 
#isAlpha()--> untuk mengecek bahwa semuanya huruf 
#isAlnum() --> untuk mengecek angka dan numerik (pengecekan password)
#isDecimal() --> untuk mengecek semuanya angka
#isSpace() --> untuk mengecek string kosong ( ada spasi, new line \n)
#istitle() --> mengecek semua kata dimulai huruf besar 

# mengecek kata dimulai huruf besar 
judul = "Spiderman Home Coming"
cek_judul = judul.istitle() # untuk mengecek huruf kapital di awal dengan hasil boolean
print(judul, 'is title = ', str(cek_judul))

# untuk mengecek bahwa semuanya huruf 
huruf = "Berisi angka atau tidak 111111"
cek_huruf = huruf.istitle() # untuk mengecek bahwa stringnya berisi angka semua / tidak 
print(huruf, 'is title = ', str(cek_huruf))

#mengecek komponen startswith() endswith()
cek_start = "Korean Food With Micin".startswith("Korean")
print("start with = ", cek_start)
cek_end = "Korean Food With Micin".endswith("Micin")
print("end with = ", cek_end)

#penggabungan komponen join() dan split()
#join() -- > mengabungkan 
#split() --> memisahkan
# contoh join
pisah = ['I','love','my','self']
gabung = ','.join(pisah)
print("ini dipisah", pisah)
print("ini digabung", gabung)
# contoh tanpa koma
gabung = ' '.join(pisah)
print(gabung)
#contoh lainnya
gabung = '->'.join(pisah)
print(gabung)

gabungan = 'ILoveMySelf'
print(gabungan.split(' '))

#alokasi karakter rjust(), ljust(), center()
print(5*'=', 'data',5*'=')
kata_kanan = 'kanan'.rjust(15)
print(",",kata_kanan,",")
#kiri
kata_kiri = 'kiri'.ljust(15)
print(',',kata_kiri,',')
#tengah 
kata_tengah = 'tengah'.center(15,'-')
print(',',kata_tengah,',')

#kebalikannya, strip()
kata_tengah = kata_tengah.strip("-")#menghilangkan tanda - 
print(":",kata_tengah,":")



