# LATIHAN 2: Interaksi Antar Objek

class Hero:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    # [TUGAS ANALISIS 2]
    # Parameter 'lawan' di sini menerima OBJEK UTUH, bukan cuma string nama.
    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)

    def diserang(self, damage):
        self.hp -= damage
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self.hp}")

# --- Main Program ---
hero1 = Hero("Layla", 100, 15)
hero2 = Hero("Zilong", 120, 20)

print("--- Mulai Bertarung ---")
hero1.serang(hero2)
hero2.serang(hero1)