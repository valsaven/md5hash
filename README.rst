Description
===========
Fast and simple md5 hash generator for files and directories.

Installing
----------
Requires Python 3.

From PyPI:
::

    pip install md5hash

Examples
--------
For a single file:
::

    from md5hash import scan
    print(scan('file.txt'))
    >>> 195FCD0B460051BF195DFCB338B196A7
