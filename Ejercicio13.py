import numpy
import numpy as np
n,m = map(int,input().split())

e=np.zeros((n,m),int)
c=np.zeros((n,m),int)
for i in range(n):
  e[i]=np.array(input().split(),int)
for i in range(n):
  c[i]=np.array(input().split(),int)  

print(e+c)
print(e-c)
print(e*c)
print(np.array(e/c,int))
print(e%c)
print(e**c)
#Array Mathematics