# nama file : import.py
# mengimport modul geometri2D
from matematika import geometri2D

# persegi panjang
p = 10
l = 8

luas = geometri2D.luaspersegipanjang(10, 8)
kel = geometri2D.kelilingpersegipanjang(10, 8)

print("PERSEGI PANJANG")
print("panjang: ", p)
print("lebar: ", l)
print("luas: ", luas)
print("keliling: ", kel)

# lingkaran
jarijari = 3
luas = geometri2D.luaslingkaran(3)
kel = geometri2D.kelilinglingkaran(3)

print("LINGKARAN")
print("jari-jari: ", jarijari)
print("luas: ", luas)
print("keliling: ", kel)