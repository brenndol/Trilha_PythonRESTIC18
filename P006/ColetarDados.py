<<<<<<< HEAD
import os
from ClassResidente import Residente, Trilha, Residencia
=======
>>>>>>> 8db0eb11a99214a047c5a905e05dc65f1f854dfa
import pandas as pd

def coletar_dados_residente():
    codigo = input("Digite o código do residente: ")
    idade = int(input("Digite o ano de nascimento do residente: "))
    formacao = int(input("Digite o código da formação: (1 para Engenharia, 2 para Computação)"))
    formacao_geral = bool(input("Qual a formação geral (True/False): "))
    andamento_grad = input("Digite o andamento da graduação do residente: ")
    tempo_formacao = int(input("Digite o tempo total de formação do residente (em anos): "))
    exp_programacao = int(input("Em uma escala de 1 a 5, qual é sua experiência prévia em programação? (1 - Iniciante, 5 - Avançado): "))

    # Validar se o usuário forneceu ambos os campos
    if andamento_grad and tempo_formacao:
        print("Erro: Os campos 'Andamento Graduação' e 'Tempo Formação' são excludentes. Forneça apenas um deles.")
        return None

    return Residente(codigo, idade, formacao, formacao_geral, andamento_grad, tempo_formacao, exp_programacao)

<<<<<<< HEAD

def salvar_dados_csv(trilha):
    trilha.dados.to_csv(f"{trilha.identificador}.csv", index=False)

def carregar_dados_csv(trilha):
    if os.path.exists(f"{trilha.identificador}.csv"):
        trilha.dados = pd.read_csv(f"{trilha.identificador}.csv")

def main():
    residencia = Residencia()

for trilha_nome, trilha_obj in residencia.trilhas.items():
        # Carregar dados do CSV se existirem
        carregar_dados_csv(trilha_obj)

while True:
=======
def main():
    residencia = Residencia()

    while True:
>>>>>>> 8db0eb11a99214a047c5a905e05dc65f1f854dfa
        print("Escolha a trilha:")
        print("1. Python")
        print("2. Java")
        print("3. .NET")
        print("0. Sair")

        escolha = input("Digite o número da trilha ou 0 para sair: ")

        if escolha == '0':
<<<<<<< HEAD
# Salvar dados antes de sair
            for trilha_nome, trilha_obj in residencia.trilhas.items():
                salvar_dados_csv(trilha_obj)
=======
>>>>>>> 8db0eb11a99214a047c5a905e05dc65f1f854dfa
            break

        trilha = None
        if escolha == '1':
            trilha = residencia.trilhas['Python']
        elif escolha == '2':
            trilha = residencia.trilhas['Java']
        elif escolha == '3':
            trilha = residencia.trilhas['.NET']
        else:
            print("Escolha inválida. Tente novamente.")
            continue

        residente = coletar_dados_residente()
        trilha.dados = trilha.dados.append(pd.Series(vars(residente)), ignore_index=True)

    for trilha_nome, trilha_obj in residencia.trilhas.items():
        print(f"\nTrilha: {trilha_nome}")
        print(trilha_obj.dados)

if __name__ == "__main__":
    main()