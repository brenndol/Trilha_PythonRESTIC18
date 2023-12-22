#Utilizando NumPy

# Para gerar um ndarray com valores inteiros aleatórios dentro de um intervalo, você pode usar a função numpy.random.randint. Por exemplo:

import numpy as np

idade_minima = 18
idade_maxima = 65
tamanho_lista = 100

ListaIdade = np.random.randint(idade_minima, idade_maxima + 1, tamanho_lista)

#Da mesma forma, para valores de ponto flutuante aleatórios, você pode usar numpy.random.uniform:

salario_minimo = 2000.0
salario_maximo = 8000.0

ListaSalario = np.random.uniform(salario_minimo, salario_maximo, tamanho_lista)

# Para calcular a mediana, o valor mínimo e máximo de um ndarray, você pode usar as funções numpy.median, numpy.min e numpy.max:

mediana_idade = np.median(ListaIdade)
valor_minimo_idade = np.min(ListaIdade)
valor_maximo_idade = np.max(ListaIdade)

mediana_salario = np.median(ListaSalario)
valor_minimo_salario = np.min(ListaSalario)
valor_maximo_salario = np.max(ListaSalario)
