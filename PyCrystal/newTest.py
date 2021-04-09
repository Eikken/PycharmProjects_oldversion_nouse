from ase import Atoms
from pyxtal import pyxtal


# my_crystal = pyxtal()
# my_crystal.from_random(3, 99, ['Ba','Ti','O'], [1,1,3])
# print(my_crystal)
c = pyxtal()
c.from_random(3, 225, ['C'], [16])
ase_struc = c.to_ase()
pmg_struc = c.to_pymatgen()
ase_struc.write('1.vasp', format='vasp', vasp5=True, direct=True)
ase_struc.write('1.xyz', format='extxyz')
print(ase_struc * 2)
print(ase_struc)
print(pmg_struc)
# C1.from_random(3, 227, ['C'], [8])
# from pyxtal.crystal import random_cluster
#
# from random import choice
#
# pgs = range(1 , 33)
# clusters = []
# for i in range(100) :
#     run = True
#     while run :
#         pg = choice ( pgs )
#         cluster = random_cluster (pg , ['C'], [36])
#         if cluster.valid :
#             clusters.append( cluster )