#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def possible_triangles(path): 
    triangles = []
    with open(path, 'r') as f:
        triangles = [[int(x) for x in l.rstrip().split()] for l in f.readlines()]
    triangles = [sorted(c[i:i + 3]) for c in zip(*triangles) for i in range(0, len(c), 3)]
    return sum([t[0] + t[1] > t[2] for t in triangles])

if __name__ == '__main__':
    print('Possible triangles = {}'.format(possible_triangles('input.txt')))

