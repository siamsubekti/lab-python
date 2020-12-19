# Nama: Tri Siam Subekti
# NIM: 0110220086
# Kelas: TI07

def convert_list(multilist):
  # Tulis kode fungsi convert_list() di bawah ini
  # Hapus pass jika implementasi sudah dibuat
  # variable new list
  new_multilist = []
  # perulangan dengan sebanyak panjang parameter multilist
  for i in range(len(multilist)):
    # perulangan dengan sebanyak panjang dari index multilist
    for j in range(len(multilist[i])):
      # menetapkan nilai list new multilist ke list multilist
        new_multilist.append(multilist[i][j])
  # mengembalikan nilai variable new multilist
  return new_multilist

def get_nilai(filename, nama):
  # Tulis kode fungsi get_nilai() di bawah ini
  # Hapus pass jika implementasi sudah dibuat
  # function open dengan directory yang dituju dari parameter
  f = open(filename)
  # perulangan dati variable yang membuka isi dari file.
  for each_line in f:
    # mengabaikan spasi
      data = each_line.split()
      # kondisi jika data nama dengan parameter sama
      if data[0].lower() == nama.lower():
        # mengembalikan nilai data index ke satu kemudian di float untuk membaca nilai yang berisi koma
          return round(float(data[1]))
  
  # menutup file yang sudah terbuka
  f.close()

def nilai_max(filename):
  # Tulis kode fungsi nilai_max() di bawah ini
  # Hapus pass jika implementasi sudah dibuat
  # Buat nama variabel list_nilai dengan tipe data array
  list_nilai = []
  # buka file dengan nama file yang diterima oleh parameter filename, dan simpan datanya kedalam variabel f
  f = open(filename)
  # lakukan perulangan dengan data yang ada di variabel f
  for each_line in f:
    # masukan nilai each_line yang sudah dipisah menggunakan split dan simpan di variabel data
    data = each_line.split()
    # masukan nilai data dan index ke 0 kedalam variabel nama
    nama = data[0]
    # masukan nilai data dan index ke 1 kedalam variabel nama dan bertipe float
    nilai = float(data[1])
    #tambahkan nilai kedalam variabel list_nilai, dengan nilai sebagai index 0 dan nama sebagai index 1
    list_nilai.append([nilai, nama])
  # panggil fungsi close untuk menyatakan telah selesai membuka file
  f.close()
  
  # mencari nilai max yang ada di variabel list_nilai
  max_nilai = max(list_nilai)
  # kembalikan nilai dari variabel max_nilai dengan index ke 1 baru index ke 2
  return max_nilai[1],max_nilai[0]


# Mulai baris ini hingga baris paling bawah
# digunakan untuk mengetes fungsi yang telah dibuat.
# Tidak perlu mengubah bagian ini.
# Ketika dijalankan, program akan menampilkan contoh
# pemanggilan fungsi dan solusi yang seharusnya.
# Cocokkan hasil pemanggilan fungsi dengan solusi  
# yang seharusnya.
def test():
  r = convert_list([[1,2], [3,4], [5,6]])
  print(f"convert_list([[1,2], [3,4], [5,6]]) = {r} \n(solusi: [1, 2, 3, 4, 5, 6])")
  print()
  r = get_nilai('nilai1.txt','joni')
  print(f"get_nilai('nilai1.txt','joni') = {r} \n(solusi: 76)")
  print()
  r = get_nilai('nilai2.txt','joni')
  print(f"get_nilai('nilai2.txt','joni') = {r} \n(solusi: None)")
  print()
  r = nilai_max('nilai1.txt')
  print(f"nilai_max('nilai1.txt') = {r} \n(solusi: ('Zack', 88.05)")
  print()
  r = nilai_max('nilai2.txt')
  print(f"nilai_max('nilai2.txt') = {r} \n(solusi: ('Arya', 90.00)")
  print()

if __name__ == '__main__':
  test()
