#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib, sys

def get_password(door):
    password = [''] * 8
    found = 0
    i = 0
    while found < 8:
        md5 = hashlib.md5((door + str(i)).encode()).hexdigest()
        if md5.startswith('00000') and md5[5].isdigit():
            pos = int(md5[5]) 
            if pos < 8 and password[pos] == '':
                password[pos] = md5[6]
                found += 1

        # Cool visualization :)
        if i % 10000 == 0:
            hax = [md5[i] if password[i] == '' else password[i] 
                   for i in range(len(password))]
            sys.stdout.write('>CRACKING: {}\r'.format(''.join(hax)))
            sys.stdout.flush()

        i += 1

    return ''.join(password)

if __name__ == '__main__':
    print("I'M IN: {}   ".format(get_password('cxdnnyjw')))

