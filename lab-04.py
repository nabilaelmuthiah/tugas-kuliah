# DDP LAB-4
# Nama: <Tulis nama di sini>
# NIM: <Tulis NIM di sini>
print("DDP LAB-04")
print("Nama : Nabila ElMuthi'ah")
print("NIM : 0110120172")
# SOAL 1 - Mencetak nama
# Tuliskan program untuk Soal 1 di bawah ini
print( )
print(" SOAL NO 1 ")
print("=== Mencetak Nama ===")
print( )

#variabel global
nama = input("Masukkan Nama Anda : ")
panjang = len(nama)
#inisialisasi untuk variabel perulangan n bernilai 0
n = 0
#kondisi dimana bernilai true or false jika n kurang dari atau sama dengan panjang maka statement akan terus dicetak
while n <= panjang :
  #mencetak string dengan fungsi slicing 
  print(nama [0:n])
  #pengubah variabel agar mengarah ke kondisi false dengan increment
  n = n + 1
print( )

# SOAL 2 - Validasi teks
# Tuliskan program untuk Soal 2 di bawah ini
print(" SOAL NO 2 ")
print("=== Validasi Teks ===")
print( )

while True :
  #penginputan teks ke variabel
  N = input("Masukkan sebuah Teks : ")
  #menghitung panjang string teks
  panjang = len(N)
  #kondisi true sesuai dengan kriteria
  if (panjang >= 8 and (N.endswith("yyy") or N.endswith("YYY"))and (("NF" in N) or ("nf" in N) or ("Nf" in N) or ("nF" in N)) and not N.isalpha()) : 
    #program mencetak hasil teks yang dimasukkan valid
    print("Text valid, Program berhenti. Selamat Datang!")
    #jika kondisi true maka akan break atau berhenti lalu lanjut ke program di line 48
    break
  #kondisi lain atau bernilai false
  else :
    #program mencetak teks tidak valid karena tidak sesuai kriteria
    print("Text tidak valid, silahkan coba lagi.")  
print(" Terima Kasih ")
# sumber dari siapa.. Tulis disini aja 
# sumber : youtube + Kak Fauzi