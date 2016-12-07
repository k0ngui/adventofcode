#!/usr/bin/env python3

import re

def check_ssl(path): 
    brackets = re.compile('\[\w*\]')
    aba = re.compile(r'(?=((\w)(?!\2)(\w)\2))')
    count = 0
    for a in open(path):
        supernet = ' '.join(brackets.split(a))
        hypernet = ' '.join(brackets.findall(a))
        for m in aba.findall(supernet):
            if m[0][1] + m[0][0] + m[0][1] in hypernet:
                count += 1
                break

    return count

if __name__ == '__main__':
    print('SSL support in', check_ssl('input.txt'), 'addresses.')

