from pyxtal.crystal import Tol_matrix
from pyxtal import pyxtal

my_crystal = pyxtal()
my_crystal.from_random(3, 36, ['H2O'], [4], 1.0)
xtal = my_crystal.to_ase(resort=False)
print(xtal)
# my_crystal = pyxtal()
# my_crystal.from_random(3, 99, ['Ba','Ti','O'], [1,1,3])
# print(my_crystal)
# ase_structure  = my_crystal.to_ase()
# ase_structure.write('batiO.vasp',format='vasp',vasp5=True,direct=True)
# ase_struc = c.to_ase()
# pmg_struc = c.to_pymatgen()