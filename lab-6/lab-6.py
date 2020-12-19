# Nama: Tri Siam Subekti
# NIM: 0110220086
# Kelas: TI 07

def jumlah_batas(nums, batas):
  # variable total dengan tipe data array sebagai menampung dari array lama ke array baru
  total = [] 
  # perulangan for loop dalam mengambil elemen di paramater nums yang berupa data array
  for i in range(len(nums)):
    # kondisi saat value nums jika lebih dari parameter batas
    if nums[i] > batas:
      # jika ditemukan ada value nums yang lebih dari batas maka value tersebeut akan di tambahkan di dalam data array total
      total.append(nums[i])
  
  # mengembalikan dengan menggunakan function sum untuk menambahkan elemen yanga ada di dalam variabel total
  return sum(total)

def list_nonvokal(s):
  # variabel hasi untuk menampung data array lama ke data array baru
  hasil = []
  # penrulangan for loop dalam mengambil elemen di parameter s yang berupa data string
  for index in range(len(s)):
      # variabel cekVokal kondisi untuk menemukan adakah value vokal 'a', 'i', 'u, 'e, 'o', 'A', 'I', 'U, 'E, 'O' ada di dalam parameter s
      cekVocal = 'aiueoAIUEO'
      # kondisi jika bukan di dalam variabel cekVokal
      if s[index] not in cekVocal:
          # maka variabel hasil yang di buatkan diatas tadi di tambahkan dengan vaue dari index parameter s
          hasil.append(s[index])
  # mengembalikan vaue variabel hasil dari fungsi list_nonvokal.
  return hasil

def list_modify(alist, command, position, value=None):
  # menetapkan nilai alist ke variabel baru tanpa mengubah isi dari data alist
  alist_new = alist[:]
  # kondisi jika ada command 'add' dan position 'start'
  if (command == 'add') and position == 'start':
      # variabel alist_new akan di tambahkan data dengan parameter value, dengan index ke 0 atau data pertama
      alist_new.insert(0, value)
      # mengembalikan data array baru yaitu variabel alist_new dari parameter alist_new
      return alist_new
  # kondisi jika ada command 'add' dan position 'end'
  elif (command == 'add') and position == 'end':
      # variabel alist_new akan di tambahkan data dengan parameter value, dengan index ke terakhir memakai function append
      alist_new.append(value)
      # mengembalikan data array baru yaitu variabel alist_new dari parameter alist_new
      return alist_new
  # kondisi jika ada command 'remove' dan position 'start'
  elif (command == 'remove') and position == 'start':
      # menghapus dengan function del dengan index ke 0 atau pertama
      del alist_new[0]
      # mengembalikan data array baru yaitu variabel alist_new dari parameter alist_new
      return alist_new
  # kondisi selain kondisi di atas maka hal terakhir yang dijalankan ada di else
  else:
      # menghapus dengan function del dengan index ke 0 atau pertama
      del alist_new[len(alist) - 1]
      # mengembalikan data array baru yaitu variabel alist_new dari parameter alist_new
      return alist_new





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
  print(f"list_nonvokal('Saya cinta programming') = {r} \n(solusi: ['S', 'y', ' ', 'c', 'n', 't', ' ', 'p', 'r', 'g', 'r', 'm', 'm', 'n', 'g'])")
  print()
  r = list_modify(['ayam', 'ikan', 'kucing'], 'add', 'start', 'bebek')
  print(f"list_modify(['ayam', 'ikan', 'kucing'], 'add', 'start', 'bebek') = {r} \n(solusi: ['bebek', 'ayam', 'ikan', 'kucing'])")
  print()
  r = list_modify(['ayam', 'ikan', 'kucing'], 'add', 'end', 'bebek')
  print(f"list_modify(['ayam', 'ikan', 'kucing'], 'add', 'end', 'bebek') = {r} \n(solusi: ['ayam', 'ikan', 'kucing', 'bebek'])")
  print()
  r = list_modify(['ayam', 'ikan', 'kucing'], 'remove', 'start')
  print(f"list_modify(['ayam', 'ikan', 'kucing'], 'remove', 'start') = {r} \n(solusi: ['ikan', 'kucing'])")
  print()
  r = list_modify(['ayam', 'ikan', 'kucing'], 'remove', 'end')
  print(f"list_modify(['ayam', 'ikan', 'kucing'], 'remove', 'end') = {r} \n(solusi: ['ayam', 'ikan'])")
  print()

if __name__ == '__main__':
  test()
