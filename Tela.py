import matplotlib.pyplot as plt
import random
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
plt.rcParams['figure.figsize'] = (13,7)
class Front():

    def comunicacao1 (self):
        x, y = linear_Func()
        ax.clear()
        ax.plot(x, y)
        canva.draw()
        self.Label1 = Label(self.root, text = "Função Linear", font='verdona-bold 11', bg='#000000', fg='#0000FF')
        self.Label1.place(relx=0.365, rely= 0.09, relwidth=0.40, relheight=0.1)
    
    def comunicacao2 (self):
        x, y = Parab_Func()
        ax.clear()
        ax.plot(x, y)
        canva.draw()
        self.Label1 = Label(self.root, text = "Função Parabólica", font='verdona-bold 11', bg='#000000', fg='#0000FF')
        self.Label1.place(relx=0.365, rely= 0.09, relwidth=0.40, relheight=0.1)
    
    def comunicacao3 (self):
        x, y = Logaritmo_Func ()
        ax.clear()
        ax.plot(x, y)
        canva.draw()
        self.Label1 = Label(self.root, text = "Função Logarítima", font='verdona-bold 11', bg='#000000', fg='#0000FF')
        self.Label1.place(relx=0.365, rely= 0.09, relwidth=0.40, relheight=0.1)
    
    def comunicacao4 (self):
        x, y = Exp_Func ()
        ax.clear()
        ax.plot(x, y)
        canva.draw()
        self.Label1 = Label(self.root, text = "Função Exponencial", font='verdona-bold 11', bg='#000000', fg='#0000FF')
        self.Label1.place(relx=0.365, rely= 0.09, relwidth=0.40, relheight=0.1)

    def Aleatorio(self):
        x = []
        y = []
        for i in range (50):
            rnd = random.randrange(1, 200) 
            x.append(rnd*i)
            y.append(i)
        ax.clear()
        ax.plot(x, y)
        canva.draw()
        self.Label1 = Label(self.root, text = "Função Aleatória", font='verdona-bold 11', bg='#000000', fg='#0000FF')
        self.Label1.place(relx=0.365, rely= 0.09, relwidth=0.40, relheight=0.1)
    
    def grafico(self):
        x = []
        y = []
        for i in range (50):
            rnd = random.randrange(1, 200) 
            x.append(rnd*i)
            y.append(i)
        ax.plot(x, y)
        ax.set_facecolor('xkcd:black')
       

    def __init__(self):
        self.root = root
        self.tela()
        self.Labels()
        self.botoes()
        self.grafico()
        root.mainloop()

    def tela(self):
        self.root.title('Finonaci')
        self.root.configure(background='#000000')
        self.root.geometry("710x370+200+200")
        self.root.resizable(False, False)
        self.root.iconbitmap("imagens/icon.ico")
    
    def Labels(self):
        self.Label1 = Label(self.root, text = "FIBONACI - Visualizador de Funções", font='verdona-bold 13', bg='#000000', fg='#0000FF')
        self.Label1.place(relx=0.015, rely= 0.01, relwidth=0.40, relheight=0.1)

        self.Label1 = Label(self.root, text = "Função Aleatória", font='verdona-bold 11', bg='#000000', fg='#0000FF')
        self.Label1.place(relx=0.365, rely= 0.09, relwidth=0.40, relheight=0.1)

    def botoes(self):
        self.btn1 = Button(self.root, text = "Linear", command=self.comunicacao1)
        self.btn1.place(relx=0.015, rely= 0.2, relwidth=0.15, relheight=0.1)

        self.btn2 = Button(self.root, text = "Parábola", command=self.comunicacao2)
        self.btn2.place(relx=0.015, rely= 0.32, relwidth=0.15, relheight=0.1)
    
        self.btn3 = Button(self.root, text = "Logarítma", command=self.comunicacao3)
        self.btn3.place(relx=0.015, rely= 0.435, relwidth=0.15, relheight=0.1)
        
        self.btn4 = Button(self.root, text = "Exponencial", command=self.comunicacao4)
        self.btn4.place(relx=0.015, rely= 0.559, relwidth=0.15, relheight=0.1)

        self.btn4 = Button(self.root, text = "Aleatório", command=self.Aleatorio)
        self.btn4.place(relx=0.015, rely= 0.679, relwidth=0.15, relheight=0.1)
     
Front()