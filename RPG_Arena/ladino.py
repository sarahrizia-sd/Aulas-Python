import random
from personagem import Personagem

class Ladino(Personagem):
    def __init__(self, nome):
        super().__init__(nome, 95)

    def atacar(self, inimigo):
        dano_base = 18
        critico = random.random() < 0.40  # 40% de chance
        
        if critico:
            dano = dano_base * 2
            print(f"💥 GOLPE FATAL! O Ladino {self.nome} atingiu o ponto fraco de {inimigo.nome} com {dano} de dano!")
        else:
            dano = dano_base
            print(f"🗡️ O Ladino {self.nome} esfaqueou {inimigo.nome} com {dano} de dano.")
            
        inimigo.hp -= dano