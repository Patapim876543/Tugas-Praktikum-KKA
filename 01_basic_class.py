# LATIHAN 1: Dasar Class dan Object

class Hero:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")

# --- Main Program ---
hero1 = Hero("Layla", 100, 15)
hero2 = Hero("Zilong", 120, 20)

hero1.info()
hero2.info()

# [TUGAS ANALISIS 1]
# Coba ubah atribut public ini secara langsung
# hero1.hp = 500
# print(f"HP Layla setelah dihack: {hero1.hp}")