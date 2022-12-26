#latihan komparasi dan logika 
# gabungan area rentang dari sebuah angka
"""
# ++++++++3--------10+++++++
InputUser = float(input("masukan angka yang bernilai\n kurang dari 3\natau\n lebih besar dari 10\n :"))
#+++++++3--------
# Memeriksa angka kurang dari 3 
IsKurangDari = (InputUser < 3)
print('kurang dari 3 = ', IsKurangDari)

#--------10+++++++
# Memeriksa angka lebih dari 10 
IsLebihDari = (InputUser > 10)
print('Lebih dari 10 = '
, IsLebihDari) 


#++++3------10+++++++
isCorrect = IsKurangDari or IsLebihDari
print ('angka yang anda masukan = ' , isCorrect)

#-------3+++++++10---------
#kasus irisan 
print("\n", 10*"=", "\n")
InputUser = float(input("masukan angka yang bernilai\n lebih dari 3\natau\n kurang dari 10\n :"))


#--------3+++++++++
IsLebihDari = InputUser > 3

print("Lebih dari 3 = ", IsLebihDari)


#++++++++10-------
IsKurangDari = InputUser < 10 
print ('kurang dari 10 = ' , IsKurangDari)


#-------3+++++++10---------
isCorrect = IsKurangDari and IsLebihDari
print ('angka yang anda masukan = ' , isCorrect)
"""

#Tugas Mandiri 
print("\n", 10*"=", "\n")
print("Tugas Mandiri")
print("\n", 10*"=", "\n")


#-----0+++++5-----8+++++11-----
InputUser = float(input("masukan angka yang > 0  , < 5 dan > 8 , < 11 : " ))

#memeriksa angka > 0 
IsLebihDari = InputUser > 0 
print (" Angka lebih dari 0 = ", IsLebihDari )

#memeriksa angka < 5
IsKurangDari = InputUser < 5 
print ("Angka kurang dari 5 = ", IsKurangDari)

#memeriksa angka > 8 
IsLebihDari = InputUser > 8 
print("Angka leih dari 8 = ", IsLebihDari)

#memeriksa angka < 11
IsKurangDari = InputUser < 11 
print("Angka kurang dari 11 = ", IsKurangDari)

#-----0+++++5-----8+++++11-----
InputUser = float(input("masukan angka Between 0 - 5 dan 8-11 \n :"))
A = (InputUser > 0)
B = (InputUser < 5)
C = (InputUser > 8)
D = (InputUser < 11)
Hasilnilai = (A and B) or (C and D)
print("Hasil=",Hasilnilai)

#+++++0-----5+++++8-----11+++++