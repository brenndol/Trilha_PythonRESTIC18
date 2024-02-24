import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Selecione o Ano")
        
        self.year_label = tk.Label(root, text="Selecione o ano:")
        self.year_label.pack()
        
        self.year_var = tk.StringVar(root)
        self.year_dropdown = tk.OptionMenu(root, self.year_var, "")
        self.year_dropdown.pack()
        
        self.fetch_years_button = tk.Button(root, text="Buscar anos disponíveis", command=self.fetch_years)
        self.fetch_years_button.pack()

    def fetch_years(self):
        try:
            page = requests.get("https://portal.inmet.gov.br/dadoshistoricos")
            soup = BeautifulSoup(page.content, 'html.parser')
            options = [option.text for option in soup.find(id="anos").find_all("option")]
            self.year_var.set('') # Reset previous selection
            self.year_dropdown['menu'].delete(0, 'end') # Clear previous menu
            for option in options:
                self.year_dropdown['menu'].add_command(label=option, command=tk._setit(self.year_var, option))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao buscar anos disponíveis: {str(e)}")

def run_gui():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()
