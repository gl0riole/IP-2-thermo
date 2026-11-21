import time
import numpy as np

start = time.time()

N = int(1e5)
array = np.zeros(N, dtype = float)


for i in range(N):
    array[i] = np.random.rand()
    
eind = time.time()
lengte = eind - start

print(lengte)