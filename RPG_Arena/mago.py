import random
from personagem import Personagem

class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome, 80)

    def atacar(self, inimigo):
        dano_base = 25
        critico = random.random() < 0.30  # 30% de chance
        
        if critico:
            dano = dano_base * 2
            print(f"💥 MAGIA CRÍTICA! O Mago {self.nome} obliterou {inimigo.nome} com {dano} de dano!")
        else:
            dano = dano_base
            print(f"🔮 O Mago {self.nome} lançou um feitiço em {inimigo.nome} causando {dano} de dano.")
            
        inimigo.hp -= dano