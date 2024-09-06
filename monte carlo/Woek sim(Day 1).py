import matplotlib as mp 
import numpy as np 
sims= 100000

A = np.random.uniform(1, 5, sims)
B = np.random.uniform(2, 6, sims)

Duration = A+B 

mp.figure(figsize = (3, 1.5))
mp.hist(duration, density = True)
mp.axvline(9, color = "r")
mp.show()
print((duration > 9).sum()/sims)

