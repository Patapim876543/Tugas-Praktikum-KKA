# LATIHAN 3: Pewarisan (Inheritance)

class Hero:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp}")

    def diserang(self, damage):
        self.hp -= damage
        print(f"{self.name} sisa HP: {self.hp}")

class Mage(Hero):
    def __init__(self, name, hp, attack_power, mana):
        # [TUGAS ANALISIS 3]
        # Coba hapus baris super().__init__ di bawah ini, lalu jalankan.
        super().__init__(name, hp, attack_power) 
        self.mana = mana

    def info(self):
        print(f"{self.name} [Mage] | HP: {self.hp} | Mana: {self.mana}")

    def skill_fireball(self, lawan):
        if self.mana >= 20:
            print(f"{self.name} lempar Fireball ke {lawan.name}!")
            self.mana -= 20
            lawan.diserang(self.attack_power * 2)

# --- Main Program ---
eudora = Mage("Eudora", 80, 30, 100)
balmond = Hero("Balmond", 200, 10)

eudora.info()
eudora.skill_fireball(balmond)