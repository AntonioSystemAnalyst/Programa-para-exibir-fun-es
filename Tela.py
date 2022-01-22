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
        self.root.geometry("500x250+200+200")
        self.root.resizable(False, False)
        self.root.iconbitmap("imagens/icon.ico")
    
    def Labels(self):
        Label1 = Label(root, text = "Fibonaci")
        Label1.pack()

    def botoes(self):
        btn = Button(root, text = "Analise", command=sequencia)
        btn.pack()

    

Front()