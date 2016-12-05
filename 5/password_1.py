#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib

def get_password(door):
    password = []
    i = 0
    while len(password) < 8:
        md5_hash = hashlib.md5((door + str(i)).encode()).hexdigest()
        if md5_hash.startswith('00000'):
            password.append(md5_hash[5])
        i += 1

    return ''.join(password)

if __name__ == '__main__':
    print('Password =', get_password('cxdnnyjw'))

