import tkinter as tk
from gui import WeatherApp
from segprot import segPrototipo

def run_gui():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()
    segPrototipo()
