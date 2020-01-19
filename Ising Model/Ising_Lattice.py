#! usr/bin/env/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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
            self.lattice = np.random.choice(a=[-1,1], size=self.size)
        if self.mode == "h":
            self.lattice = np.ones(self.size, dtype=int)
        if self.mode == "l":
            self.lattice = - np.ones(self.size, dtype=int)

    def bc(self, indices):
        """
            Determines if a pair of indices falls outside the boundary of the
            lattice and if so, applies a periodic (toroidal) boundary condition
            to return new indices.
        """
        # if indices[0] < 0:
        #     n = self.size[0] - 1
        # if indices[0] > self.size[0] - 1:
        #     n = 0
        # if indices[1] < 0:
        #     m = self.size[1] - 1
        # if indices[1] > self.size[1] - 1:
        #     m = 0
        # try:
        #     return((n,m))
        # except UnboundLocalError:
        #     return(indices)
        return((indices[0]%self.size[0], indices[1]%self.size[1]))

    def delta_energy(self, indices):
        """
            Calculates and returns the change in energy from flipping a given
            of a given lattice site (n,m) due to spin interaction with its
            neighbors. Change in energy given by:

            E = - S_n,m * (S_n+1,m + Sn-1,m + S_n,m-1, + S_n,m+1)

            Four other lattice points enter this expression.
        """

        n, m = indices
        delta_energy = 2 * self.lattice[n,m] * (
                    self.lattice[self.bc((n-1, m))]
                    + self.lattice[self.bc((n+1,m))]
                    + self.lattice[self.bc((n, m-1))]
                    + self.lattice[self.bc((n, m+1))]
                    )
        return(delta_energy)

    def attempt_flip(self):
        """
            Randomly chooses a site on the lattice and tries to flip it.
        """
        indices = (np.random.randint(0, self.size[0]), np.random.randint(0, self.size[1]))
        if self.delta_energy(indices) <= 0.0:
            self.lattice[indices] *= -1
        elif np.random.rand() < np.exp(-self.delta_energy(indices) / self.temp):
            self.lattice[indices] *= -1

    def animate(self, *args):
        self.attempt_flip()
        self.image.set_array(self.lattice)
        return(self.image,)

    def run(self, **kwargs):

        max_iter = kwargs.get("max_iter")

        self.figure = plt.figure()
        self.image = plt.imshow(self.lattice, animated=True)

        self.animation = animation.FuncAnimation(self.figure,self.animate,frames=max_iter,repeat=False,interval=0.001,blit=True)
        plt.show()

    def exportAnimation(self, filename, dotsPerInch):
        """
        Exports the animation to a .gif file without compression. (Linux
        distributions with package "imagemagick" only. Files can be large!)
        """
        self.animation.save(filename, dpi=dotsPerInch, writer="imagemagick")
