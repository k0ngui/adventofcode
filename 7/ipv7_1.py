#!/usr/bin/env python3

import re

def check_tls(path): 
    abba_bkt = re.compile(r'\[\w*(\w)(?!\1)(\w)\2\1\w*\]')
    abba = re.compile(r'(\w)(?!\1)(\w)\2\1') 
    return sum([re.search(abba_bkt, a) == None and 
                re.search(abba, a) != None for a in open(path)])

if __name__ == '__main__':
    print('TLS support in', check_tls('input.txt'), 'addresses.')

