identificador = []
idade = []
formacao = []
formacaoGeral = []
formacaoEspecifica = []
andamentoGraduacao = []
tempoFormacao = []
experienciaPrevia = []

# Função para coletar informações de um membro da equipe
def coletar_informacoes():
    identificador = input("Digite os 3 primeiros do CPF e os 2 ultimos da data de nascimento. Identificador (tic18PyXXXXX) : ")

    # Verificar se o identificador tem 5 dígitos, sendo os 3 primeiros do CPF e os 2 últimos da data de nascimento
    if len(identificador) != 5 or not identificador.isdigit() or int(identificador[:3]) > 999 or int(identificador[3:]) > 99:
        print("Erro: Identificador inválido. Deve ter 5 dígitos (3 do CPF, 2 da data de nascimento). Tente novamente.")
        return coletar_informacoes()

    idade = int(input("Idade: "))
    formacao = int(input("Formação (0 - Técnica, 1 - Técnica Graduação em andamento, 2 - Graduação em andamento, 3 - Graduação concluída): "))

    # Verificar se a formação é 0, 1, 2 ou 3
    if formacao not in [0, 1, 2, 3]:
        print("Erro: Formação deve ser 0, 1, 2 ou 3. Tente novamente.")
        return coletar_informacoes()

    if formacao != 0:
        formacaoGeral = int(input("Área de formação geral (0 - Engenharia, 1 - Computação): "))

        # Verificar se a área de formação geral é 0 ou 1
        if formacaoGeral not in [0, 1]:
            print("Erro: Área de formação geral deve ser 0 ou 1. Tente novamente.")
            return coletar_informacoes()

        formacaoEspecifica = input("Área de formação específica: ")
    else:
        formacaoGeral = None
        formacaoEspecifica = None

    if formacao == 1 or formacao == 2:
        andamentoGraduacao = float(input("Andamento da graduação (% concluído): "))
        tempoFormacao = None
    elif formacao == 3:
        andamentoGraduacao = None
        tempoFormacao = int(input("Tempo de formado (anos): "))
    else:
        andamentoGraduacao = None
        tempoFormacao = None

    experienciaPrevia = input("Tinha experiência prévia em programação? (True ou False): ").lower()

    # Verificar se a experiência prévia é True ou False
    if experienciaPrevia not in ['true', 'false']:
        print("Erro: Experiência prévia deve ser True ou False. Tente novamente.")
        return coletar_informacoes()

    experienciaPrevia = experienciaPrevia == 'true'

    return identificador, idade, formacao, formacaoGeral, formacaoEspecifica, andamentoGraduacao, tempoFormacao, experienciaPrevia

# Coleta de informações para 3 membros da equipe
for _ in range(3):
    info = coletar_informacoes()

    identificador.append(info[0])
    idade.append(info[1])
    formacao.append(info[2])
    formacaoGeral.append(info[3])
    formacaoEspecifica.append(info[4])
    andamentoGraduacao.append(info[5])
    tempoFormacao.append(info[6])
    experienciaPrevia.append(info[7])

# Imprimir as listas
print("Identificadores:", identificador)
print("Idades:", idade)
print("Formações:", formacao)
print("Áreas de formação geral:", formacaoGeral)
print("Áreas de formação específica:", formacaoEspecifica)
print("Andamento da graduação:", andamentoGraduacao)
print("Tempo de formado:", tempoFormacao)
print("Experiência prévia:", experienciaPrevia)
