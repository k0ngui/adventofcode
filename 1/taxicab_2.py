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
    visited = set()

    for move in moves:
        o_i += 1 if (move[0] == 'R') else -1
        magnitude = orientations[o_i % 4]

        for i in range(int(move[1:])):
            position = tuple(map(sum, zip(position, magnitude)))
            if position in visited:
                print('Distance = {}'.format(sum(abs(x) for x in position)))
                return
            visited.add(position)

if __name__ == '__main__':
    distance('input.txt')

