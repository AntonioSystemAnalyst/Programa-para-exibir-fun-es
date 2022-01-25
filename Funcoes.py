import random
from re import X
from tkinter import Y
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math

def cmd_click ():
    print ('Hello World!')
def sequencia ():
    p = 1
    n = 0
    result = 0
    qtd = 0
    vetx = []
    vety = []
    for i in range(1000):
        result = p + n
        p = n
        n = result     
        vety.append(result)
        vetx.append(i) 
        print ('Result: {} - {}'.format(i, result))
        if result % 2 != 0:
            qtd = qtd + 1
         
    print ("qtd: {}".format(qtd + 1))
    plt.scatter(vetx, vety)
    plt.show()


def linear_Func():  # y = x + 1 rnd em x inicial 
    result = [1, 2, 3, 4, 5, 6]
    rnd = random.randrange (1,10)
    ax = random.randrange(1,10)
    i = 0
    for i in range (6):
        if ax % 2 == 0:
            result[i] = rnd - i
        else:
            result[i] = rnd + i 
    return result

def Parab_Func():  # y = ax^2 + bx + c 

    a = random.randrange(1, 10)
    b = random.randrange(1, 10)
    c = random.randrange(1, 10)
    x = -b/(2*a)
    y = -1*(b*b-(4*a*c))/(4*a)
    resultx = [1, 2, 3, 4, 5, 7, 8]
    resulty = [1, 2, 3, 4, 5, 7, 8]
    resultx [4] = x 
    resulty [4] = y 
    i = 5
    for i in range (3):
        resultx[i] = x + i
        resulty[i] = y + i
    return resultx, resulty
    











    
    




    

      

