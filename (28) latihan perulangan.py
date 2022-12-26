#menggunakana for  
"""print("="*5)
j = 1 #dummy var
for i in range(6):
    print("*"*j)
    j += 1

# menggunakan while 
print("="*5)
j = 1
while True: 
    print("*"*j)
    j += 1 
    if j > 6:
        break

# hanya ganjil saja 
print("="*5)
j = 1
while True: 
    if j%2:
        print("*"*j)
        j += 1 
    else:
        # Print jika ganjil 
        j += 1 
        continue
    # akan break juka j melebihi 10
    if j > 10:
        break
  """
#latihan 
sisi = 10 
hitung = 1
spasi = int(sisi/2)
while True:
    if hitung%2:
        print(" "*spasi,"*"*hitung)
        hitung += 1
        spasi -= 1
    else: 
        hitung += 1 
        continue 
    if hitung > sisi: 
        break 

# tugas 
print("="*10)
while True: 
    if hitung%2:
        spasi += 1
        print(" "*spasi, "*"*hitung)
        hitung -= 1    
    else: 
        hitung -= 1
        continue 
    if hitung == 0: 
        break