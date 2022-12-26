# width and multiline 

#data
data_nama = "Cynder Ndy"
data_umur = 17
data_tinggi = 180.3
data_nomor_sepatu = 44 

#string 
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}"
print("="*5,"Data String","="*5)
print(data_string)

#String Multiline
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_nomor_sepatu}"
print("="*5,"Data String Multiline","="*5)
print(data_string)

#String Multiline Triplets(""" """)
data_string = f"""nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print("="*3,"Data String Multiline Triplets","="*3)
print(data_string)

#mengatur lebar
data_nama = "Cynder"
data_string = f"""
nama   = {data_nama}
nama   = {data_nama:>7} # :> untuk ngatur lebar
umur   = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print("="*3,"Mengatur lebar","="*3)
print(data_string)

