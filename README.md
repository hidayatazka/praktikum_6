# latihan
- buatlah dictonary daftar kontak (nama sebagai key,dan nomer sebagai value)
- tampilkan kontak nya mamat
- tambahkan kontak baru dengan nama aska 087654544
- ubah kontak darto dengan nomer baru 087677776
- tampilkan semua nama
- tampilkan semua nomer
- tampilkan daftar nama dan nomer
- hapus kontak darto
# RUMUS NYA
# Latihan
print("Nama : hidayat azka")
print("NIM  : 312210374")

daftarkontak = {"Nama": "Nomer Telepon"}
kontak = {'mamat': '081267888', 'Darto': '087677776'}

# print
print("============================")
print("|   # Nama   |Nomor Telepon|")
print("============================")
print("|   # mamat    |  ", kontak['mamat'], '|')
print("|   # Darto   |  ", kontak['Darto'], '|')
print("============================")
print()

# Tampilkan kontaknya mamat
print("# Tampilkan kontaknya mamat")
print("===========================")
print("|    mamat     | ", kontak['mamat'], '|')
print("===========================")
print()

# Tambah kontak baru dengan nama aska, nomor 087654544
print("# Tambah kontak baru dengan nama aska, nomor 087654544")
kontak['aska'] = '087654544'
print("===========================")
print("|    aska    | ", kontak['aska'], '|')
print("===========================")
print()

# Ubah kontak darto dengan nomor baru 088999776
print("# Ubah kontak Darto dengan nomor baru 088999776")
kontak['Darto'] = '088999776'
print("===========================")
print("|    Darto    | ", kontak['Darto'], '|')
print("===========================")
print()

# Tampilkan semua Nama
print("# Tampilkan semua Nama")
print("==================================")
print(kontak.keys())
print("==================================")
print()

# Tampilkan semua Nomor
print("# Tampilkan semua Nomor")
print("====================================================")
print(kontak.values())
print("====================================================")
print()

# Tampilkan daftar Nama dan nomornya
print("# Tampilkan daftar Nama dan nomornya")
print("================================================================================")
print(kontak.items())
print("================================================================================")
print()

# Menghapus kontak Darto
print("# Hapus kontak Darto")
print("=========================================================")
kontak.pop('Darto')
print(kontak.items())
print("=========================================================")
# PROGRAM NYA
![img](gambar/coding%20Latihan.py%201.png)
![img](gambar/coding%20Latihan.py%202.png)
![img](gambar/coding%20Latihan.py%203.png)
# HASIL PEMOGRAMAN 
![img](gambar/hasil%20codingan%20latihan.png)
![img](gambar/hasil%20codingan%20latihan%202.png)
rumus praktikum6
python x = {}
while True: c = input("\n(T)ambah, (U)bah, (H)apus, (C)ari, (L)ihat, (K)eluar: ")
if c.lower() == 't': print("Tambah Data") nama = input("Nama : ") nim = int(input("NIM : ")) uts = int(input("Nilai UTS : ")) uas = int(input("Nilai UAS : ")) tugas = int(input("Nilai Tugas : ")) akhir = tugas30/100 + uts35/100 + uas*35/100 x[nama] = nim, uts, uas, tugas, akhir

elif c.lower() == 'u': print("Ubah Data") nama = input("Masukkan Nama : ") if nama in x.keys(): nim = int(input("NIM : ")) uts = int(input("Nilai UTS : ")) uas = int(input("Nilai UAS : ")) tugas = int(input("Nilai Tugas : ")) akhir = tugas * 30 / 100 + uts * 35 / 100 + uas * 35 / 100 x[nama] = nim, uts, uas, tugas, akhir else: print("Nama {0} tidak ditemukan".format(nama))

elif c.lower() == 'h': print("Hapus Data") nama = input("Masukkan Nama : ") if nama in x.keys(): del x[nama] else: print("Nama {0} Tidak Ditemukan".format(nama))

elif c.lower() == 'c': print("Cari Data") nama = input("Masukkan Nama : ") if nama in x.keys(): print("="*73) print("| Daftar Mahasiswa |") print("="*73) print("| Nama | NIM | UTS | UAS | Tugas | Akhir |") print("="*73) print("| {0:15s} | {1:15d} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |" .format(nama, nim, uts, uas, tugas, akhir)) print("="*73) else: print("Nama {0} Tidak Ditemukan".format(nama))

elif c.lower() == 'l': if x.items(): print("="*78) print("| Daftar Mahasiswa |") print("="*78) print("|No. | Nama | NIM | UTS | UAS | Tugas | Akhir |") print("="*78) i = 0 for z in x.items(): i += 1 print("| {no:2d} | {0:15s} | {1:15d} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |" .format(z[0][:13], z[1][0], z[1][1], z[1][2], z[1][3], z[1][4], no=i)) print("=" * 78) else: print("="*78) print("| Daftar Mahasiswa |") print("="*78) print("|No. | Nama | NIM | UTS | UAS | Tugas | Akhir |") print("="*78) print("| TIDAK ADA DATA |") print("="*78)

elif c. lower() == 'k': break

else: print("Pilih menu yang tersedia")

Penjelasan :
1.) Pertama kita membuat sebuah dictionary kosong yang nantinya akan diinputkan data ketika program dijalankan. python

2.) Lalu kita membuat kondisi perulangan dan sebuah keterangan untuk pilihan menu yang akan menjalankan program. python Gambar 2

3.) Membuat syntax untuk menambahkan data. python Disini apabila kita menginputkan 't' maka kita akan diminta untuk menginputkan beberapa data. Data yang kita inputkan akan masuk ke dictionary 'x' yang telah dibuat tadi dengan data 'nama' sebagai keys dan sisanya sebagai valuesnya.

4.) Membuat syntax untuk mengubah data. python Apabila kita menginput 'u' maka akan ada keterangan untuk mengubah data dan kita akan diminta untuk menginputkan nama yang mau diubah datanya, apabila nama tidak ada maka outputnya "Nama {} tidak ditemukan". Dimana {} adalah nama/data yang mau kita ubah.

5.) Membuat syntax untuk menghapus data. python Apabila kita menginput 'h' maka kita akan diminta menginput nama yang akan dihapus. Jika nama ada di dalam dictionary, maka system akan menghapus keys/nama tersebut beserta valuesnya pada statement del x[nama].

6.) Membuat syntax untuk mencari data. python Apabila kita menginputkan 'c' maka kita akan diminta untuk memasukkan nama yang akan dicari. Apabila nama yang dicari ada di dalam dictionary maka outputnya akan menampilkan data dari nama tersebut.

7.) Membuat syntax untuk melihat atau menampilkan data. python Apabila kita menginput 'l' maka sistem akan menampilkan data - data yang sudah kita masukkan. Jika kita belum memasukkan data maka outputnya menjadi "TIDAK ADA DATA".

8.) Membuat syntax untuk menghentikan perulangan. python Apabila kita menginput 'k' maka program akan langsung berhenti.

9.) Membuat syntax untuk apabila memilih pilihan yang tidak ada di menu. python kita menginputkan selain yang ada pada menu (t, u, h, c, l, k) maka kita akan diminta untuk memilih menu yang tersedia.

# contoh codingan dictionary
![img](gambar/coding%20praktikum%201.png)
![img](gambar/coding%20praktikum%202.png)
![img](gambar/coding%20praktikum%203.png)
# HASIL DARI CODINGAN DICTONARY
![img](gambar/gambar%201.png)
![img](gambar/gambar%202.png)
![img](gambar/gambar%203.png)

