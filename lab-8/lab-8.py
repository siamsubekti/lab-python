# Nama: Tri Siam Subekti
# NIM: 0110220086
# Kelas: TI 07

def hitung_kemunculan(s):
  # Tulis kode fungsi hitung_kemunculan() di bawah ini
  # Hapus pass jika implementasi sudah dibuat

  # variable hasil dengan tipe data dictionary
  hasil = {}
  # variable array dengan menetapkan nilai dari parameter s yang telah di split, 
  # function split untuk mengabaikan nilai spasi dari parameter s yang mengandung nilai string
  array = s.split()
  # looping dari variable array yang telah di tetapkan nilai s yang di split
  for i in array:
    # variabel hasil dari tipe data dictionary untuk menetapkan nilai key dan value
    # hasil[s(str(i))] untuk menetapkan keys ke variable hasil
    # array.count(str(i)) untuk menetapkan value ke variable hasil
    # str untuk mengubah objek menjadi string
    # function count untuk mencari jumlah kemunculan dari index yang telah di loop
    hasil[str(i)] = array.count(str(i))
  # mengembalikan nilai hasil yang telah di tetapkan nilai keys dan valuenya.
  return hasil

def urut_unik(s):
  # Tulis kode fungsi urut_unik() di bawah ini
  # Hapus pass jika implementasi sudah dibuat

  # variabel list_dict dengan tipe data dictionary
  list_dict = {}
  # variable a yang ditetapkan nilai dari parameter s yang telah di split
  # function split untuk mengabaikan nilai spasi dari parameter s yang mengandung nilai string
  a = s.split()
  # variable list_urut yang di tetapkan dari function list yang mengembalikan sebuah list
  # kemudian list_dict menggunakan function formkeys yang mengembalikan urutan elemen yang diberikan sebagai keys dari variable list_dict
  list_urut = list(list_dict.fromkeys(a))
  # variable list_urut di urutkan sesuai abjad menggunakan function sort
  list_urut.sort()
  # mengembalikan nilai dari variabel list_urut
  return list_urut

def read(filename):
  # Tulis kode fungsi read() di bawah ini
  # Hapus pass jika implementasi sudah dibuat

  # variabel f yang di tetapkan nilai dari function open untuk membuka file dari parameter filename
  f = open(filename)
  # variable kamus yang bernilai tipe data dictionary
  kamus = {}
  # looping dengan variable line dari variabel f yang isinya adalah file yang di open dari parameter filename
  for line in f:
    # variabel hasil yang ditetapkan dari index line yang telah di split
    hasil = line.split()
    # variabel kamus dengan ditetapkan nilai keys dan value dengan cara mengambil index 0 dari variabel hasil sebagai keys dan index 1 dari variabel hasil sebagai value
    kamus[hasil[0]] = hasil[1]
  # mengembalikan nilai dari variable kamus dengan tipe data dictionary
  return kamus





# Mulai baris ini hingga baris paling bawah
# digunakan untuk mengetes fungsi yang telah dibuat.
# Tidak perlu mengubah bagian ini.
# Ketika dijalankan, program akan menampilkan contoh
# pemanggilan fungsi dan solusi yang seharusnya.
# Cocokkan hasil pemanggilan fungsi dengan solusi  
# yang seharusnya.
def test():
  r = hitung_kemunculan("pisang jambu apel jambu pisang jeruk")
  print(f"hitung_kemunculan('pisang jambu apel jambu pisang jeruk') = {r} \n(solusi: {{'pisang': 2, 'jambu': 2, 'apel': 1, 'jeruk': 1}})")
  print()
  r = urut_unik("pisang jambu apel jambu pisang jeruk")
  print(f"urut_unik('pisang jambu apel jambu pisang jeruk') = {r} \n(solusi: ['apel', 'jambu', 'jeruk', 'pisang'])")
  print()
  r = urut_unik('kecapi melon kecapi kecapi kecapi')
  print(f"urut_unik('kecapi melon kecapi kecapi kecapi') = {r} \n(solusi: ['kecapi', 'melon'])")
  print()
  r = read('data1.txt')
  print(f"read('data1.txt') = {r} \n(solusi: {{'101': 'Teddy-Bear', '102': 'Kelereng', '201': 'Laptop', '202': 'Smartphone', '203': 'Speaker', '301': 'Avanza', '302': 'Supra-X', '401': 'Topi', '402': 'Jaket', '403': 'Scarf'}}")
  print()
  r = read('data2.txt')
  print(f"read('nilai2.txt') = {r} \n(solusi: {{'711': 'Malaysia', '712': 'Singapura', '713': 'Indonesia', '814': 'USA', '815': 'Canada'}}")
  print()

if __name__ == '__main__':
  test()
