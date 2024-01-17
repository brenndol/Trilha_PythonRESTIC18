import pandas as pd

class Residente:
    def __init__(self, codigo, idade, formacao, formacao_geral, andamento_grad, tempo_formacao, exp_programacao):
        self.codigo = codigo
        self.idade = idade
        self.formacao = formacao
        self.formacao_geral = formacao_geral
        self.andamento_grad = andamento_grad
        self.tempo_formacao = tempo_formacao
        self.exp_programacao = exp_programacao

class Trilha:
    def __init__(self, identificador):
        self.identificador = identificador
        self.dados = pd.DataFrame(columns=['Código', 'Idade', 'Formação', 'Formação Geral', 'Andamento Graduação', 'Tempo Formação', 'Exp Programação'])

class Residencia:
    def __init__(self):
        self.trilhas = {
            'Python': Trilha('tic18Py'),
            'Java': Trilha('tic18Jav'),
            '.NET': Trilha('tic18Net')
        }