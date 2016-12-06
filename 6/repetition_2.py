#!/usr/bin/env python3

from collections import Counter

def get_message(path): 
    messages = [list(line.rstrip()) for line in open(path)]
    return ''.join(Counter(c).most_common()[-1][0] for c in zip(*messages))

if __name__ == '__main__':
    print('Message =', get_message('input.txt'))

