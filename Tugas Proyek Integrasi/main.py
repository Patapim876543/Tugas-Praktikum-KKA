from inventory import Laptop, Smartphone

# --- POLYMORPHISM: Fitur Keranjang Belanja ---
def proses_transaksi(daftar_belanja):
    print("\n--- STRUK TRANSAKSI ---")
    total_tagihan = 0
    
    for i, item in enumerate(daftar_belanja, 1):
        produk = item['produk']
        qty = item['qty']
        
        subtotal, pajak_satuan = produk.hitung_harga_total(qty)
        total_tagihan += subtotal
        
        print(f"{i}. {produk.tampilkan_detail()}")
        print(f"   Harga Dasar: Rp {produk.get_harga_dasar():,.0f} | Pajak: Rp {pajak_satuan:,.0f}")
        print(f"   Beli: {qty} unit | Subtotal: Rp {subtotal:,.0f}")
    
    print("-" * 40)
    print(f"TOTAL TAGIHAN: Rp {total_tagihan:,.0f}")
    print("-" * 40)

# --- ALUR PROGRAM (USER STORY) ---
print("--- SETUP DATA ---")
# 1. Admin membuat data produk
laptop_rog = Laptop("ROG Zephyrus", 20000000, 0, "Ryzen 9")
if laptop_rog.set_stok(10):
    print(f"Berhasil menambahkan stok {laptop_rog.nama}: 10 unit.")

iphone = Smartphone("iPhone 13", 15000000, 0, "12MP")

# 2. Admin mencoba mengisi stok negatif [cite: 276]
iphone.set_stok(-5) 

# Isi stok yang benar
if iphone.set_stok(20):
    print(f"Berhasil menambahkan stok {iphone.nama}: 20 unit.")

# 3. User membeli produk (Simulasi Keranjang) [cite: 277]
keranjang = [
    {'produk': laptop_rog, 'qty': 2},
    {'produk': iphone, 'qty': 1}
]

# 4. Jalankan Transaksi
proses_transaksi(keranjang)