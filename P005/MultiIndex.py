import pandas as pd

idade_series = [29, 23, 24, 29, 23, 24, 23, 24, 24, 27, 23, 22, 24]
formação_series = [3, 2, 2, 3, 2, 3, 2, 2, 2, 1, 1, 1, 2]
formaçãoGeral_series = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0]
formaçãoEspecífica_series = ["Análise e Desenvolvimento de Sistemas", "Engenharia Química", "Engenharia Química", "Engenharia Mecânica", "Engenharia Química", "Ciência da Computação", "Engenharia Elétrica", "Engenharia Química", "Engenharia Química", "Engenharia Química", "Ciência da Computação", "Ciência da Computação", "Engenharia Elétrica"]
andamentoGraduação_series = [78, 72, 70.16, None, 80, None, 90.16, 76.94, 75.58, 81.38, 0.66, 0.66, 0.99]
tempoFormação_series = [None, None, None, 4, None, 1, None, None, None, None, None, None, None]
experiênciaPrevia_series = [False, False, False, False, False, True, True, True, True, True, True, True, True]


data = {
    'Idade': idade_series,
    'Formação': formação_series,
    'Formação Geral': formaçãoGeral_series,
    'Formação Específica': formaçãoEspecífica_series,
    'Andamento Graduação': andamentoGraduação_series,
    'Tempo Formado (anos)': tempoFormação_series,
    'Experiência Prévia': experiênciaPrevia_series
}

df = pd.DataFrame(data)


trilhas = {
    "Python": ["tic18Py06894", "tic18Py06200", "tic18Py86399", "tic18Py05594", "tic18Py05800"],
    ".Net": ["tic18Py06799", "tic18Py07100", "tic18Py07799", "tic18Py08099", "tic18Py05996"],
    "Java": ["tic18Py08200", "tic18Py86001", "tic18Py05999"]
}


multi_index = pd.MultiIndex.from_tuples([(trilha, identificador) for trilha, ids in trilhas.items() for identificador in ids],
                                        names=["Trilha", "Identificador"])


df.set_index(multi_index, inplace=True)

# Extraindo informações do DataFrame com MultiIndex
print("Perfil dos alunos da residência:")
print(df)

# Agrupando por trilha e extraindo informações
for trilha, dados in df.groupby(level="Trilha"):
    print(f"\nPerfil dos alunos da trilha {trilha}:")
    print(dados)

