import pandas as pd

# Dados fornecidos
identificador = ["tic18Py06894", "tic18Py06200", "tic18Py86399", "tic18Py05594", "tic18Py05800"]
idade = [29, 23, 24, 29, 23]
formação = [3, 2, 2, 3, 2]
formaçãoGeral = [1, 0, 0, 0, 0]
formaçãoEspecífica = ["Análise e Desenvolvimento de Sistemas", "Engenharia Química", "Engenharia Química", "Engenharia Mecânica", "Engenharia Química"]
andamentoGraduação = [78, 72, 70.16, None, 80]
tempoFormação = [None, None, None, 4, None]
experiênciaPrevia = [False, False, False, False, False]

# Criar um objeto Index usando a lista de identificadores
index = pd.Index(identificador)

# Criar objetos Series para cada lista
idade_series = pd.Series(idade, index=index)
formação_series = pd.Series(formação, index=index)
formaçãoGeral_series = pd.Series(formaçãoGeral, index=index)
formaçãoEspecífica_series = pd.Categorical(formaçãoEspecífica, categories=None, ordered=False)
andamentoGraduação_series = pd.Series(andamentoGraduação, index=index)
tempoFormação_series = pd.Series(tempoFormação, index=index)
experiênciaPrevia_series = pd.Series(experiênciaPrevia, index=index)

# Criar DataFrame
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

# Exibir DataFrame
print(df)
