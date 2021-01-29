#!/usr/bin/env python3

from sys import platform
from os import path, walk
import hashlib

BLOCKSIZE = 65536


def md5(file_path):
    """Calculates the md5-hash of the file.
    :param file_path: full path to the file.
    """

    return hashlib.md5(open(file_path,'rb').read()).hexdigest().upper()


def size(full_path):
    """Shows file size.
    :param full_path: full path to the file.
    """

    file_size = path.getsize(full_path)
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
    if platform == 'windows':
        slash = '\\'
    elif platform == 'linux':
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

    tree = path.normpath(tree)
    assert path.exists(tree), "#Error. The path '{}' is" \
                                 " invalid or doesn't exist.".format(str(tree))

    if path.isfile(tree):
        return md5(tree)
    elif path.isdir(tree):
        tree = walk(tree)
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
