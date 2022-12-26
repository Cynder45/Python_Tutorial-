# latihan konversi satuan temperature 
# program  konversi celcius ke satuan lain 

print("\n Program Konversi Satuan Temperature\n")
celcius = float(input('Masukan Suhu Dalam Celcius : '))
print("Suhu adalah ", celcius, "Celcius")

#Reamur 
# (4/5)C
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah ", reamur, "Reamur")

#Fahrenheit 
Fahrenheit = ((9/5)* celcius) + 32 
print("Suhu dalam fahrenheit adalah ", Fahrenheit, "Fahrenheit")

#Kelvin 
Kelvin = celcius + 273 
print("Suhu dalam kelvin adalah ", Kelvin, "Kelvin")


# Fahrenheit ke Kelvin 
Fahrenheit = float(input('Masukan suhu dalam Fahrenheit : '))
rumus = ((Fahrenheit - 32) * (5/9)) + 273.15
print("Suhu fahrenheit ke kelvin adalah  ",rumus, "Reamur")

# Kelvin ke Fahrenheit 
Kelvin = float(input('Masukan suhu dalam Kelvin : '))
rumus2 = (9/5)*(Kelvin - 273) + 32
print("Suhu dari Kelvin ke Fahrenheit adalah : ", rumus2 ,"Fahrenheit")