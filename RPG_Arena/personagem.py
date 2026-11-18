class Personagem:
    def __init__(self, nome, hp_maximo):
        self.nome = nome
        self.hp_maximo = hp_maximo
        self.hp = hp_maximo

    def atacar(self, inimigo):
        pass

    def usar_pocao(self):
        cura = 20
        if self.hp + cura > self.hp_maximo:
            self.hp = self.hp_maximo
        else:
            self.hp += cura
        print(f"🧪 {self.nome} usou uma poção e recuperou HP! (HP atual: {self.hp}/{self.hp_maximo})")