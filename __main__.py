#!/usr/bin/env python

# Copyright (c) 2013 "OKso http://okso.me"
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


from __future__ import print_function

import os
import hashlib
import base64
import getpass

# Python3 input() compatibility:
try:
    input = raw_input
except NameError:
    pass

LEN = 32


def hash(*keys):
    merge = b'-'.join(keys)
    hashed = hashlib.sha512(merge).digest()
    rebased = base64.b64encode(hashed)
    return rebased[:32]


def read_secret_file():
    path = os.path.join(os.getenv('HOME'), '.mip.key')
    return open(path, 'rb').read()


def ask_for_locker():
    lock = getpass.getpass('locker: ')
    lock2 = getpass.getpass('locker (again): ')
    while lock != lock2:
        print('Inputs do not match. Try again')
        lock = getpass.getpass('locker: ')
        lock2 = getpass.getpass('locker: ')
    return lock


def main():
    hidden = read_secret_file()
    lock = ask_for_locker()
    while True:
        paint = input('paint: ')
        print(hash(paint, lock, hidden))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
