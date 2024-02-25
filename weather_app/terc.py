import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

def extrair_dados_mensais(html_content):
    # Inicializa listas para armazenar os dados de precipitação e temperatura média:
    precipitacao_mensal = []
    temperatura_media_mensal = []

    # Analisa o conteúdo HTML com BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Encontra a tabela que contém os dados mensais
    table = soup.find('table', class_='tabela_padrao')

    # Verifica se a tabela foi encontrada
    if table:
        # Encontra todas as linhas da tabela, exceto o cabeçalho
        linhas = table.find_all('tr')[1:]

        # Itera sobre as linhas da tabela
        for linha in linhas:
            # Extrai os dados de cada coluna da linha
            colunas = linha.find_all('td')
            # A segunda coluna contém os dados de precipitação
            precipitacao = float(colunas[1].text.strip().replace(',', '.'))
            precipitacao_mensal.append(precipitacao)
            # A terceira coluna contém os dados de temperatura média
            temperatura = float(colunas[2].text.strip().replace(',', '.'))
            temperatura_media_mensal.append(temperatura)

    return precipitacao_mensal, temperatura_media_mensal

def obter_estacoes():
    url = "https://portal.inmet.gov.br/dadoshistoricos"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        select_estacoes = soup.find('select', id='sel_station')
        options = select_estacoes.find_all('option')
        estacoes = [option.text.strip() for option in options]
        return estacoes
    else:
        print("Falha ao obter as estações. Status code:", response.status_code)
        return []

def obter_anos(estacao):
    url = f"https://portal.inmet.gov.br/dadoshistoricos?p_p_id=dadoshistoricos&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_dadoshistoricos_WAR_dadoshistoricosportlet_javax.portlet.action=geraGraficoHistorico&p_p_col_id=column-2&p_p_col_count=1&_dadoshistoricos_WAR_dadoshistoricosportlet_codigo={estacao}&_dadoshistoricos_WAR_dadoshistoricosportlet_javax.portlet.action=geraGraficoHistorico"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        select_anos = soup.find('select', id='sel_date_year')
        options = select_anos.find_all('option')
        anos = [option.text.strip() for option in options]
        return anos
    else:
        print("Falha ao obter os anos. Status code:", response.status_code)
        return []

def obter_dados(estacao, ano):
    url = f"https://portal.inmet.gov.br/dadoshistoricos?p_p_id=dadoshistoricos&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_dadoshistoricos_WAR_dadoshistoricosportlet_javax.portlet.action=geraGraficoHistorico&p_p_col_id=column-2&p_p_col_count=1&_dadoshistoricos_WAR_dadoshistoricosportlet_codigo={estacao}&_dadoshistoricos_WAR_dadoshistoricosportlet_ano={ano}&_dadoshistoricos_WAR_dadoshistoricosportlet_mes="
    response = requests.get(url)
    if response.status_code == 200:
        precipitacao, temperatura = extrair_dados_mensais(response.content)
        return precipitacao, temperatura
    else:
        print("Falha ao obter os dados. Status code:", response.status_code)
        return [], []

def gerar_grafico_precipitacao(precipitacao):
    plt.plot(range(1, 13), precipitacao, marker='o')
    plt.xlabel('Mês')
    plt.ylabel('Precipitação (mm)')
    plt.title('Precipitação Mensal')
    plt.grid(True)
    plt.show()

def gerar_grafico_temperatura(temperatura):
    plt.plot(range(1, 13), temperatura, marker='o', color='r')
    plt.xlabel('Mês')
    plt.ylabel('Temperatura (°C)')
    plt.title('Temperatura Média Mensal')
    plt.grid(True)
    plt.show()

def gerar_graficos():
    estacao = estacao_combobox.get()
    ano = ano_combobox.get()

    precipitacao, temperatura = obter_dados(estacao, ano)
    gerar_grafico_precipitacao(precipitacao)
    gerar_grafico_temperatura(temperatura)

app = tk.Tk()
app.title('Gerador de Gráficos Meteorológicos')

frame = ttk.Frame(app, padding='10')
frame.grid(row=0, column=0)

estacao_label = ttk.Label(frame, text='Estação:')
estacao_label.grid(row=0, column=0, sticky='w')

estacoes = obter_estacoes()
estacao_combobox = ttk.Combobox(frame, values=estacoes, state='readonly')
estacao_combobox.grid(row=0, column=1)

ano_label = ttk.Label(frame, text='Ano:')
ano_label.grid(row=1, column=0, sticky='w')

anos = []
ano_combobox = ttk.Combobox(frame, values=anos, state='readonly')
ano_combobox.grid(row=1, column=1)

def on_estacao_select(event):
    estacao = estacao_combobox.get()
    anos = obter_anos(estacao)
    ano_combobox['values'] = anos

estacao_combobox.bind('<<ComboboxSelected>>', on_estacao_select)

gerar_button = ttk.Button(frame, text='Gerar Gráficos', command=gerar_graficos)
gerar_button.grid(row=2, columnspan=2)

app.mainloop()
