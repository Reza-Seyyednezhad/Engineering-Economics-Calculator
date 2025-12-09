from math import pow, log

# **********************************************************************************
# A: یک سری پرداخت های یکسان
# P: ارزش فعلی
# F: اصل و فرع


def F_P(i:float, n:int, P:float=0):
    i = i/100
    result1 = (pow((1+i), n)) 
    if P > 0:
        result2 = P * result1
    else:
        result2 = 0
    return result1, result2

# **********************************************************************************
# print("F_P: ",F_P(0.25, 25))
# print(F_P(6,3,200))
# print("-----------------------")
# print(F_P(6,10,200))
# **********************************************************************************

def P_F(i:float, n:int, F:float=0):
    i = i/100
    result1 = (1/(pow((1+i), n)))
    if F > 0:
        result2 = F * result1
    else:
        result2 = 0
    return result1, result2

# **********************************************************************************
# print("P_F: ",P_F(0.25, 25))
# print(P_F(4,48))
# **********************************************************************************

def P_A(i:float, n:int, A:float=0):
    i = i/100
    result1 = ((pow((1+i), n)) - 1)/(i * (pow((1+i), n)))
    if A > 0:
        result2 = A * result1
    else:
        result2 = 0
    return result1, result2

# **********************************************************************************
# print("P_A: ",P_A(0.25, 25))
# print(P_A(13,42))
# **********************************************************************************

def A_P(i:float, n:int, P:float=0):
    i = i/100
    result1 = (i * (pow((1+i), n)))/((pow((1+i), n)) - 1)
    if P > 0:
        result2 = P * result1
    else:
        result2 = 0
    return result1, result2 

# **********************************************************************************
# print("A_P: ",A_P(0.25, 25))
# **********************************************************************************

def A_F(i:float, n:int, F:float=0):
    i = i/100
    result1 = (i / ((pow((1+i), n)) - 1))
    if F > 0:
        result2 = F * result1
    else:
        result2 = 0
    return result1, result2

# **********************************************************************************
# print("A_F: ",A_F(0.25, 25))
# **********************************************************************************

def F_A(i:float, n:int, A:float=0):
    i = i/100
    result1 = (((pow((1+i), n)) - 1)/ i)
    if A > 0:
        result2 = A * result1
    else:
        result2 = 0
    return result1, result2 

# **********************************************************************************
# print("F_A: ",F_A(0.25, 25))
# **********************************************************************************

def P_G(i:float, n:int, G:float=0):
    i = i/100
    result1 = (((pow(1+i, n) - 1)/(i * pow(1+i, n)))- (n/(pow(1+i, n))))/i
    if G>0:
        result2 = G * result1
    else:
        result2 = 0
    return result1, result2 
# **********************************************************************************
# print("P_G: ",P_G(0.25, 25))
# **********************************************************************************


def A_G(i:float, n:int, G:float=0):
    i = i/100
    result1 = (1/i) - (n/(pow(1+i, n) - 1))
    if G>0:
        result2 = G * result1
    else:
        result2 = 0
    return result1, result2 

# **********************************************************************************
# print("A_G: ",A_G(0.25, 25))
# **********************************************************************************

def i_P_F(P, F, n):
    result1 = F/P
    result2 = (pow(result1, (1/n))) - 1
    return result2


# print(i_P_F(300000, 500000, 5))

def rule_72(n):
    return 72 / n


def n_F_P(F,P, i):
    i = i/100
    return (log(F/P)/log(i + 1))

# print(n_F_P(20000,10000,5))

x = [(1,1000,25),(5,62,455),(31,522,32),(500,300,400)]


# x.sort(key=lambda x: x[2])

import operator

y = x.sort()
# print(sorted(x, key=operator.itemgetter(2)))
summ = 0

for i in sorted(x, key=operator.itemgetter(2)):
    # print(i[2])
    summ += i[2]
    # print("**********")

# print(summ)
# print(880 + 32)