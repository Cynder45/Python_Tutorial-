#operasi aritmatika 
from traceback import print_tb


a = 10
b = 3 

# operasi pertambahan (+)
hasil = a+b
print(a,'+',b, '=',hasil)

# operasi pengurangan (-)
hasil = a-b
print(a,'-',b,'=', hasil)

# operasi perkalian (*)
hasil = a*b
print(a,'*',b,'=',hasil)

# operasi pembagian (/)
hasil = a/b
print(a,'/',b,'=', hasil)

# operasi eksponen / pangkat (**)
hasil = a**b
print(a,'**',b,'=',hasil)

# operasi modulus / sisa pembagian (%)
hasil = a%b
print(a,'%',b,'=',hasil)

# operasi floor division (//)
hasil = a//b
print(a,'//',b,'=',hasil)

#prioritas operasi, operational precedence
x = 3 
y = 2 
z = 4 
hasil = x ** y * z + x / y - y % z // x
print(x, '**' ,y ,'*', z, '+' ,x, '/' ,y ,'-', y, '%' ,z, '//', x,'=' , hasil)

#prioritas operasi 
# ()
# eksponen 
# perkalian 
# pertambahan
hasil = x + y * z
print(x,'+',y,'*',z,'=', hasil)