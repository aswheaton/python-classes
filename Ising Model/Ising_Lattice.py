#! usr/bin/env/python

import matplotlib.pyplot as plt
import numpy as np

class Ising_Lattice(object):
    """
        Ising model lattice class object. Takes keyword arguments:

        temperature = Float, the temperature of the lattice.
        size        = Tuple, the size of the lattice (n,m).
        mode        = String, can be "r" for random mode or "m".
        animate     = Boolean, whether or not to animate the simulation.
    """

    def __init__(self, **kwargs):
        self.temp = kwargs.get("temperature")
        self.size = kwargs.get("size")
        self.mode = kwargs.get("mode")
        self.anim = kwargs.get("animate")
        self.build()

    def build(self):
        if self.mode == "r":
            self.lattice = np.random.random_integers(0, high=1, size=self.size)
        if self.mode == "m":
            self.lattice = np.ones(self.size, dtype=int)

    def bc(self, indices):
        """
            Determines if a pair of indices falls outside the boundary of the
            lattice and if so, applies a periodic (toroidal) boundary condition
            to return new indices.
        """
        if indices[0] < self.size[0]:
            n = self.size[0] - 1
        if indices[0] > self.size[0]:
            n = 0
        if indices[1] < self.size[1]:
            m = self.size[1] - 1
        if indices[1] > self.size[1]:
            m = 0
        return((n,m))

    def energy(self, indices):
        """
            Calculates and returns the energy of a given lattice site (n,m) due
            to spin interaction with its neighbors. Energy given by:
            E = - S_n,m * (S_n+1,m + Sn-1,m + S_n,m-1, + S_n,m+1)
        """
        energy = -2 * self.lattice[n,m] *
                    (self.lattice[self.bc(n-1, m)]
                    + self.lattice[self.bc(n+1,m)]
                    + self.lattice[self.bc(n, m-1)]
                    + self.lattice[self.bc(n, m+1)]
                    )
        return(energy)

    def step(self):
        """
            Randomly chooses a site on the lattice and tries to flip it.
        """
        indices = np.random.randint(0, self.size, 2)
        if self.energy(indices) <= 0.0:
            self.system[indices] *= -1
        elif np.exp(-self.energy(indices) / self.T) > np.random.rand():
            self.system[indices] *= -1

    def run(self):
        ani = animation.FuncAnimation(fig, self.step, self.lattice, blit=True, interval=10, repeat=False, init_func=init)
        plt.show()
