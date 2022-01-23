from matplotlib.image import FigureImage
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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
        self.matplocanv()
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

    def matplocanv(self):
        f = Figure (figsize=(5,5), dpi = 100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8], [5,6,7,2,4,1,3,7])
        self.root.canvas = FigureCanvasTkAgg(f, self)
        self.root.canvas.show()
        self.root.canvas.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)
        #toolbar = NavigationToolbar2TkAgg (canvas, self)
        #canvas._tkcanvas.pack (side = TOP, fill = BOTH, expand = True)

Front()