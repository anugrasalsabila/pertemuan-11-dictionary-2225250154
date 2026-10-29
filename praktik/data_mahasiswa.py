
def cari_mahasiswa(data, nim):
    return data.get(nim)


def rata_rata_nilai(data):
    if not data:
        return 0

    total = 0

    for info in data.values():
        total += info["nilai"]

    return total / len(data)


data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}

# 1. Pencarian mahasiswa berdasarkan NIM
print("=== PENCARIAN MAHASISWA ===")

nim_cari = "A003"
hasil = cari_mahasiswa(data_mahasiswa, nim_cari)

if hasil is not None:
    print(f"Data {nim_cari}: {hasil}")
else:
    print("Data tidak ditemukan")

# 2. Pencarian NIM yang tidak tersedia
nim_cari = "A999"
hasil = cari_mahasiswa(data_mahasiswa, nim_cari)

if hasil is not None:
    print(f"Data {nim_cari}: {hasil}")
else:
    print(f"Data {nim_cari} tidak ditemukan")

# 3. Menambahkan mahasiswa baru
print("\n=== TAMBAH MAHASISWA ===")

data_mahasiswa["A006"] = {
    "nama": "Fajar",
    "kelas": "B",
    "nilai": 80
}

print("Mahasiswa A006 berhasil ditambahkan")

# 4. Memperbarui nilai mahasiswa
print("\n=== PEMBARUAN NILAI ===")

data_mahasiswa["A002"]["nilai"] = 82

print("Nilai Budi (A002) berhasil diubah menjadi 82")

# 5. Menampilkan seluruh data menggunakan items()
print("\n=== SELURUH DATA MAHASISWA ===")

for nim, info in data_mahasiswa.items():
    print(
        f"NIM: {nim}, "
        f"Nama: {info['nama']}, "
        f"Kelas: {info['kelas']}, "
        f"Nilai: {info['nilai']}"
    )

# 6. Menghitung rata-rata nilai mahasiswa
print("\n=== RATA-RATA NILAI ===")

rata_rata = rata_rata_nilai(data_mahasiswa)

print(f"Rata-rata nilai mahasiswa: {rata_rata:.2f}")