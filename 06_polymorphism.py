# LATIHAN 6: Polymorphism (Banyak Bentuk)

class Hero:
    def __init__(self, nama): self.nama = nama
    def serang(self): print("Hero menyerang basic")

class Mage(Hero):
    def serang(self): print(f"{self.nama} (Mage) : MAGIC SPLASH!")

class Archer(Hero):
    # [TUGAS ANALISIS 6] Jangan ubah nama method jadi 'tembak_panah'
    def serang(self): print(f"{self.nama} (Archer) : ARROW SHOT!")

class Fighter(Hero):
    def serang(self): print(f"{self.nama} (Fighter) : PUNCH!")

# --- Main Program ---
pasukan = [
    Mage("Eudora"),
    Archer("Miya"),
    Fighter("Chou")
]

print("--- WAR START ---")
# Satu perintah .serang(), respon beda-beda
for p in pasukan:
    p.serang()