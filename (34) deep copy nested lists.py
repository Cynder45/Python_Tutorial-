data_0 = [1,2]
data_1 = [3,4]
data_2D = [data_0,data_1,10]
data_2D_copy = data_2D.copy()
print(f"data = {data_2D}")
print(f"data_copy = {data_2D_copy}")

#mengambil data dari nested list
data = data_2D [0]
print(f"data = {data}")

# mengambil angka depannya saja 
data = data_2D [0] [0]
print(f"data = {data}")

#Address semuanya 
print(f"address asli = {hex(id(data_2D))}")
print(f"address copy = {hex(id(data_2D_copy))}")

#mengambil adddress member ke-1 
print("Address member ke-1")
print(f"address asli = {hex(id(data_2D[0]))}")
print(f"address copy = {hex(id(data_2D_copy[0]))}")

data_2D[0][1] = 5
data_2D[2] = 9
print(f"address = {data_2D}")
print(f"address = {data_2D_copy}")

#deep copy 
 
from copy import deepcopy
data_2D = [data_0,data_1,10]
data_2D_deepcopy = deepcopy(data_2D)

print(f"address asli = {hex(id(data_2D))}")
print(f"address copy = {hex(id(data_2D_deepcopy))}")

print("Address member ke-1")
print(f"address asli = {hex(id(data_2D[0]))}")
print(f"address copy = {hex(id(data_2D_deepcopy[0]))}")


data_2D[1][0] = 30 
print(f"address = {data_2D}")
print(f"address = {data_2D_copy}")
print(f"address = {data_2D_deepcopy}")