from dataclasses import dataclass


data = "ini adalah string"
print(data)
print(type(data))

#1. cara membuat string 
'''
    1. dengan menggunakan single quote '____'
    2. dengan menggunakan double quote "______"
'''
data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')

# 2. Menggunakan tanda \ 
# membuat tanda ' menjadi string 
print('Mari keluar di hari jum\'at')
print('g\'day, isnt\'t it ?')

#backslash 
print("C:\\user\\Ucup")

# tab 
print("Ucup\tlagi\tmakan") #jauhan 

# backspace 
print("Ucup \blagi \bmakan") #deketan 

# newline
print("baris pertama \nbaris kedua") # LF --> Line feed --> Unix, macos
print("baris pertama\rbaris kedua") # CR --> Carriage return --> commodore, acorn, lisp
print("baris pertama\r\nbaris kedua") # CRLF --> line feed carriage return --> Windows

# string literal atau raw 

#hati - hati 
print('C:\new folder') # akan salah pathnya
print('C:\\new folder') # akan benar pathnya

# menggunakan raw string 
print(r'C:\new folder')

# multiline literal string 
print('''
Nama  : Ucup 
Kelas : 3 SD
''')

# multiline literal string dan raw 
print(r'''
Nama  : Ucup 
Kelas : 3 SD
Website : WWW.Ucup.Com\newID
''')
