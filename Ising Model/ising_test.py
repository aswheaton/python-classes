from Ising_Lattice import Ising_Lattice
import matplotlib.pyplot as plt

lattice = Ising_Lattice(temperature=1.5, size=(100,100), mode="r", animate=True)
lattice.run(dynamic="kawasaki", max_iter=10000)
