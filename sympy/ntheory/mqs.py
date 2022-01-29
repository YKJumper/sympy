from sympy.core.numbers import igcd, mod_inverse
from sympy.core.power import integer_nthroot
from sympy.ntheory.residue_ntheory import _sqrt_mod_prime_power
from sympy.ntheory import isprime
from sympy.ntheory import qs
from math import log, sqrt
from decimal import Decimal
from datetime import datetime
from math import log, sqrt
from decimal import Decimal
from datetime import datetime
# import random

# rgen = random.Random()

# from joblib import Parallel, delayed
# def process(R, i):
#     if integer_nthroot(R, i)[1]:
#         return 0
#     else:
#         return i




# results = Parallel(n_jobs=4)(delayed(process)(i) for i in range(2, 30))
# print(results)  # prints [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

N = 25645121643901801
m = sqrt(Decimal(N))
M = 50
for i in range(1,M):
    Rm = int(((m+i)**2) % N)
    print ("i=", i, ": ", Rm, ": ", qs(Rm, 2000, 1000), end=";\n")



# N = 0x3082010a0282010100be409df46ee1ea76871c4d45448ebe46c883069dc12afe181f8ee402faf3ab5d508a16310b9a06d0c57022cd492d5463ccb66e68460b53eacb4c24c0bc724eeaf115aef4549a120ac37ab23360e2da8955f32258f3dedccfef8386a28c944f9f68f29890468427c776bfe3cc352c8b5e07646582c048b0a891f9619f762050a891c766b5eb78620356f08a1a13ea31a31ea099fd38f6f62732586f07f56bb8fb142bafb7aaccd6635f738cda0599a838a8cb17783651ace99ef4783a8dcf0fd942e2980cab2f9f0e01deef9f9949f12ddfac744d1b98b547c5e529d1f99018c7629cbe83c7267b3e8a25c7c0dd9de6356810209d8fd8ded2c3849c0d5ee82fc90203
# S = sieve.primerange(2, 30)
# for i in S:
#     print("Power=", i, end=" \n")
#     P_root = integer_nthroot(N, i)
#     for j in range(501,5000):
#         R_rest = (P_root[0]+j)**i % N
#         results = Parallel(n_jobs=7, prefer="threads")(delayed(process)(R_rest, k) for k in range(2, 30))
#         if 0 in results:
#             print("j=", j, end=";\n")

# S = sieve.primerange(2, 2)
# for prime in S:
#     print("Prime = ", prime)
#     Imin = round(log(N, prime)) + 1
#     Imax = 2*Imin + 1
#     for i in range(Imin,Imax):
#         R = N % prime**i
#         if R == 0:
#             print("i = ", i)
#             break

            

"""
print (qs(25645121643901801, 2000, 10000))
print (qs(340282366920938463463374607431768211457, 2000, 10000)) <--2**128+1
print (qs(340282366920938463463374607431768211457*25645121643901801, 2000, 10000))
print (qs(0x3082010a0282010100be409df46ee1ea76871c4d45448ebe46c883069dc12afe181f8ee402faf3ab5d508a16310b9a06d0c57022cd492d5463ccb66e68460b53eacb4c24c0bc724eeaf115aef4549a120ac37ab23360e2da8955f32258f3dedccfef8386a28c944f9f68f29890468427c776bfe3cc352c8b5e07646582c048b0a891f9619f762050a891c766b5eb78620356f08a1a13ea31a31ea099fd38f6f62732586f07f56bb8fb142bafb7aaccd6635f738cda0599a838a8cb17783651ace99ef4783a8dcf0fd942e2980cab2f9f0e01deef9f9949f12ddfac744d1b98b547c5e529d1f99018c7629cbe83c7267b3e8a25c7c0dd9de6356810209d8fd8ded2c3849c0d5ee82fc90203, 2000, 10000))
print (qs(0x3082010a0282010100be409df46ee1ea76871c4d454, 0x20000, 0x1000)) --> 1134308329036989866337357649190002837825416381912148
{1995077197595492, 2274214412162259291574722201940738676, 4} -- Takes 18:21:53.548006 --> 21:13:57.613757 
"""