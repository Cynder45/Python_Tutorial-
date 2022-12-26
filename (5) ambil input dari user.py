# Input user

#data yang dimasukan pasti string
data = input("Masukan data : ")
print("data : ", data, "Type : ", type(data))

#jika ingin mengambil data integer 
data_int =  int (input("Masukan angka : "))
print("data : ", data_int ,"Type :",type(data_int))

#jika ingin mengambil data float
data_float = float(input("Masukan desimal : "))
print("data :", data_float, "Type : ",type(data_float) )

#jika boolean
data_bool = bool(int((input("Masukan bool : "))))
print("data :", data_bool, "Type : ",type(data_bool) )
