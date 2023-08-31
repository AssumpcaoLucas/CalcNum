import numpy as np

f = lambda y: y - 0.9*np.sin(y)
df = lambda y: 1 - 0.9*np.cos(y)
error = 0.0001

def newRaph(x0):
    if abs(f(x0)) < error:
        return x0
    return newRaph(x0 - f(x0)/df(x0))

arr = []
for i in range(30):
    arr.append(np.pi*(i+1)/30)

result = map(newRaph, arr)

res = list(result)

for i in range(30):
    print (str(arr[i]) + " = " + str(res[i]))

