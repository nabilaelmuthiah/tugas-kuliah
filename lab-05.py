print("DDP LAB-04")
print("Nama : Nabila ElMuthi'ah")
print("NIM : 0110120172")
print( )

#mendefinisikan fungsi
def cetak_nama(nama=''):
  #membuat suatu kondisi jika nama kosong
  if nama == '':
    print("Tidak ada nama yang dicetak.")
  #kondisi jika suatu nama ada
  else:
    #proses loping dengan range panjang nama
    for i in range(0,len(nama)):
      i = i + 1
      #mencetak fungsi slicing
      print(nama [0:i])
    #mencetak nama ditambah sebuah tanda seru   
    print(nama,'!')

  #pass

def hitung_kesamaan(kata1, kata2):
  #membuat variabel a untuk menjumlah karakter yang ada di kata1
  a = len(kata1)
  #membuat variabel b untuk menjumlah karakter yang ada di kata2
  b = len(kata2)
  #untuk angka awal saat proses looping
  r = 0
  #kondisi jika jumlah karakter kata1 lebih dari kata2
  if (a > b) :
    #fungsi looping untuk membandingkan setiap karakter pada kata1 dan kata2
    for i in range(b) :
      z = kata1[i]
      y = kata2[i]
      #jika kata1 dan kata2 sama
      if z == y :
        r += 1
      #mengembalikan hasil akhir loopingan
    return r
  #fungsi looping untuk membandingkan setiap karakter pada kata1 dan kata2
  else :
    #proses looping 
    for i in range (a) :
      z = kata1[i]
      y = kata2[i]
      #jika kata1 dan kata2 sama
      if z == y :
        r += 1
    #mengembalikan hasil akhir looping
    return r
  #pass

def hitung(bil1, bil2, operator="+"):
  #sebuah kondisi jika operator bernilai +
  if operator == "+" :
    #maka kedua bilangan dijumlah
    r = bil1 + bil2
    #fungsi disimpan untuk dikembalikan lagi nanti
  #jika kondisi berbeda atau jika operator bernilai minus
  elif operator == "-" :
  #maka kedua bilangan dikurang
    r = bil1 - bil2
  #kondisi jika operator bernilai *
  elif operator == "*" :
  #kedua bilangan di kali
    r = bil1 * bil2
  #kondisi jika operator bernilai /
  elif operator == "/" :
  #kedua bilangan di bagi
    r = bil1 / bil2
  #jika kondisi berbeda, 
  return r
  


 #sumber : Kak Fauzi dan diajari teman saya
  #pass



# Mulai baris ini hingga baris paling bawah
# digunakan untuk mengetes fungsi yang telah dibuat.
# Tidak perlu mengubah bagian ini.
# Ketika dijalankan, program akan menampilkan contoh
# pemanggilan fungsi dan solusi yang seharusnya
# (untuk fungsi hitung_kesamaan() dan fungsi hitung()).
# Cocokkan hasil pemanggilan fungsi dengan solusi  
# yang seharusnya.
def test():
  print("Hasil cetak_nama('Nabila'):")
  cetak_nama("Nabila")
  print()
  print("Hasil cetak_nama(''):")
  cetak_nama("")
  print()
  r = hitung_kesamaan('python', 'path')
  print(f"hitung_kesamaan('python', 'path') = {r} \t(solusi: 3)")
  r = hitung_kesamaan('masak', 'cuci')
  print(f"hitung_kesamaan('masak', 'cuci') = {r} \t(solusi: 0)")
  r = hitung_kesamaan('python', '')
  print(f"hitung_kesamaan('python', '') = {r} \t\t(solusi: 0)")
  print()
  a = hitung(4, 8)
  print(f'hitung(4, 8) = {a} \t\t(solusi: 12)')
  b = hitung(4, 8, '-')
  print(f"hitung(4, 8, '-') = {b} \t(solusi: -4)")
  c = hitung(4, 8, '*')
  print(f"hitung(4, 8, '*') = {c} \t(solusi: 32)")

if __name__ == '__main__':
  test()