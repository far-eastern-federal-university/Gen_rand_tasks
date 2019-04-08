import numpy as np
import math 
from statistics import variance
r_1=np.random.uniform(0,1)
r_2=np.random.uniform(0,1)
eps_1=math.sqrt(-2*math.log(r_1))*np.sin(2*math.pi*r_2)
eps_2=math.sqrt(-2*math.log(r_1))*np.cos(2*math.pi*r_2)
print(eps_2, eps_1)

lst_eps1 = []
lst_eps2 = []
for i in range(10000):
    r_1=np.random.uniform(0,1)
    r_2=np.random.uniform(0,1)
    eps_1=math.sqrt(-2*math.log(r_1))*np.sin(2*math.pi*r_2)
    lst_eps1.append(eps_1)
    eps_2=math.sqrt(-2*math.log(r_1))*np.cos(2*math.pi*r_2)
    lst_eps2.append(eps_2)

print(np.mean(lst_eps1), np.var(lst_eps1), np.mean(lst_eps2), np.var(lst_eps2))
