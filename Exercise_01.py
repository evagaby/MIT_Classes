import numpy as np
a = []
for i in range(0,5): 
    c = i + 5 
    a.append(c)
print(a)

num = [1,2,4,5]
b = []
for i in num:
    c = i*3
    b.append(c)
print(b)

inter = np.intersect1d(a,b)
union = np.union1d(a,b)
minus = np.setdiff1d(a,b)
print(minus,union, inter)



