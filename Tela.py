from distutils import command
from tkinter import *
from tkinter import ttk
from Funcoes import sequencia

root = Tk()

class Front():
    def __init__(self):
        self.root = root
        self.tela()
        self.Labels()
        self.botoes()
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
        self.btn1 = Button(self.root, text = "Linear", command=sequencia)
        self.btn1.place(relx=0.015, rely= 0.2, relwidth=0.15, relheight=0.1)

        self.btn2 = Button(self.root, text = "Parabola", command=sequencia)
        self.btn2.place(relx=0.015, rely= 0.32, relwidth=0.15, relheight=0.1)
    
        self.btn3 = Button(self.root, text = "Logaritma", command=sequencia)
        self.btn3.place(relx=0.015, rely= 0.435, relwidth=0.15, relheight=0.1)
        
        self.btn4 = Button(self.root, text = "Exponenical", command=sequencia)
        self.btn4.place(relx=0.015, rely= 0.559, relwidth=0.15, relheight=0.1)
Front()