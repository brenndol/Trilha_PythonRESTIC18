import pandas as pd

class Residente:
    def __init__(self, codigo, idade, formacao, formacao_geral, andamento_grad, tempo_formacao, exp_programacao):
        self.codigo = f"{tipo_trilha}{cpf[:3]}{ano_nascimento[-2:]}" 
        self.idade = 2024 - int(ano_nascimento)
        self.formacao = self._mapear_formacao(formacao)
        self.formacao_geral = formacao_geral
        self.andamento_grad = andamento_grad if not tempo_formacao else None
        self.tempo_formacao = tempo_formacao if not andamento_grad else None
        self.exp_programacao = exp_programacao
     
    # garantindo que o campo andamento_grad e tempo_formacao sejam excludentes.   
    def _mapear_formacao(self, formacao):
        mapeamento = {'Engenharia': 1, 'Computação': 2}
        return mapeamento.get(formacao, None)

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
  