import tkinter as tk
from style import Style

class Functions:
    def añadir(entry, label, combobox, procedures, scrolledtext):
        try:
            cuantia = int(entry.get())
            for procedure in procedures:
                if combobox.get() == procedure:
                    if cuantia >= 18000:
                        for index in range(1, int(procedures[procedure])):
                            cuantia = cuantia * 0.8
                    else:
                        for index in range(1, int(procedures[procedure]) + 1):
                            cuantia = cuantia * 0.8
                    if int(procedures[procedure]) == 1:
                        cuantia = cuantia * (1 / 3)
                    if int(procedures[procedure]) >= 15:
                        cuantia = 18000
            scrolledtext.insert(tk.INSERT, f'{combobox.get()} - {entry.get()} - {round(cuantia)}\n')
            label.config(text=round(label.cget('text') + cuantia))
        except ValueError:
            Style.toplevel('200x75', 'Error', 'Por favor,\nIntroduce una cuantía válida', 17, 17)

    def limpiar(label, entry, scrolledtext):
        scrolledtext.delete(1.0, tk.END)
        entry.delete(0, tk.END)
        entry.insert(0, 18000)
        label.config(text=0)





        


        