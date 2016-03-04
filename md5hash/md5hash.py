#!/usr/bin/env python3

import sys
import os
import hashlib

BLOCKSIZE = 65536


def md5(file_path):
    """Calculates the md5-hash of the file.
    :param file_path: full path to the file.
    """

    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        while True:
            buf = f.read(BLOCKSIZE)
            if not buf:
                break
            while len(buf) > 0:
                hasher.update(buf)
                buf = f.read(BLOCKSIZE)
    md5_hash = hasher.hexdigest().upper()
    return md5_hash


def size(full_path):
    """Shows file size.
    :param full_path: full path to the file.
    """

    file_size = os.path.getsize(full_path)
    str_file_size = str(file_size)
    print(str_file_size, 'b')

    # Show size in b, kb, mb or gb depending on the dimension
    if len(str_file_size) >= 10:
        print('{0:.2f}'.format(file_size / 1073741824), 'gb')
    elif len(str_file_size) >= 7:
        print('{0:.2f}'.format(file_size / 1048576), 'mb')
    elif len(str_file_size) >= 4:
        print('{0:.2f}'.format(file_size / 1024), 'kb')


def calculate(directory):
    """Split the tuple (obtained from scan) to separate files.
       Alternately send full paths to the files in md5 and call it.
       :param directory: tuple of files in the directory."""

    # Set correct slashes for the OS
    if sys.platform == 'windows':
        slash = '\\'
    elif sys.platform == 'linux':
        slash = '/'
    else:
        print('#Error. Unknown platform.')
        return

    print('Files in the current directory and their md5-hashes:\n')

    for i in range(len(directory[2])):  # Go through the list of files
        full_path = directory[0]+slash+directory[2][i]
        print(full_path)  # Get the list of files with full paths
        size(full_path)
        print(md5(full_path))
        # return md5(full_path)


def scan(tree):
    """Scan the directory and send the obtained tuple to calculate.
       :param tree: path to file or directory"""

    tree = os.path.normpath(tree)
    assert os.path.exists(tree), "#Error. The path '{}' is" \
                                 " invalid or doesn't exist.".format(str(tree))

    if os.path.isfile(tree):
        return md5(tree)
    elif os.path.isdir(tree):
        tree = os.walk(tree)
        for directory in tree:
            print('...................')
            print('Current directory:')
            print(directory[0])  # Current directory
            if not directory[2]:  # Empty directory check
                print('An empty directory.')
                continue
            else:
                print('List of the files in the current directory:')
                print(directory[2])  # Files in the current directory
                print()
            calculate(directory)
