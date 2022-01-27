import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy 

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
    x = []
    y = []
    rnd = random.randrange (1,10)
    ax = random.randrange(1,10)
    i = 0
    for i in range (6):
        if ax % 2 == 0:
            x.append(rnd - i)
        else:
            x.append(rnd + i)
        y.append(i)   
    return  x, y

def Parab_Func():  # y = ax^2 + bx + c 

    ax = random.randrange(1,10)
    if ax%2 == 0:
        a = random.randrange(1, 10)
    else:
        a =-1*random.randrange(1, 10)
    b = random.randrange(0, 10)
    c = random.randrange(0, 10)
    x = -1*b/(2*a)
    y = -1*((b*b)-(4*a*c))/(4*a)
    resultx = []
    resulty = []
    for i in range (200):
        if i < 100:
            resultx.append(x - (98-i))
            resulty.append(((a*resultx[i]*resultx[i]) + (b*resultx[i]) + c)) 
        if i > 100:
            resultx.append(x + (i-100))
            resulty.append(((a*resultx[i]*resultx[i]) + (b*resultx[i]) + c)) 
        if i == 100:
             resulty.append(y)
             resultx.append(x)    
    return resultx, resulty


def Logaritmo_Func ():
    y = []
    x = []
    rnd = random.randrange(1, 11)
    for i in range (100):
        if rnd % 2 == 0:
             x.append(-1*numpy.log(rnd+i))
        else:
             x.append(numpy.log(rnd+i))
        y.append(i)  
    return x, y

def Exp_Func ():
    y = []
    x = []
    rnd = random.randrange(1, 11)
    for i in range (100):
        if rnd % 2 == 0:  
            x.append((-1*(rnd+i)*(rnd+i)))
        else:
            x.append(((rnd+i)*(rnd+i)))
        y.append(i)
    return x, y 


   
    











    
    




    

      

