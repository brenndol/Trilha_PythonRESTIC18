import pandas as pd

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
andamentoGraduação_series = pd.Series(andamentoGraduação, index=index)
tempoFormação_series = pd.Series(tempoFormação, index=index)
experiênciaPrevia_series = pd.Series(experiênciaPrevia, index=index)

# Análise 1: Idade média, membros mais jovens e membros mais velhos
idade_media = idade_series.mean()
membros_mais_jovens = idade_series[idade_series == idade_series.min()].index.tolist()
membros_mais_velhos = idade_series[idade_series == idade_series.max()].index.tolist()

print(f"Idade média dos membros da equipe: {idade_media:.2f} anos")
print(f"Membros mais jovens: {', '.join(membros_mais_jovens)}")
print(f"Membros mais velhos: {', '.join(membros_mais_velhos)}\n")

# Análise 2: Predominância de técnicos, graduandos ou graduados
perfil_formação = {
    0: "Técnico",
    1: "Graduando",
    2: "Graduado"
}

perfil_formação_counts = formação_series.map(perfil_formação).value_counts()

print("Perfil de formação dos membros:")
for perfil, count in perfil_formação_counts.items():
    print(f"{perfil}: {count} membros")

print()

# Análise 3: Engenheiros ou formados em cursos de computação
formação_geral_counts = formaçãoGeral_series.map({0: "Engenheiro", 1: "Computação"}).value_counts()

print("Formação geral dos membros:")
for formacao, count in formação_geral_counts.items():
    print(f"{formacao}: {count} membros")
