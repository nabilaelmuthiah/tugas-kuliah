# SOAL 1 - Menghitung rata-rata
# Tuliskan program untuk Soal 1 di bawah ini
print("===SOAL===")
print("average suatu bilangan")
a =  eval(input("Masukkan bilangan pertama : "))
b = eval(input("Masukkan bilangan kedua : "))
c = eval(input("Masukkan bilangan ketiga : "))
print("berapakah rata-ratanya?")
average=( a+b+c ) / 3
print("hasil", "dari", "rata-rata", "bilangan", a,b,c, "adalah", average)
# SOAL 2 - Menulis kelipatan bilangan
# Tuliskan program untuk Soal 2 di bawah ini
print("===SOAL 2===")
print("Kelipatan suatu bilangan")
x = int(input("Masukkan bilangan bulat : "))
for x in range(0, 50, x) :
   print( x, " ", sep="---", end=" ")
   #sumber belajar tambahan dari youtube : Kelas terbuka