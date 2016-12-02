#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def distance(data): 
    moves = []
    with open(data, 'r') as f:
        moves = f.read().rstrip().split(", ")

    # North, East, South, West
    orientations = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    o_i = 0
    position = (0, 0)

    for move in moves:
        o_i += 1 if (move[0] == 'R') else -1
        magnitude = tuple(int(move[1:]) * x for x in orientations[o_i % 4])
        position = tuple(map(sum, zip(position, magnitude)))

    print('Distance = {}'.format(sum(abs(x) for x in position)))

if __name__ == '__main__':
    distance('input.txt')

