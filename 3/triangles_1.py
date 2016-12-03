#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def possible_triangles(path): 
    triangles = []
    with open(path, 'r') as f:
        triangles = [sorted([int(x) for x in l.rstrip().split()]) for l in f.readlines()]
    return sum([t[0] + t[1] > t[2] for t in triangles])

if __name__ == '__main__':
    print('Possible triangles = {}'.format(possible_triangles('input.txt')))

