import random 
import math
from operator import add

def generate_data(datalen):
    x_train = [0]*datalen
    y_train = [0]*datalen
    for tick in range(datalen):
        sqrft =  random.randrange(15,35,1)/10
        floors = random.randrange(1,3,1)
        bedrooms = random.randrange(1,5,1)
        price = ((35000 * sqrft) + (30000 * floors) + (30000 * bedrooms)) + 25000 + random.randrange(-1000, 1000, 100)
        x_train[tick] = [sqrft,floors,bedrooms]
        y_train[tick] = price
    return x_train, y_train

def cost(x_train,y_train,w,b):
    m = len(y_train)
    n = len(x_train[0])
    cost = 0

    for i in range(m):
        f_wb_i = 0
        for j in range(n):
            f_wb_i += x_train[i][j] * w[j]
        f_wb_i += b

        cost += (f_wb_i - y_train[i])**2
    
    return cost / (2*m)

def findgradient(x_train,y_train,w,b):
    m = len(y_train)
    n = len(x_train[0])
    dj_dw = [0]*n
    dj_db = 0
    for i in range(m):
        f_wb_i = 0
        for j in range(n):
            f_wb_i += w[j]*x_train[i][j]
        f_wb_i += b
        dj_db += f_wb_i - y_train[i]
        for j in range(n):
            dj_dw[j] += (f_wb_i - y_train[i])*x_train[i][j]
        dj_dw[:] = [x / m for x in dj_dw]
    return dj_dw, dj_db/m

def rundescent(x_train,y_train,w,b,iterations,alpha):
    for i in range(iterations):
        dj_dw,dj_db = findgradient(x_train,y_train,w,b)
        alphader = [-x * alpha for x in dj_dw]
        w = list(map(add,w,alphader))
        b -= alpha *dj_db
        if i% math.ceil(iterations / 10) == 0:
            print("Iteration: " + str(i) + "  Cost: "+ str(cost(x_train,y_train,w,b)))
    return w,b


def main():
    x_train, y_train = generate_data(150)
    w,b = rundescent(x_train,y_train, [0,0,0], 0, 10000, 0.001)
    print("w: " + str(w) + "  b:" + str(b))
main()



