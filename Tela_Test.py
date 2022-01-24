import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *

janela = Tk ()
janela.title ("GG")
janela.geometry ("600x400")


Figura = plt.Figure(figsize=(8, 4), dpi= 60)
ax = Figura.add_subplot (111)
canva =  FigureCanvasTkAgg(Figura, janela)
canva.get_tk_widget().grid(row=0, column=0)


cat = ["bored", "happy", "bored", "bored", "happy", "bored"]
dog = ["happy", "happy", "happy", "happy", "bored", "bored"]
activity = ["combing", "drinking", "feeding", "napping", "playing", "washing"]

ax.plot(activity, dog, label="dog")
ax.plot(activity, cat, label="cat")
ax.legend()






janela.mainloop()