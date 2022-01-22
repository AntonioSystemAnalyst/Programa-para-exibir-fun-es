import matplotlib.pyplot as plt
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

