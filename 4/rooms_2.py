#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re, string
from collections import Counter

def real_rooms(path): 
    r = re.compile('([a-z-]+)(\d+)\[([a-z]+)\]')
    rooms = [r.match(line).groups() for line in open(path)]
    for room in rooms:
        counts = Counter(room[0].replace('-', ''))
        s_counts = sorted(counts, key = lambda x: (-counts[x], x))
        if ''.join(s_counts[:5]) == room[2]:
            yield room

def decrypt_caesar(ciphertext, shift):
    alphabet = string.ascii_lowercase
    shift = int(shift) % len(alphabet)
    ciphertext = ciphertext[:-1].replace('-', ' ')
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    return ciphertext.translate(str.maketrans(alphabet, shifted_alphabet))

if __name__ == '__main__':
    for room in real_rooms('input.txt'):
        if decrypt_caesar(room[0], room[1]) == 'northpole object storage':
            print('North Pole objects here:', room)

