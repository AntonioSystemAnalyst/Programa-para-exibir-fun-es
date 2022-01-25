import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from Funcoes import *

try:
    from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg
except ImportError:
    from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk as NavigationToolbar2TkAgg

root = Tk()

Figura = plt.Figure(figsize=(8, 4), dpi= 60)
ax = Figura.add_subplot (111)
canva =  FigureCanvasTkAgg(Figura, root)
canva.get_tk_widget().place(relx=0.25, rely= 0.2)
toolbar = NavigationToolbar2TkAgg (canva, root)
canva._tkcanvas.place(relx=0.25, rely= 0.2)


resultado = [1, 2, 3, 4, 5]

class Front():

    def comunicacao1 (self):
       
        resultado = linear_Func()
        Y = [1, 2, 7, 6, 8, 9]
        X = [0, 1, 2, 3, 4, 5]
        Y =  resultado
        i = 0

        ax.clear()
        ax.plot(X, Y)
        ax.legend()
        canva.draw()
    
    def comunicacao2 (self):
        x, y = Parab_Func()
        ax.clear()
        ax.plot(x, y)
        ax.legend()
        canva.draw()
        print (' ------------------- aq:')
        print (x)
        print (' -------------------')
        print (y)

    def __init__(self):
        self.root = root
        self.tela()
        self.Labels()
        self.botoes()
        self.grafico()
        root.mainloop()

    def tela(self):
        self.root.title('Finonaci')
        self.root.configure(background='#207293')
        self.root.geometry("730x390+200+200")
        self.root.resizable(False, False)
        self.root.iconbitmap("imagens/icon.ico")
    
    def Labels(self):
        self.Label1 = Label(self.root, text = "FIBONACI - Visualizador de Funções", font='verdona-bold 10', bg='#207293', fg='#000000')
        self.Label1.place(relx=0.015, rely= 0.05, relwidth=0.30, relheight=0.1)

    def botoes(self):
        self.btn1 = Button(self.root, text = "Linear", command=self.comunicacao1)
        self.btn1.place(relx=0.015, rely= 0.2, relwidth=0.15, relheight=0.1)

        self.btn2 = Button(self.root, text = "Parabola", command=self.comunicacao2)
        self.btn2.place(relx=0.015, rely= 0.32, relwidth=0.15, relheight=0.1)
    
        self.btn3 = Button(self.root, text = "Logaritma")
        self.btn3.place(relx=0.015, rely= 0.435, relwidth=0.15, relheight=0.1)
        
        self.btn4 = Button(self.root, text = "Exponenical", command="")
        self.btn4.place(relx=0.015, rely= 0.559, relwidth=0.15, relheight=0.1)
    
    def grafico(self):
        Y = resultado
        X = [1, 2, 3, 4, 5]
        ax.scatter(X, Y)
        ax.legend()
         
Front()