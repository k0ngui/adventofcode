#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def bathroom_code(path): 
    data = []
    with open(path, 'r') as f:
        data = f.readlines()

    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    moves = { 'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0) }
    key = (1, 1)

    for line in data:
        for char in line.rstrip():
            key = tuple(map(lambda x: min(max(sum(x), 0), 2),
                            zip(moves[char], key)))
        yield str(keypad[key[0]][key[1]])


if __name__ == '__main__':
    print('Code = {}'.format(''.join(bathroom_code('input.txt'))))

