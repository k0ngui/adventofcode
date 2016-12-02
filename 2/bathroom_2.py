#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def bathroom_code(path): 
    data = []
    with open(path, 'r') as f:
        data = f.readlines()

    keypad = [['0', '0', '1', '0', '0'], 
              ['0', '2', '3', '4', '0'], 
              ['5', '6', '7', '8', '9'], 
              ['0', 'A', 'B', 'C', '0'],
              ['0', '0', 'D', '0', '0']]
    moves = { 'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0) }
    key = (2, 0)

    for line in data:
        for char in line.rstrip():
            new_key = tuple(map(lambda x: min(max(sum(x), 0), 4),
                                zip(moves[char], key)))
            if keypad[new_key[0]][new_key[1]] != '0':
                key = new_key

        yield keypad[key[0]][key[1]]

if __name__ == '__main__':
    print('Code = {}'.format(''.join(bathroom_code('input.txt'))))

