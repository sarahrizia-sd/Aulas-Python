import random
from personagem import Personagem

class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, 120)

    def atacar(self, inimigo):
        dano_base = 15
        critico = random.random() < 0.20  # 20% de chance
        
        if critico:
            dano = dano_base * 2
            print(f"💥 GOLPE CRÍTICO! O Guerreiro {self.nome} dizimou {inimigo.nome} com {dano} de dano!")
        else:
            dano = dano_base
            print(f"⚔️ O Guerreiro {self.nome} atacou {inimigo.nome} com {dano} de dano.")
            
        inimigo.hp -= dano