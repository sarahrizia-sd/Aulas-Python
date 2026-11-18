from guerreiro import Guerreiro
from mago import Mago
from ladino import Ladino

def criar_jogador(numero):
    while True:
        try:
            nome = input(f"\nDigite o nome do Jogador {numero}: ")
            print(f"Escolha a classe para {nome}:")
            print("[1] Guerreiro")
            print("[2] Mago")
            print("[3] Ladino")
            escolha = int(input("Opção: "))
            
            if escolha == 1:
                return Guerreiro(nome)
            elif escolha == 2:
                return Mago(nome)
            elif escolha == 3:
                return Ladino(nome)
            else:
                print("❌ Opção inválida. Escolha 1, 2 ou 3.")
        except ValueError:
            print("❌ Erro: Por favor, digite um número inteiro válido.")

def turno(atacante, defensor):
    print(f"\n--- Turno de {atacante.nome} (HP: {atacante.hp}/{atacante.hp_maximo}) ---")
    while True:
        try:
            print("Escolha sua ação:")
            print("[1] Atacar")
            print("[2] Usar Poção")
            acao = int(input("Opção: "))
            
            if acao == 1:
                atacante.atacar(defensor)
                break
            elif acao == 2:
                atacante.usar_pocao()
                break
            else:
                print("❌ Opção inválida. Escolha 1 ou 2.")
        except ValueError:
            print("❌ Erro: Por favor, digite apenas números.")

def main():
    print("="*30)
    print(" ARENA RPG ".center(30, "="))
    print("="*30)
    
    jogador1 = criar_jogador(1)
    jogador2 = criar_jogador(2)
    
    print("\n🔥 A BATALHA COMEÇOU! 🔥")
    
    rodada = 1
    while jogador1.hp > 0 and jogador2.hp > 0:
        print(f"\n=== RODADA {rodada} ===")
        
        # Turno Jogador 1
        turno(jogador1, jogador2)
        if jogador2.hp <= 0:
            break
            
        # Turno Jogador 2
        turno(jogador2, jogador1)
        
        rodada += 1
        
    print("\n🏆 FIM DE JOGO 🏆")
    if jogador1.hp > 0:
        print(f"O vencedor é {jogador1.nome}!")
    elif jogador2.hp > 0:
        print(f"O vencedor é {jogador2.nome}!")
    else:
        print("Empate épico!")

if __name__ == "__main__":
    main()