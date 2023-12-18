from __init__ import *

def percorrer_listas_com_zip(lista_nomes, lista_salarios):
    for nome, salario in zip(lista_nomes, lista_salarios):
        print(f"{nome}: R${salario}")

def calcular_folha_com_reajuste(lista_salarios):
    for salario in lista_salarios:
        print(f"Novo salário com reajuste de 10%: R${salario * 1.1:.2f}")

def modificar_datas_anteriores_a_2019(lista_datas):
    for data in lista_datas:
        if data < Data(1, 1, 2019):
            data.dia = 1
    print("Datas modificadas com sucesso!")

def iterador_zip(lista_nomes, lista_salarios):
    percorrer_listas_com_zip(lista_nomes, lista_salarios)

def iterador_map(lista_salarios):
    calcular_folha_com_reajuste(lista_salarios)

def iterador_filter(lista_datas):
    modificar_datas_anteriores_a_2019(lista_datas)

def menu():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    while True:
        print("\n Menu Principal \n")
        print("1. Incluir nome na lista de nomes.")
        print("2. Incluir salário na lista de salários.")
        print("3. Incluir data na lista de datas.")
        print("4. Incluir idade na lista de idades.")
        print("5. Percorrer listas de nomes e salários.")
        print("6. Calcular o valor da folha com um reajuste de 10%.")
        print("7. Modificar o dia das datas anteriores a 2019.")
        print("8. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nomes.entrada_de_dados()
        elif opcao == "2":
            salarios.entrada_de_dados()
        elif opcao == "3":
            datas.entrada_de_dados()
        elif opcao == "4":
            idades.entrada_de_dados()
        elif opcao == "5":
            iterador_zip(nomes, salarios)
        elif opcao == "6":
            iterador_map(salarios)
        elif opcao == "7":
            iterador_filter(datas)
        elif opcao == "8":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()