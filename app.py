from style import Style
from procedures import Procedures
from functions import Functions

procedures = Procedures.procedures('procedures.csv')

root = Style.root('600x300', 'Cálculo de Honorarios', 'CAB_logo.ico')

Style.label(root, 'Cuantía del procedimiento:', 20, 75)
entry = Style.entry(root, 10, 175, 75, 18000)
Style.label(root, '€', 250, 75)

combobox = Style.combobox(root, procedures, 40, 20, 152)

Style.image(root, 'CAB_image.jpg', (53, 50), 300, 50)
añadir = Style.button(root, 'Añadir', 8, 300, 150, lambda: Functions.añadir(entry, total, combobox, procedures, scrolledtext))
limpiar = Style.button(root, 'Limpiar', 8, 300, 225, lambda: Functions.limpiar(total, entry, scrolledtext))

scrolledtext = Style.scrolledtext(root, 25, 7, 370, 55)
Style.label(root, 'Total:', 370, 228)
total = Style.label(root, 0, 475, 228)
Style.label(root, '€', 565, 228)

root.mainloop()