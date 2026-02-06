# LATIHAN 4: Enkapsulasi (Keamanan Data)

class Hero:
    def __init__(self, nama, hp_awal):
        self.nama = nama
        self.__hp = hp_awal # Private (Rahasia)

    # Getter
    def get_hp(self):
        return self.__hp

    # Setter (dengan Validasi)
    def set_hp(self, nilai_baru):
        # [TUGAS ANALISIS 4.2] Coba hapus if/else ini untuk melihat efeknya
        if nilai_baru < 0:
            self.__hp = 0
        elif nilai_baru > 1000:
            self.__hp = 1000
        else:
            self.__hp = nilai_baru

# --- Main Program ---
hero1 = Hero("Layla", 100)

# [TUGAS ANALISIS 4.1] Akses Paksa (Name Mangling)
# print(hero1._Hero__hp) 

# Uji Validasi
hero1.set_hp(-50)
print(f"HP setelah diset negatif: {hero1.get_hp()}")