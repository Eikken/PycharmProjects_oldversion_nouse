# from pyxtal import pyxtal
# my_crystal = pyxtal()
# my_crystal.from_random(3, 36, ['H2O'], [4], 1.0)
# # random_crystal(group, species, numIons, factor, lattice, sites, conventional, tm)
# # xtal = my_crystal.to_ase(resort=False)
# ordered_xtal = my_crystal.to_ase()
# print(ordered_xtal)
# print(xtal)
from scipy.special import comb, perm

import itertools
count = 0
dic = {'A':[1,1,1],'B':[1,0,1]
       }
for i in itertools.combinations('ABCDEFGHIJKL', 2):
    tmp = list(i)
    print(tmp)
#     count+=1
# print(count)
# print(perm(3, 2))
# for i in range(8):
#     print("C 12 i",comb(12, i))
#     #展示 abcdefghijk的排列，把a(1,1,1)全排列