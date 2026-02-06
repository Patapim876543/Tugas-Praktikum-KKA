from abc import ABC, abstractmethod

# --- ABSTRACTION ---
class BarangElektronik(ABC):
    def __init__(self, nama, harga_dasar, stok_awal):
        self.nama = nama
        # --- ENCAPSULATION ---
        self.__harga_dasar = harga_dasar # Private
        self.__stok = 0                  # Private awal
        self.set_stok(stok_awal)         # Menggunakan setter untuk validasi awal

    # GETTER untuk Stok
    @property
    def stok(self):
        return self.__stok

    # GETTER untuk Harga Dasar (dibutuhkan class anak untuk hitung pajak)
    def get_harga_dasar(self):
        return self.__harga_dasar

    # SETTER dengan Validasi [cite: 268]
    def set_stok(self, jumlah):
        if jumlah >= 0:
            self.__stok = jumlah
            return True
        else:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
            return False

    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass

# --- INHERITANCE ---
class Laptop(BarangElektronik):
    def __init__(self, nama, harga_dasar, stok_awal, processor):
        super().__init__(nama, harga_dasar, stok_awal)
        self.processor = processor

    # POLYMORPHISM: Override Method [cite: 272]
    def tampilkan_detail(self):
        return f"[LAPTOP] {self.nama} | Proc: {self.processor}"

    def hitung_harga_total(self, jumlah):
        pajak = self.get_harga_dasar() * 0.10 # Pajak 10% [cite: 270]
        total_per_unit = self.get_harga_dasar() + pajak
        return total_per_unit * jumlah, pajak

class Smartphone(BarangElektronik):
    def __init__(self, nama, harga_dasar, stok_awal, kamera):
        super().__init__(nama, harga_dasar, stok_awal)
        self.kamera = kamera

    # POLYMORPHISM: Override Method [cite: 272]
    def tampilkan_detail(self):
        return f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}"

    def hitung_harga_total(self, jumlah):
        pajak = self.get_harga_dasar() * 0.05 # Pajak 5% [cite: 271]
        total_per_unit = self.get_harga_dasar() + pajak
        return total_per_unit * jumlah, pajak