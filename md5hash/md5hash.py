#!/usr/bin/env python3

import sys
import os
import hashlib
import time

BLOCKSIZE = 65536


class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print('Elapsed time: {:.3f} sec'.format(time.time() - self._startTime))


def md5(file_path):
    """Calculates the md5-hash of the file.
    :param file_path: full path to the file.
    """

    hasher = hashlib.md5()
    with Profiler():
        with open(file_path, 'rb') as f:
            while True:
                buf = f.read(BLOCKSIZE)
                if not buf:
                    break
                while len(buf) > 0:
                    hasher.update(buf)
                    buf = f.read(BLOCKSIZE)
        md5_hash = (hasher.hexdigest()).upper()
    return md5_hash


def size(full_path):
    """Shows file size.
    :param full_path: full path to the file.
    """

    file_size = os.path.getsize(full_path)
    str_file_size = str(file_size)
    print(str_file_size, 'b\n')

    # Show size in b, kb, mb or gb depending on the dimension
    if len(str_file_size) >= 10:
        print('{0:.2f}'.format(file_size / 1073741824), 'gb\n')
    elif len(str_file_size) >= 7:
        print('{0:.2f}'.format(file_size / 1048576), 'mb\n')
    elif len(str_file_size) >= 4:
        print('{0:.2f}'.format(file_size / 1024), 'kb\n')


def calculate(d):
    """Split the tuple (obtained from scan) to separate files.
       Alternately send full paths to the files in md5 and call it.
       :param d: tuple of files in the directory."""

    # Set correct slashes for the OS
    if sys.platform == 'windows':
        slash = '\\'
    elif sys.platform == 'linux':
        slash = '/'
    else:
        print('#Error. Unknown platform.')
        return

    print('Files in the current directory and their md5-hashes:\n')
    i = 0
    assert i == 0, '#Error. Variable i != 0.'

    for i in range(len(d[2])):  # Go through the list of files
        full_path = d[0]+slash+d[2][i]
        print(full_path)  # Get the list of files with full paths
        print(md5(full_path))
        size(full_path)


def scan(s=""):
    """Scan the directory and send the obtained tuple to calculate."""

    if s == "":
        tree = input('Enter the path to file or directory: ')
        tree = os.path.normpath(tree)
    else:
        tree = s
    assert os.path.exists(tree), "#Error. The path '{}' is invalid or doesn't exist.".format(str(tree))
    tree = os.walk(tree)
    for d in tree:
        print('...................')
        print('Current directory:')
        print(d[0])  # Current directory
        if d[2]:  # Empty directory check
            print('List of the files in the current directory:')
            print(d[2])  # Files in the current directory
            print()
        else:
            print('An empty directory.')
        calculate(d)

scan()
