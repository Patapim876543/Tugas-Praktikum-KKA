# -- Laporan Analisis Praktikum OOP Python -- #
Nama: Muhammad Taufiqurrohman  
Kelas: XI RPL 6  
Mata Pelajaran: Pemrograman Berorientasi Objek



# -- Analisis 1: Basic Class & Object (Modifikasi Atribut Public) -- #
File Referensi: `01_basic_class.py`

# --- Pertanyaan: --- #
Apa yang terjadi jika kamu mengubah `hero1.hp` menjadi 500 setelah baris inisialisasi objek?

# --- Jawaban: --- #
Nilai HP hero tersebut akan berubah menjadi 500.
Penjelasan: Hal ini terjadi karena atribut `hp` pada class Hero bersifat **Public** (tidak ada tanda `__`). Python mengizinkan akses dan modifikasi langsung dari luar class. Ini menunjukkan bahwa data belum terlindungi (belum menerapkan Enkapsulasi).



# -- Analisis 2: Interaksi Antar Objek -- #
File Referensi: `02_interaksi.py`

# --- Pertanyaan: --- #
Mengapa parameter `lawan` pada method `serang` menerima sebuah objek utuh, bukan hanya string nama?

# --- Jawaban: --- #
Karena method `serang` membutuhkan akses ke **data (atribut) dan kemampuan (method)** milik lawan secara real-time.
Penjelasan: Jika hanya mengirim string (teks), kita hanya tahu namanya saja. Dengan mengirim objek utuh, `hero1` bisa mengakses `lawan.hp` untuk dikurangi atau memanggil `lawan.diserang()`. Ini memungkinkan interaksi dinamis antar objek.



# -- Analisis 3: Pewarisan (Inheritance) & Super() -- #
File Referensi: `03_inheritance.py`

# --- Pertanyaan: --- #
1. Apa yang terjadi jika `super().__init__(...)` dihapus pada class Mage?
2. Jelaskan fungsi `super()`!

# --- Jawaban: --- #
1. Error: `AttributeError: 'Mage' object has no attribute 'name'`. Program akan error saat mencoba mengakses nama atau HP.
2. Fungsi Super: `super()` berfungsi untuk memanggil method milik **Parent Class (Induk)**. Tanpa `super()`, constructor induk tidak berjalan, sehingga atribut dasar (nama, hp, attack_power) tidak pernah dibuat/disiapkan untuk Mage.



# -- Analisis 4: Enkapsulasi (Keamanan Data) -- #
File Referensi: `04_encapsulation.py`

# --- Pertanyaan: --- #
1. Apa hasil dari akses paksa `hero1._Hero__hp`?
2. Apa yang terjadi jika logika validasi di Setter dihapus?

# --- Jawaban: --- #
1. Berhasil (Akses Paksa) Nilai HP tetap muncul. Ini disebut *Name Mangling*. Python tidak memblokir total, hanya menyamarkan nama variabel. Namun, mengaksesnya secara paksa adalah praktik yang buruk.
2. Integritas Data Rusak: Jika validasi dihapus, HP bisa di-set ke angka yang tidak masuk akal, seperti **-100 (Negatif)**. Setter berfungsi sebagai "satpam" untuk mencegah bug logika seperti nyawa negatif.



# -- Analisis 5: Abstraction & Interface -- #
File Referensi: `05_abstraction.py`

# --- Pertanyaan: --- #
1. Apa yang terjadi jika class `Hero` tidak membuat method `serang`?
2. Mengapa kita tidak bisa membuat objek langsung dari `GameUnit`?

# --- Jawaban: --- #
1. Error Instansiasi: `TypeError: Can't instantiate abstract class...`. Class Hero dianggap melanggar kontrak karena tidak melengkapi method abstrak yang diwajibkan oleh induknya.
2. Abstract Class: `GameUnit` adalah Abstract Class (konsep/cetakan dasar), bukan benda nyata. Tujuannya hanya sebagai kerangka (blueprint) agar semua class turunannya memiliki standar method yang sama.



# -- Analisis 6: Polymorphism -- #
File Referensi: `06_polymorphism.py`

# --- Pertanyaan: --- #
1. Jika menambah class baru (misal: `Healer`), apakah perlu mengubah Loop utama?
2. Bolehkah mengubah nama method `serang` menjadi `tembak_panah` pada salah satu child class?

# --- Jawaban: --- #
1. Tidak Perlu: Loop utama tidak perlu diubah sama sekali. Ini membuktikan kode bersifat **Scalable** (mudah dikembangkan) berkat polimorfisme.
2. Tidak Boleh (Error): Jika nama method diubah (tidak konsisten), sistem akan error saat looping memanggil `.serang()`. Syarat polimorfisme adalah nama method harus seragam di semua class turunan.