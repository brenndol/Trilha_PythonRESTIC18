from abc import ABC, abstractmethod

class Data:
    def __init__(self, dia=1, mes=1, ano=2000):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia
    
    @dia.setter
    def dia(self, dia):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes(self, mes):
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__ano = ano
    
    def __str__(self):
        return "{}/{}/{}".format(self.__dia, self.__mes, self.__ano)

    def __eq__(self, outraData):
        return (self.__dia, self.__mes, self.__ano) == (outraData.__dia, outraData.__mes, outraData.__ano)
    
    def __lt__(self, outraData):
        return (self.__ano, self.__mes, self.__dia) < (outraData.__ano, outraData.__mes, outraData.__dia)
    
    def __gt__(self, outraData):
        return (self.__ano, self.__mes, self.__dia) > (outraData.__ano, outraData.__mes, outraData.__dia)


class AnaliseDados(ABC): 
    @abstractmethod
    def entrada_de_dados(self):
        pass

    @abstractmethod
    def mostra_mediana(self):
        pass
    
    @abstractmethod
    def mostra_menor(self):
        pass

    @abstractmethod
    def mostra_maior(self):
        pass
    
    @abstractmethod
    def listar_em_ordem(self):
        pass

    @abstractmethod
    def __iter__(self):
        pass


class ListaNomes(AnaliseDados):
    def __init__(self):
        self.__lista = []        

    def entrada_de_dados(self):
        try:
            quantidade = int(input("Quantos nomes deseja inserir? "))
            for _ in range(quantidade):
                nome = input("Digite o nome: ")
                self.__lista.append(nome)
        except ValueError:
            print("Erro: Insira um número válido para a quantidade.")

    def mostra_mediana(self):
        self.__lista.sort()
        tamanho = len(self.__lista)
        if tamanho % 2 == 0:
            indice1 = tamanho // 2 - 1
            indice2 = tamanho // 2
            mediana = self.__lista[indice1]  # Retorna o primeiro nome entre os dois no meio
        else:
            indice = tamanho // 2
            mediana = self.__lista[indice]  # Retorna o nome do meio
        return mediana

    def mostra_menor(self):
        return min(self.__lista)

    def mostra_maior(self):
        return max(self.__lista)

    def listar_em_ordem(self):
        return sorted(self.__lista)

    def __iter__(self):
        return iter(self.__lista)


class ListaDatas(AnaliseDados):
    def __init__(self):
        self.__lista = []        
    
    def entrada_de_dados(self):
        try:
            quantidade = int(input("Quantas datas deseja inserir? "))
            for _ in range(quantidade):
                while True:
                    try:
                        data_input = input("Digite a data no formato dd/mm/aaaa: ")
                        dia, mes, ano = map(int, data_input.split('/'))
                        data = Data(dia, mes, ano)
                        self.__lista.append(data)
                        break
                    except ValueError:
                        print("Erro: Insira uma data válida no formato dd/mm/aaaa.")
        except ValueError:
            print("Erro: Insira um número válido para a quantidade.")

    def mostra_mediana(self):
        self.__lista.sort()
        tamanho = len(self.__lista)
        if tamanho % 2 == 0:
            indice1 = tamanho // 2 - 1
            indice2 = tamanho // 2
            mediana = self.__lista[indice1]  # Retorna a primeira data entre as duas no meio
        else:
            indice = tamanho // 2
            mediana = self.__lista[indice]  # Retorna a data do meio
        return mediana

    def mostra_menor(self):
        return min(self.__lista)

    def mostra_maior(self):
        return max(self.__lista)

    def listar_em_ordem(self):
        return sorted(self.__lista)

    def __iter__(self):
        return iter(self.__lista)

    def __str__(self):
        return ', '.join(str(data) for data in self.__lista)


class ListaSalarios(AnaliseDados):
    def __init__(self):
        self.__lista = []        

    def entrada_de_dados(self):
        try:
            quantidade = int(input("Quantos salários deseja inserir? "))
            for _ in range(quantidade):
                while True:
                    try:
                        salario = float(input("Digite o salário: "))
                        if salario < 0:
                            raise ValueError("Salário não pode ser negativo.")
                        self.__lista.append(salario)
                        break
                    except ValueError:
                        print("Erro: Insira um valor de salário válido.")
        except ValueError:
            print("Erro: Insira um número válido para a quantidade.")

    def mostra_mediana(self):
        self.__lista.sort()
        tamanho = len(self.__lista)
        if tamanho % 2 == 0:
            indice1 = tamanho // 2 - 1
            indice2 = tamanho // 2
            mediana = (self.__lista[indice1] + self.__lista[indice2]) / 2  # Retorna a média entre os dois valores do meio
        else:
            indice = tamanho // 2
            mediana = self.__lista[indice]  # Retorna o valor do meio
        return mediana

    def mostra_menor(self):
        return min(self.__lista)

    def mostra_maior(self):
        return max(self.__lista)

    def listar_em_ordem(self):
        return sorted(self.__lista)

    def __iter__(self):
        return iter(self.__lista)


class ListaIdades(AnaliseDados):
    def __init__(self):
        self.__lista = []        
    
    def entrada_de_dados(self):
        try:
            quantidade = int(input("Quantas idades deseja inserir? "))
            for _ in range(quantidade):
                while True:
                    try:
                        idade = int(input("Digite a idade: "))
                        if idade < 0:
                            raise ValueError("Idade não pode ser negativa.")
                        self.__lista.append(idade)
                        break
                    except ValueError:
                        print("Erro: Insira uma idade válida.")
        except ValueError:
            print("Erro: Insira um número válido para a quantidade.")

    def mostra_mediana(self):
        self.__lista.sort()
        tamanho = len(self.__lista)
        if tamanho % 2 == 0:
            indice1 = tamanho // 2 - 1
            indice2 = tamanho // 2
            mediana = (self.__lista[indice1] + self.__lista[indice2]) / 2  # Retorna a média entre as duas idades do meio
        else:
            indice = tamanho // 2
            mediana = self.__lista[indice]  # Retorna a idade do meio
        return mediana

    def mostra_menor(self):
        return min(self.__lista)

    def mostra_maior(self):
        return max(self.__lista)

    def listar_em_ordem(self):
        return sorted(self.__lista)

    def __iter__(self):
        return iter(self.__lista)