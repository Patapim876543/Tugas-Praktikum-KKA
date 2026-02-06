# LATIHAN 5: Abstraction & Interface

from abc import ABC, abstractmethod

# Abstract Class (Cetakan Dasar)
class GameUnit(ABC):
    @abstractmethod
    def serang(self, target): pass

    @abstractmethod
    def info(self): pass

# Concrete Class (Objek Nyata)
class Hero(GameUnit):
    def __init__(self, nama):
        self.nama = nama
    
    # [TUGAS ANALISIS 5] Wajib ada method serang & info
    def serang(self, target):
        print(f"Hero {self.nama} menyerang {target}!")
    
    def info(self):
        print(f"Saya Hero: {self.nama}")

# --- Main Program ---
# unit = GameUnit() # Error jika dijalankan (Analisis)
h = Hero("Alucard")
h.info()
h.serang("Minion")