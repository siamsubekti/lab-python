# DDP LAB-4
# Nama: <Tulis nama di sini>
# NIM: <Tulis NIM di sini>

# SOAL 1 - Mencetak nama
# Tuliskan program untuk Soal 1 di bawah ini
print("Soal 1")
print()
input_nama = input('Masukan nama : ')
print(input_nama)
# int(len(input_nama):
jumlah_nama = len(input_nama)
for i in range(len(input_nama) + 1):
  for j in range(i):
    print(input_nama[j], end=" ")
  
  print(" ")
  # print(inp)
print()

# SOAL 2 - Validasi teks
# Tuliskan program untuk Soal 2 di bawah ini
print("Soal 2")
while True:
  input_teks = input("Masukkan sebuah teks: ")

  panjang_teks = len(input_teks)
  lower_teks = input_teks.lower() 
  first_rule = panjang_teks > 7 
  second_rule = lower_teks.count('nf') >= 1
  third_rule = True if input_teks.endswith('yyy') or input_teks.endswith('YYY')else False 
  fourth_rule = input_teks.count('0') or input_teks.count('1') or input_teks.count('2') or input_teks.count('3') or input_teks.count('4') or input_teks.count('5') or input_teks.count('6') or input_teks.count('7') or input_teks.count('8') or input_teks.count('9')
  
  if first_rule and second_rule and third_rule and fourth_rule:
    print('Teks valid. Program berhenti.')
    break
  else:
    print('Teks tidak valid.')
