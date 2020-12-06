# Nama: Nabila ElMuthi'ah
# NIM: 0110120172
# Kelas: Sistem Informasi-01

#mendefinisikan fungsi
def jumlah_batas(nums, batas):
  #memasukkan jumlah karakter nums ke dalam variabel a
  a = len(nums)
  #inisialisasi jumlah dengan 0
  jumlah = 0
  #melakukan looping i selama range sama dengan variabel a
  for i in range(a) :
    #kondisi jika indeks nums lebih dari batas
    if (nums[i] > batas) :
      #memasukkan variabel total dari keseluruhan indeks nums
      total = nums[i]
      #decrement
      jumlah += total
    #kondisi lain dari kondisi di atas
    else :
      #program akan mengecek program berjalan atau tidak 
      pass
  return jumlah 
    #pass

#mendefinisikan fungsi
def list_nonvokal(s):
  #memasukkan panjang karakter string s ke dalam variabel pjg
  pjg = len(s)
  r = []
  #list huruf vokal dalam variabel vokal
  vokal = ["A","I", "U", "E", "O", "a", "i", "u", "e", "o"]
  #looping n selama range sama dengan pjg
  for n in range(pjg) :
    #kondisi jika string s dengan indeks n tidak ada di vokal
    if s[n] not in vokal :
     #decerement
     r += s[n]
  return r 
    #pass

#mendefinisikan fungsi
def list_modify(alist, command, position, value=None):
   #kondisi seperti di deskripsi soal no.3 luaran 3.4
    if command == "remove" and position == "end" :
      #mendelete item list pada indeks terakhir atau -1
      del alist[-1]
    #kondisi lain seperti di deskripsi soal no.3 luaran 3.3
    elif command == "remove" and position == "start" :
      #mendelete item list pada indeks pertama atau indeks 0
      del alist[0]
    #kondisi lain seperti di deskripsi soal no.3 luaran 3.2
    elif command == "add" and position == "end" :
      #menambahkan item list pada posisi akhir list
      alist.append(value)
    ##kondisi lain seperti di deskripsi soal no.3 luaran 3.1
    elif command == "add" and position == "start" :
      #menambahkan item lisr pada posisi pertama atau indeks 0
      alist.insert(0, value)
    #mengembalikan nilai alist
    return alist
    #pass

#Sumber : clue kak Fauzi untuk no.1 dan 2.
#         no.3 coba-coba dari terjemahan yang di deskripsi soal dan web petanikode.com

# Mulai baris ini hingga baris paling bawah
# digunakan untuk mengetes fungsi yang telah dibuat.
# Tidak perlu mengubah bagian ini.
# Ketika dijalankan, program akan menampilkan contoh
# pemanggilan fungsi dan solusi yang seharusnya.
# Cocokkan hasil pemanggilan fungsi dengan solusi
# yang seharusnya.
def test():
    r = jumlah_batas([8, 7, 6, 10, 1], 5)
    print(f"jumlah_batas([8, 7, 6, 10, 1], 5) = {r} \n(solusi: 31)")
    print()
    r = jumlah_batas([1, -7, -10, 1], -5)
    print(f"jumlah_batas([1, -7, -10, 1], -5) = {r} \n(solusi: 2)")
    print()
    r = list_nonvokal('Halo')
    print(f"list_nonvokal('Halo') = {r} \n(solusi: ['H', 'l'])")
    print()
    r = list_nonvokal('AAAAAooooo')
    print(f"list_nonvokal('AAAAAooooo') = {r} \n(solusi: [])")
    print()
    r = list_nonvokal('Saya cinta programming')
    print(
        f"list_nonvokal('Saya cinta programming') = {r} \n(solusi: ['S', 'y', ' ', 'c', 'n', 't', ' ', 'p', 'r', 'g', 'r', 'm', 'm', 'n', 'g'])"
    )
    print()
    r = list_modify(['ayam', 'ikan', 'kucing'], 'add', 'start', 'bebek')
    print(
        f"list_modify(['ayam', 'ikan', 'kucing'], 'add', 'start', 'bebek') = {r} \n(solusi: ['bebek', 'ayam', 'ikan', 'kucing'])"
    )
    print()
    r = list_modify(['ayam', 'ikan', 'kucing'], 'add', 'end', 'bebek')
    print(
        f"list_modify(['ayam', 'ikan', 'kucing'], 'add', 'end', 'bebek') = {r} \n(solusi: ['ayam', 'ikan', 'kucing', 'bebek'])"
    )
    print()
    r = list_modify(['ayam', 'ikan', 'kucing'], 'remove', 'start')
    print(
        f"list_modify(['ayam', 'ikan', 'kucing'], 'remove', 'start') = {r} \n(solusi: ['ikan', 'kucing'])"
    )
    print()
    r = list_modify(['ayam', 'ikan', 'kucing'], 'remove', 'end')
    print(
        f"list_modify(['ayam', 'ikan', 'kucing'], 'remove', 'end') = {r} \n(solusi: ['ayam', 'ikan'])"
    )
    print()


if __name__ == '__main__':
    test()
 