#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from collections import Counter

def real_rooms(path): 
    r = re.compile('([a-z-]+)(\d+)\[([a-z]+)\]')
    rooms = [r.match(line).groups() for line in open(path)]
    for room in rooms:
        counts = Counter(room[0].replace('-', ''))
        s_counts = sorted(counts, key = lambda x: (-counts[x], x))
        if ''.join(s_counts[:5]) == room[2]:
            yield room

if __name__ == '__main__':
    print('Sum of sector IDs = {}'.format(
          sum([int(room[1]) for room in real_rooms('input.txt')])))

