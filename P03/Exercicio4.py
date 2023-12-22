import numpy as np

class ListaNotas:
    def _init_(self):
        self.disciplinas = {}

    def adicionar_disciplina(self, nome_disciplina):
        if nome_disciplina in self.disciplinas:
            print(f"A disciplina '{nome_disciplina}' já está cadastrada.")
        else:
            self.disciplinas[nome_disciplina] = np.array([], dtype=float)

    def adicionar_nota(self, nome_disciplina, nota):
        if nota < 0 or nota > 10:
            raise ValueError("A nota deve estar entre 0 e 10.")
        if nome_disciplina in self.disciplinas:
            self.disciplinas[nome_disciplina] = np.append(self.disciplinas[nome_disciplina], nota)
        else:
            print(f"A disciplina '{nome_disciplina}' não está cadastrada. Adicione-a antes de adicionar notas.")

    def mostrar_notas(self, nome_disciplina):
        if nome_disciplina in self.disciplinas:
            return self.disciplinas[nome_disciplina]
        print(f"A disciplina '{nome_disciplina}' não está cadastrada.")
        return np.array([])

    def mediana_disciplina(self, nome_disciplina):
        if nome_disciplina in self.disciplinas:
            if self.disciplinas[nome_disciplina].size > 0:
                return np.median(self.disciplinas[nome_disciplina])
            else:
                print(f"Não há notas registradas para a disciplina '{nome_disciplina}'.")
        else:
            print(f"A disciplina '{nome_disciplina}' não está cadastrada.")
        return None

    def media_disciplina(self, nome_disciplina):
        if nome_disciplina in self.disciplinas:
            if self.disciplinas[nome_disciplina].size > 0:
                return np.mean(self.disciplinas[nome_disciplina])
            else:
                print(f"Não há notas registradas para a disciplina '{nome_disciplina}'.")
        else:
            print(f"A disciplina '{nome_disciplina}' não está cadastrada.")
        return None
