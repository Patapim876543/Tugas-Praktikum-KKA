# -- TechMaster Inventory System -- #

Proyek ini adalah implementasi sistem manajemen inventaris toko elektronik menggunakan bahasa pemrograman Python dengan menerapkan **4 Pilar Utama OOP**.

# -- Implementasi Pilar OOP -- #
1.  [cite_start] Abstraction: Menggunakan class `BarangElektronik` sebagai blueprint abstrak yang tidak bisa di-instansiasi[cite: 262, 263].
2.  Encapsulation: Atribut `__stok` dan `__harga_dasar` bersifat private. Perubahan stok wajib melalui method `set_stok()` yang memiliki validasi angka negatif[cite: 266, 268].
3.  [cite_start]**Inheritance**: Class `Laptop` dan `Smartphone` mewarisi seluruh fungsi dasar dari `BarangElektronik`[cite: 269].
4.  Polymorphism: 
    - [cite_start]*Method Overriding*: `hitung_harga_total()` memiliki logika pajak berbeda (Laptop 10%, Smartphone 5%)[cite: 270, 271].
    - [cite_start]*Generic Function*: Fungsi `proses_transaksi()` dapat memproses berbagai jenis objek elektronik dalam satu list secara seragam[cite: 273].

# -- Cara Menjalankan -- #
Jalankan file utama melalui terminal:
```bash
python main.py