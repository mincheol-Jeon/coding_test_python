# s = 'hello!'
# print(s[0])
# print(s[0:1])
# print(s[-6:])
# print(s[-6:-1])
# print(s[-6])

# y = 'leebyunhun'
# print(y[:3])

import numpy as np

nda = np.arange(24).reshape(4,3,2)
ndb = np.arange(6).reshape(3,2)
ndc = np.arange(3).reshape(3,1)

print(nda)
print('-'*5)
print(ndb)
print('-'*5)
print(ndc)
print('-'*5)
print(nda+ndb)
print('-'*20)
print(nda+ndb-ndc)
