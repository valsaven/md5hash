Description
===========
[![Build Status](https://drone.io/github.com/valsaven/md5hash/status.png)](https://drone.io/github.com/valsaven/md5hash/latest)
[![Code Issues](https://www.quantifiedcode.com/api/v1/project/d19ef1a9507044aea01468e398cb9d64/badge.svg)](https://www.quantifiedcode.com/app/project/d19ef1a9507044aea01468e398cb9d64)
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
