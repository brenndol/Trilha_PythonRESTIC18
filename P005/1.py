identificador = ["tic18Py06894", "tic18Py06200", "tic18Py86399", "tic18Py05594", "tic18Py05800"]
idade = [29, 23, 24, 29, 23]
formação = [3, 2, 2, 3, 2]
formaçãoGeral = [1, 0, 0, 0, 0]
formaçãoEspecífica = ["Análise e Desenvolvimento de Sistemas", "Engenharia Química", "Engenharia Química", "Engenharia Mecânica", "Engenharia Química"]
andamentoGraduação = [78, 72, 70.16, None, 80]
tempoFormação = [None, None, None, 4, None]
experiênciaPrevia = [False, False, False, False, False]

# Imprimir as informações de cada usuário com porcentagem no campo "Andamento da Graduação"
for i in range(len(identificador)):
    print(f"Usuário {i + 1}:")
    print("Identificador:", identificador[i])
    print("Idade:", idade[i])
    print("Formação:", formação[i])
    print("Formação Geral:", formaçãoGeral[i])
    print("Formação Específica:", formaçãoEspecífica[i])

    if andamentoGraduação[i] is not None:
        print("Andamento da Graduação: {:.2f}%".format(andamentoGraduação[i]))
    else:
        print("Andamento da Graduação: Não aplicável")

    print("Tempo de Formado em anos:", tempoFormação[i])
    print("Experiência Prévia:", experiênciaPrevia[i])
    print()
