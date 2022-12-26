# tipe data : Angka satuan (integer)
data_integer = 1 
print(type(data_integer))
print("data : ", data_integer)
print(" - bertipe : ", type(data_integer))

# tipe data : Angka koma (float)
data_float = 1.5
print("data : ", data_float)
print(" - bertipe : ", type(data_float))

# tipe data : Kumpulan karakter (string)
data_string = "pipi"
print("data : ", data_string)
print(" - bertipe : ", type(data_string))

# tipe data : biner true/false (boolean)
data_boolean = True
print("data : ", data_boolean)
print(" - bertipe : ", type(data_boolean))

## tipe data khusus 

# data kompleks
data_complex = complex (5,6)
print("data : ", data_complex)
print("bertipe : ", type(data_complex))

# tipe data dari bahasa C 
from ctypes import c_double

data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("bertipe : ", type(data_c_double))

