
# Pertemuan 11 - Dictionary dan Map

Nama: Intan Anugra Salsabila
NIM: 2225250154
Kelas: ...

## Tujuan

Memahami penggunaan dictionary dalam Python untuk menyimpan,
mencari, menambahkan, memperbarui, dan menampilkan data mahasiswa.

## Struktur Data

Program menggunakan dictionary dengan NIM sebagai key utama.
Setiap NIM menyimpan data nama, kelas, dan nilai mahasiswa.

Contoh:
```python
"A001": {"nama": "Ayu", "kelas": "A", "nilai": 85}
```

## Cara Menjalankan

Menjalankan latihan:

```bash
py latihan/01_dasar_dictionary.py
py latihan/02_akses_get.py
py latihan/03_manipulasi_dictionary.py
py latihan/04_iterasi_dictionary.py
py latihan/05_dictionary_bersarang.py
py latihan/06_fungsi_dictionary.py
```

Menjalankan praktik utama:

```bash
py praktik/data_mahasiswa.py
```

## Algoritma Praktik

1. Menyiapkan dictionary data mahasiswa.
2. Membuat fungsi cari_mahasiswa(data, nim).
3. Membuat fungsi rata_rata_nilai(data).
4. Menguji pencarian NIM yang tersedia dan tidak tersedia.
5. Menambahkan mahasiswa baru dengan NIM A006.
6. Memperbarui nilai mahasiswa A002 menjadi 82.
7. Menampilkan seluruh data menggunakan items().
8. Menghitung dan menampilkan rata-rata nilai mahasiswa.

## Hasil Pengujian

| Kasus | Input/Aksi | Hasil |
|---|---|---|
| Pencarian tersedia | A003 | Data Citra ditampilkan |
| Pencarian tidak tersedia | A999 | Data tidak ditemukan |
| Penambahan data | A006 | Data Fajar ditambahkan |
| Pembaruan nilai | A002 menjadi 82 | Nilai Budi berubah menjadi 82 |
| Rekap data | items() | Semua data mahasiswa tampil |
| Rata-rata nilai | 6 mahasiswa | 83.50 |

## Analisis Efisiensi

Pencarian berdasarkan NIM menggunakan dictionary memiliki
rata-rata kompleksitas waktu O(1).

Penambahan dan pembaruan data berdasarkan key juga memiliki
rata-rata kompleksitas waktu O(1).

Penampilan seluruh data dan perhitungan rata-rata nilai
memerlukan waktu O(n), dengan n adalah jumlah mahasiswa.

## Refleksi

1. Apa perbedaan akses menggunakan tanda kurung siku dan get()?

   Tanda kurung siku dapat menghasilkan KeyError jika key tidak
   ditemukan, sedangkan get() dapat mengembalikan None atau nilai
   default.

2. Mengapa NIM digunakan sebagai key?

   Karena NIM digunakan untuk membedakan dan mencari data mahasiswa.

3. Apa fungsi items()?

   items() digunakan untuk mengambil pasangan key dan value
   dalam dictionary.

4. Apa manfaat dictionary bersarang?

   Dictionary bersarang dapat menyimpan beberapa informasi
   mahasiswa dalam satu NIM.

## Kesimpulan

Dictionary memudahkan pengelolaan data mahasiswa berdasarkan NIM.
Melalui praktikum ini, saya mempelajari pencarian, penambahan,
pembaruan, iterasi, dan perhitungan rata-rata nilai menggunakan
Python.