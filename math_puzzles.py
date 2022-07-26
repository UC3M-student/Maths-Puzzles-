from cmath import sqrt
from itertools import permutations

"""
#Problem2: What three square numbers add up to 125?
x = list(range(0,13,1))
comb = list(permutations(x,3))

lst = []

for i in comb:
    result_ = i[0]**2 + i[1]**2 + i[2]**2
    if result_ == 125:
        lst.append(i)
print("What three square numbers add up to 125? The results is:  ", lst)
"""
#############################################################################################
"""
#Problem1: What two square numbers add up to 36.482 ?

y = list(range(0,192,1))
comb2 = list(permutations(y,2))
lst2 = []

for y in comb2:
    result_2 = y[0]**2 + y[1]**2
    if result_2 == 36482:
        lst2.append(y)

print("What two square numbers add up to 36482? The results is:  ", lst2)
"""
#############################################

#Problem3: What two whole numbers add upp to 16 and multiply to 55?
"""
z = list(range(0,17,1))
comp3 = list(permutations(z,2))
lst3 = []

for xy in comp3:
    if (xy[0] + xy[1] == 16) & (xy[0]*xy[1] ==55):
        lst3.append(xy)

print(lst3)
"""
#############################################

#Problem4: What two prime numbers multiply to 3071?

"""
lst_prime_numbers = []
for i in range(2,1000):
    x = 0
    for y in range(2,i):
        if i%y ==0:
            x +=1
    if x == 0:
        lst_prime_numbers.append(i)


comp4 = list(permutations(lst_prime_numbers,2))
lst4 = []

for i in comp4:
    if i[0]*i[1] == 3071:
        lst4.append(i)

print(lst4)

"""

############################################

#Problem5: List all the pairs of prime numbers(<100) which add up to a square number. Example: 11 + 4 = 16 = 4*4

"""
lst_prime_numbers = []
for i in range(2,100):
    x = 0
    for y in range(2,i):
        if i%y ==0:
            x +=1
    if x == 0:
        lst_prime_numbers.append(i)

comp5 = list(permutations(lst_prime_numbers,2))

for i in comp5:
    if sqrt(i[0]+i[1]) in range(1,100,1):
        print(i)

"""
