# Jalankan program berikut dengan menekan tombol Run
# Masukkan nama kamu dan tekan enter
# Perhatikan luaran dari program tersebut
# Pelajari yang dilakukan oleh program tersebut
# (Optional) Bisakah kamu menambahkan baris kode
# sehingga program menanyakan umur 
# dan menampilkannya ke layar?

# nama = input("Masukkan nama Anda: ")
# print("Halo, ", nama, ". Belajar pemrograman itu menyenangkan.", sep="")
# rows = 5
rows = input("Masukkan Rows: ");
intRows = int(rows);
for i in range(0, intRows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(intRows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")
