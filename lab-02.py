# DDP LAB-2
print("===SOAL 1===")
print("Mencetak bilangan")
# SOAL 1 - Mencetak bilangan
# Tuliskan program untuk Soal 1 di bawah ini
#Proses looping for dengan range lanjutan dimulai dari satu hingga 2 dengan pengurangan -2
for i in range(100, 0, -2):
#mencetak hasil perulangan
   print(i, end=",")

print( )
print( )
print("===Soal 2===")
print("Menghitung rata-rata")
# SOAL 2 - Menghitung rata-rata
# Tuliskan program untuk Soal 2 di bawah ini
# Menginput angka yang akan dihitung
x = int(input("Masukkan banyaknya angka : "))
#inisial jumlah x
total=0
# Proses looping for, dengan range sebanyak x 
for i in range(x) :
#i dimulai dari 1
    i = i + 1
#proses input nilai
    y = eval(input("Masukkan sebuah bilangan : "))
# proses penjumlahan nilai input dengan total
    total = total+y
#mencetak hasil total
print("Jumlah dari bilangan tersebut adalah :", total)
#Menghitung rata-rata dari bilangan tersebut
print("Nilai rata-rata dari bilangan tersebut adalah", total/x)
print( )

print( )
# SOAL 3 - Mencetak persegi
# Tuliskan program untuk Soal 3 di bawah ini
print("===SOAL 3===")
print("Membuat persegi")
#memasukkan pengulangan baris sebanyak 6
for i in range(6) :
#memasukkan pengulangan kolom sebanyak 6
    for j in range(6):
        print("$", end=" ")
    print( )

print( )
print( )
print("===SOAL 3===")
#memasukkan panjang sisi
s = int(input("Masukkan sebuah angka : "))
#Proses pengulangan dengan range sebanyak s
for i in range(s):
#mencetak hasil dengan # dikali panjang sisi yang diinput
    print('#'*s, sep=" ")







# SOAL 3 - Mencetak persegi
# Tuliskan program untuk Soal 3 di bawah ini
#print("===SOAL 3===")
for i in range(6) :
    for j in range(6):
        print("$", end=" ")
    print( )
