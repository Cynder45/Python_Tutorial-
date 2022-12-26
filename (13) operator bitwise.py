#operasi biner, bitwise (Operasi masing masing bit)
from re import A


a = 9 
b = 5 

# bitwise or (|)
c = a | b
print('\n' ,5*'=', 'or', 5*'=' )
print('nilai : ', a , ', binary : ', format (a,'08b') )
print('nilai : ', b , ', binary : ', format (b,'08b') )
print('-------------(|)')
print('nilai : ', c , ', binary : ', format (c,'08b') )

# bitwise AND (&)
c = a & b 
print('\n' ,5*'=', 'AND', 5*'=' )
print('nilai : ', a , ', binary : ', format (a,'08b') )
print('nilai : ', b , ', binary : ', format (b,'08b') )
print('-------------(|)')
print('nilai : ', c , ', binary : ', format (c,'08b') )

# bitwise XOR (^)
c = a^b 
print('\n' ,5*'=', 'XOR', 5*'=' )
print('nilai : ', a , ', binary : ', format (a,'08b') )
print('nilai : ', b , ', binary : ', format (b,'08b') )
print('-------------(|)')
print('nilai : ', c , ', binary : ', format (c,'08b') )

# bitwise NOT (~)
c = ~a 
print('\n' ,5*'=', 'NOT', 5*'=' )
print('nilai : ', c , ', binary : ', format (c,'08b') )

# operasi bitwise 
# OR
c = True
print('\n' ,5*'=', 'Bitwise OR', 5*'=' )
c |= False
print("nilai c |= False, nilai c menjadi ", c )
c = False
print("nilai c = ", c )
c |= False
print("nilai c |= False, nilai c menjadi ", c )

# Operasi bitwise 
# AND
c = True
print('\n' ,5*'=', 'Bitwise AND', 5*'=' )
c &= False
print("nilai c &= False, nilai c menjadi ", c )
c = False
print("nilai c = ", c )
c &= False
print("nilai c &= False, nilai c menjadi ", c )

#geser geser 
d = 0b0100
print("\nnilai d =",format(d,"04b"))
d >>= 2 
print("\nnilai d >>= 2, nilai d menjadi ",format(d,"04b"))
d <<= 2 
print("\nnilai d <<= 1, nilai d menjadi ",format(d,"04b"))
