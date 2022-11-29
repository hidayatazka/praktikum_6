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