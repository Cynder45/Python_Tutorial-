#date and time latihan)
import datetime as dt
hari_ini = dt.date.today()
print(hari_ini)
"""
#print berdasarkan hari 
hari_lahir = dt.date(2005,11,4)
print(f"Hari lahir saya = {hari_lahir:%A}") 

#pendeteksi hari lahir 
print("Masukan tanggal lahir kalian")
tanggal = int(input("Tanggal = "))
bulan   = int(input("Bulan   = "))
tahun   = int(input("Tahun   = "))
tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir anda adalah = {tanggal_lahir}")
print(f"Hari lahir anda adalah    = {tanggal_lahir:%A}")

hari_ini = dt.date.today()
umur_hari = hari_ini - tanggal_lahir 
umur_tahun = umur_hari / 365
print("Umur anda adalah " , umur_hari)
"""
# pendeteksi tahun kelahiran, dan umur 
print("Masukan tanggal lahir kalian")
tanggal = int(input("Tanggal = "))
bulan   = int(input("Bulan   = "))
tahun   = int(input("Tahun   = "))
tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir anda adalah = {tanggal_lahir}")
print(f"Hari lahir anda adalah    = {tanggal_lahir:%A}")

hari_ini = dt.date.today()
umur_hari = hari_ini - tanggal_lahir 
umur_tahun = umur_hari.days // 365
print("Umur anda adalah " , umur_tahun,"tahun")
