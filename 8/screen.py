#!/usr/bin/env python3

import re
import numpy as np

def simulate(path): 
    screen = np.zeros((6, 50), dtype=np.int)
    for line in open(path):
        v = [int(x) for x in re.findall(r'\d+', line)]
        if 'rect' in line:
            screen[:v[1], :v[0]] = np.full((v[1], v[0]), 1, dtype=np.int)
        elif 'column' in line:
            screen[:, v[0]] = np.roll(screen[:, v[0]], v[1])
        elif 'row' in line:
            screen[v[0]] = np.roll(screen[v[0]], v[1])
        
    return screen

if __name__ == '__main__':
    screen = simulate('input.txt')
    np.set_printoptions(linewidth=120)
    print('Pixels on =', np.sum(screen))
    print(screen)

