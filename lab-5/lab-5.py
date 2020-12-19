def cetak_nama(nama=''):
  if (len(nama) > 0):
    for i in range(len(nama) + 1):
        for j in range(i):
          print(nama[j], end=" ")

        print(" ")
  else:
    print("Tidak ada nama yang dicetak")

# cetak_nama('Fikri')
  

def hitung_kesamaan(kata1, kata2):
    hasil = 0
    for i in range(len(kata1)):
        for j in range(len(kata2)):
            if (kata1[i] == kata2[j]):
                hasil = i
    return hasil

def hitung(bil1, bil2, operator='+'):
  hasil = 0
  if (operator == '+'):
    hasil = bil1 + bil2
    return hasil
  elif (operator == '-'):
    hasil = bil1 - bil2
    return hasil
  elif (operator == '*'):
    hasil = bil1 * bil2
    return hasil
  else:
    hasil = bil1 + bil2
    return hasil




# Mulai baris ini hingga baris paling bawah
# digunakan untuk mengetes fungsi yang telah dibuat.
# Tidak perlu mengubah bagian ini.
# Ketika dijalankan, program akan menampilkan contoh
# pemanggilan fungsi dan solusi yang seharusnya
# (untuk fungsi hitung_kesamaan() dan fungsi hitung()).
# Cocokkan hasil pemanggilan fungsi dengan solusi  
# yang seharusnya.
def test():
  print("Hasil cetak_nama('Mawar'):")
  cetak_nama("Mawar")
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
  r = hitung(4, 8)
  print(f'hitung(4, 8) = {r} \t\t(solusi: 12)')
  r = hitung(4, 8, '-')
  print(f"hitung(4, 8, '-') = {r} \t(solusi: -4)")
  r = hitung(4, 8, '*')
  print(f"hitung(4, 8, '*') = {r} \t(solusi: 32)")

if __name__ == '__main__':
  test()
