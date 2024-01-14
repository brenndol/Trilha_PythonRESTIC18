import numpy as np

class ListaNotas:
    def __init__(self, nAlunos=30, nCreditos=3):
        self._nAlunos = nAlunos
        self._nCreditos = nCreditos
        self._notas = None

    def _verificar_notas_lidas(self):
        if self._notas is None:
            print("Notas não foram lidas. Utilize o método leNotas() primeiro.")
            return False
        return True

    def leNotas(self):
        print(f"Digite as notas para {self._nAlunos} alunos:")
        self._notas = np.zeros((self._nAlunos, self._nCreditos), dtype=float)
        for i in range(self._nAlunos):
            while True:
                try:
                    nota = float(input(f"Nota do aluno {i + 1}: "))
                    if 0.0 <= nota <= 10.0:
                        self._notas[i] = nota
                        break
                    else:
                        print("Digite uma nota válida entre 0.0 e 10.0")
                except ValueError:
                    print("Digite uma nota válida.")

    def _calcular_media(self, array, axis=None):
        return np.mean(array, axis=axis)

    def mediaTurma(self):
        if not self._verificar_notas_lidas():
            return None
        return self._calcular_media(self._notas)

    def mediaAluno(self, index=0):
        if not self._verificar_notas_lidas():
            return None
        return self._calcular_media(self._notas[:, index])

    def mediaAvaliacao(self, index=0):
        if not self._verificar_notas_lidas():
            return None
        return self._calcular_media(self._notas[:, index])

    def quantAprovados(self):
        if not self._verificar_notas_lidas():
            return None
        return np.sum(self._calcular_media(self._notas, axis=1) >= 6)

    def quantReprovados(self):
        if not self._verificar_notas_lidas():
            return None
        return np.sum(self._calcular_media(self._notas, axis=1) < 6)

    def menorNota(self):
        if not self._verificar_notas_lidas():
            return None
        return np.min(self._notas, axis=0), np.min(self._calcular_media(self._notas, axis=1))

    def maiorNota(self):
        if not self._verificar_notas_lidas():
            return None
        return np.max(self._notas, axis=0), np.max(self._calcular_media(self._notas, axis=1))

    def menorNotaMediaFinal(self):
        if not self._verificar_notas_lidas():
            return None
        return np.min(self._calcular_media(self._notas, axis=1))

    def maiorNotaMediaFinal(self):
        if not self._verificar_notas_lidas():
            return None
        return np.max(self._calcular_media(self._notas, axis=1))

    def __str__(self):
        if not self._verificar_notas_lidas():
            return "Notas não foram lidas. Utilize o método leNotas() primeiro."
        return f"Notas da turma:\n{self._notas}"

if __name__ == "__main__":
    turma = ListaNotas()
    turma.leNotas()

    index_aluno = 0
    index_avaliacao = 0

    media_aluno = turma.mediaAluno(index_aluno)
    media_avaliacao = turma.mediaAvaliacao(index_avaliacao)
    quant_aprovados = turma.quantAprovados()
    quant_reprovados = turma.quantReprovados()
    menor_nota = turma.menorNota()
    maior_nota = turma.maiorNota()
    menor_nota_media_final = turma.menorNotaMediaFinal()
    maior_nota_media_final = turma.maiorNotaMediaFinal()

    print(f"Média do aluno {index_aluno + 1}: {media_aluno}")
    print(f"Média na avaliação {index_avaliacao + 1}: {media_avaliacao}")
    print(f"Quantidade de aprovados: {quant_aprovados}")
    print(f"Quantidade de reprovados: {quant_reprovados}")
    print(f"Menor nota: {menor_nota}")
    print(f"Maior nota: {maior_nota}")
    print(f"Menor nota na média final: {menor_nota_media_final}")
    print(f"Maior nota da média final: {maior_nota_media_final}")
    print(str(turma))
