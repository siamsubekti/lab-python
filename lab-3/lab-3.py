# DDP LAB-3

# SOAL 1 - Gunting-Batu-Kertas
# Tuliskan program untuk Soal 1 di bawah ini
print('# Nomor 1')
print()
print('Masukan inputan diantara kata berikut :')

print('1.gunting',
      '2.batu', 
      '3.kertas')
print()
player1 = input("Masukkan Player-1 = ")
player2 = input("Masukkan Player-2 = ")
player1 = player1.lower()
player2 = player2.lower()

if (player1 and player2 == "gunting") or (player1 and player2 == "kertas") or (player1 and player2 == "batu"):
  if player1 == player2:
    print("Seri")
  elif player1 != player2:
    if (player1 == "gunting" and player2 == "batu") or (player1 == "batu" and player2 == "kertas") or (player1 == "kertas" and player2 == "gunting"):
      print("Player 2 Menang")
    elif (player1 == "batu" and player2 == "gunting") or (player1 == "gunting" and player2 == "kertas") or (player1 == "kertas" and player2 == "batu"):
      print("Player 1 Menang")
else:
  print("Inputan Salah")

print('==================================================')
print()
# SOAL 2 - Toko Buku Bekas
# Tuliskan program untuk Soal 2 di bawah ini
print('# Nomor 2')
print()
jumlahBuku = int(input("Masukkan jumlah buku yang akan dibeli = "))

if jumlahBuku < 10:
  total = jumlahBuku * 20000
  print("Total Harga ", total)
elif (jumlahBuku > 10) and (jumlahBuku < 26):
  total = jumlahBuku * 18000
  print("Total harga ", total)
elif (jumlahBuku >= 26) and (jumlahBuku <= 50):
  total = jumlahBuku * 15000
  print("Total harga ", total)
elif jumlahBuku > 50:
  total = jumlahBuku * 10000
  print("Total harga ", total)


print('==================================================')
print()
# SOAL 3 - Mencetak Persegi
# Tuliskan program untuk Soal 3 di bawah ini
print('# Nomor 3')
print()
bulat = int(input("Masukkan sebuah bilangan bulat = "))
for c in range(bulat):
  print(end='\n')
  if c % 2 == 0:
    for a in range(bulat):
      print('#', end=' ')
  else:
    for a in range(bulat):
      print('$', end=' ')




