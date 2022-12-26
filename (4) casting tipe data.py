# merubah dari 1 tipe ke tipe yang lain 
# tipe data : Integer, Float, String, Boolean 
from operator import truediv


print("==INTEGER==")
data_int = 1
print("data = ", data_int,", type = ",type(data_int))

data_float = float(data_int)
data_str =str(data_int)
data_bool = bool(data_int) #akan false jika nilai int = 0 

print("data = ", data_float,", type = ",type(data_float))
print("data = ", data_str,", type = ",type(data_str))
print("data = ", data_bool,", type = ",type (data_bool))

#FLOAT
print("==FLOAT==")
data_float = 2.5
data_int = int(data_float) #akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float)
print("data = ", data_float,", type = ",type(data_float))
print("data = ", data_str,", type = ",type(data_str))
print("data = ", data_bool,", type = ",type (data_bool))
print("data = ", data_int, "type = ", type(data_int))


#Boolean 
print("==Boolean==")
data_boolean = True
data_int = int(data_boolean) 
data_str = str(data_boolean)
data_float = float(data_boolean)
print("data = ", data_boolean,", type = ",type (data_boolean))
print("data = ", data_float,", type = ",type(data_float))
print("data = ", data_str,", type = ",type(data_str))
print("data = ", data_int, "type = ", type(data_int))

#String
print("==String==")
data_str = "pipi"
#data_int = int(data_str) #String harus berupa angka
data_bool = bool(data_str) #False jika string kosong
#data_float = float(data_str) #String harus berupa angka
print("data = ", data_str,", type = ",type (data_str))
#print("data = ", data_float,", type = ",type(data_float))
print("data = ", data_bool,", type = ",type(data_bool))
#print("data = ", data_int, "type = ", type(data_int))

#String2
print("==String2==")
data_str = ""
#data_int = int(data_str) #String harus berupa angka
data_bool = bool(data_str) #False jika string kosong
#data_float = float(data_str) #String harus berupa angka
print("data = ", data_str,", type = ",type (data_str))
#print("data = ", data_float,", type = ",type(data_float))
print("data = ", data_bool,", type = ",type(data_bool))
#print("data = ", data_int, "type = ", type(data_int))

#String3
print("==String3==")
data_str = "10"
data_int = int(data_str) #String harus berupa angka
data_bool = bool(data_str) #False jika string kosong
data_float = float(data_str) #String harus berupa angka
print("data = ", data_str,", type = ",type (data_str))
print("data = ", data_float,", type = ",type(data_float))
print("data = ", data_bool,", type = ",type(data_bool))
print("data = ", data_int, "type = ", type(data_int))