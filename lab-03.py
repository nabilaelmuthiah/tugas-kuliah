# DDP LAB-3

# SOAL 1 - Gunting-Batu-Kertas
# Tuliskan program untuk Soal 1 di bawah ini
print("---SOAL 1---")
print("Gunting, Batu, Kertas!")
print(" ")

#player 1 memasukkan pilihan
player1 = input("Player 1 memasukkan pilihan gunting, batu, atau kertas :")
#player2 memasukkan pilihan
player2 = input("Player 2 memasukkan pilihan gunting, batu atau kertas :")
# kondisi jika pilihan kedua player sama
if (player1 == player2):
#maka hasil yang dicetak adalah seri
  print('pertandingan seri')
# kondisi jika player1 memilih gunting
elif player1 == "gunting" :
  if player2 == "kertas" :
    print("Player 1 menang!")
  elif player2 == "batu" :
    print("Player 2 menang!")
# kondisi jika player1 memilih batu
elif player1 == "batu" :
  if player2 == "kertas" :
    print("Player 2 menang!")
  if player2 == "gunting" :
    print("Player 1 Menang!")
#kondisi jika player 1 memilih kertas
elif player1 == "kertas" :
  if player2 == "gunting" :
    print("Player 2 Menang!")
  if player2 == "batu" :
    print("Player 1 Menang!")
# kondisi lain jika player memasukkan pilihan terdapat typo
else :
  print("Silakan masukkan kembali karakter dengan benar.")

print("pertandingan selesai")
print( )
print( )

# SOAL 2 - Toko Buku Bekas
# Tuliskan program untuk Soal 2 di bawah ini
print("---SOAL 2---")
print("Toko Buku Bekas")
print(" ")

# menginput jumlah buku yang akan dibeli
buku = eval(input('masukan jumlah buku yang mau dibeli : '))
# kondisi jika buku yang dibeli  kurang dari atau sama dengan 10 maka harga buku 20000
if (buku <= 10):
  harga = 20000
  total_harga = buku * harga
# kondisi jika buku yang dibeli  kurang dari atau sama dengan 25 maka harga buku 18000
elif (buku <= 25):
  harga = 18000
  total_harga = buku * harga
# kondisi jika buku yang dibeli  kurang dari atau sama dengan 5 maka harga buku 15000
elif (buku <= 50):
  harga = 15000
  total_harga = buku* harga
# kondisi jika buku yang dibeli  lebih dari atau sama dengan 10 maka harga buku 20000
elif (buku >= 50):
  harga = 10000
  total_harga = buku*harga
#mencetak total_harga buku dari perhitungan total_harga = buku*harga
print('total_harga buku = ', total_harga, "rupiah")
print( )
print( )

# SOAL 3 - Mencetak Persegi
# Tuliskan program untuk Soal 3 di bawah ini
print("---SOAL 3---")
print("Mencetak persegi")
print(" ")

persegi = int(input("Masukkan sebuah bilangan : "))
for i in range(1, persegi) :
  if (i % 2) :
    print(" # " * persegi )
  else :
    print(" $ " * persegi )
