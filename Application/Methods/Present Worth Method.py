def Net_Present_Worth(Initial_Cost:float, i:float, n:float,*Annual_Cash_Flow):
    myList = list(Annual_Cash_Flow)
    i = i/100
    NPW = 0
    for x in range(n):
        NPW += (myList[x])/((1+i)**x+1)
