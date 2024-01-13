from os import sys
from utils import clear, menu, get_input, bars
from Questoes import Questoes;

def main_app():
    # Definindo questoes
    opcoes = [
        "Sair",
        "Questão 1A",
        "Questão 1B",
        "Questão 2A",
        "Questão 2B I",
        "Questão 2B II",
        "Questão 2B III",
        "Questão 2B IV",
        "Questão 2B V"
        ]
    
    while True:
        # Limpando tela
        clear()
        # Mostrando menu
        menu(title="Menu de Questões", params=opcoes)
        # Pegando opção do usuário
        escolha = get_input("Escolha uma das opções acima, pelo número listado: ")
        # Verificando opções escolhidas
        if (escolha.isdigit()) and (int(escolha) in range(0, len(opcoes))):
            escolha = int(escolha)
            if escolha == 0: 
                print("Saindo...")
                bars(size=50)
                return
            # Instânciando questoes
            q = Questoes()
            # Colocar questao 1 aqui
            if escolha == 1:   q.Questao1_A()
            elif escolha == 2: q.Questao1_B()
            elif escolha == 3: q.Quastao2_A()
            elif escolha == 4: q.Questao2_B_1()
            elif escolha == 5: q.Questao2_B_2()
            elif escolha == 6: q.Questao2_B_3()
            elif escolha == 7: q.Questao2_B_4()
            elif escolha == 8: q.Questao2_B_5()
        else:
            get_input(f"Por favor, digite um número válido [0, {len(opcoes)-1}]\nPressione ENTER para continuar...")
            
if __name__ == "__main__":
    main_app()