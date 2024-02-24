import os
import requests
import tkinter as tk
from tkinter import ttk, messagebox
import zipfile
from bs4 import BeautifulSoup

class SegundoPrototipoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Seleção de Ano e Estação")

        self.year_label = ttk.Label(root, text="Selecione o ano:")
        self.year_label.grid(row=0, column=0, padx=5, pady=5)

        self.year_var = tk.StringVar(root)
        self.year_dropdown = ttk.Combobox(root, textvariable=self.year_var)
        self.year_dropdown.grid(row=0, column=1, padx=5, pady=5)

        self.station_label = ttk.Label(root, text="Selecione a estação:")
        self.station_label.grid(row=1, column=0, padx=5, pady=5)

        self.station_var = tk.StringVar(root)
        self.station_dropdown = ttk.Combobox(root, textvariable=self.station_var)
        self.station_dropdown.grid(row=1, column=1, padx=5, pady=5)

        self.fetch_years_button = ttk.Button(root, text="Buscar anos disponíveis", command=self.buscar_ano)
        self.fetch_years_button.grid(row=0, column=2, padx=5, pady=5)

        self.fetch_stations_button = ttk.Button(root, text="Buscar estações disponíveis", command=self.buscar_estacao)
        self.fetch_stations_button.grid(row=1, column=2, padx=5, pady=5)

    def buscar_ano(self):
        try:
            page = requests.get("https://portal.inmet.gov.br/dadoshistoricos")
            page.raise_for_status()  
            years = self.extrair_ano(page.content)
            self.year_dropdown['values'] = years
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao buscar anos disponíveis: {str(e)}")

    def extrair_ano(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        options = [option.text for option in soup.find(id="anos").find_all("option")]
        return options

    