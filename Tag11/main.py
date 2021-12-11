import numpy as np
from collections import deque
from scipy import ndimage

from numpy.core.fromnumeric import shape

def firstTask():

    octopoden = np.genfromtxt("input_test.txt", delimiter=1, dtype=int)
    steps = 100
    flashes = 0
    for s in range(steps):
        flashed = np.zeros(shape=shape(octopoden), dtype=bool)
        octopoden[octopoden > 9] = 0
        octopoden += 1
        flashes, octopoden = flashing(octopoden, flashed, flashes)
        print(flashes)
        octopoden[octopoden > 9] = 0
        print(octopoden)
    print(flashes)


def flashing(octopoden, flashed, flashes):
        energyLevelReached = octopoden > 9
        newToFlash = np.logical_xor(flashed,energyLevelReached)
        if not newToFlash.any():
            return flashes, octopoden
        flashes += sum(sum(newToFlash))
        paddedNewToFlash = np.pad(newToFlash, pad_width=1, constant_values=0)
        paddedOctoPoden = np.pad(octopoden, pad_width=1, constant_values=0)
        columns, rows = np.where(paddedNewToFlash)
        for i in range(len(columns)):
            paddedOctoPoden[columns[i]-1][rows[i]-1] += 1
            paddedOctoPoden[columns[i]-1][rows[i]] += 1
            paddedOctoPoden[columns[i]-1][rows[i]+1] += 1
            paddedOctoPoden[columns[i]][rows[i]-1] += 1
            paddedOctoPoden[columns[i]][rows[i]+1] += 1
            paddedOctoPoden[columns[i]+1][rows[i]-1] += 1
            paddedOctoPoden[columns[i]+1][rows[i]] += 1
            paddedOctoPoden[columns[i]+1][rows[i]+1] += 1
        # structure = ndimage.generate_binary_structure(2, 2)
        # flashRadius = ndimage.binary_dilation(newToFlash, structure=structure)
        octopoden = paddedOctoPoden[1:-1, 1:-1]
        flashed = np.logical_or(flashed, newToFlash)
        return flashing(octopoden, flashed, flashes)
        

        





if __name__ == "__main__":
    firstTask()