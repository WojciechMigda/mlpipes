#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
################################################################################
#
#  Copyright (c) 2016 Wojciech Migda
#  All rights reserved
#  Distributed under the terms of the MIT license
#
################################################################################
#
#  Filename: pypipes.py
#
#  Decription:
#      General python pipes
#
#  Authors:
#       Wojciech Migda
#
################################################################################
#
#  History:
#  --------
#  Date         Who  Ticket     Description
#  ----------   ---  ---------  ------------------------------------------------
#  2016-01-02   wm              Initial version
#
################################################################################
"""

from __future__ import print_function

import pipe as P

__author__ = 'Wojciech Migda'
__date__ = '2016-01-02'
__version__ = '0.0.1'
__all__ = [
    'unzip', 'as_csv_rows', 'iformat', 'loopcount', 'timestamp', 'iattach',
    'as_key', 'getitem', 'setitem', 'del_key', 'as_set'
]


def fopen_(obj):
    from types import GeneratorType
    if type(obj) is str:
        with open(obj, 'r') as f:
            yield f
    elif type(obj) is GeneratorType:
        yield next(obj)
    else:
        yield obj


@P.Pipe
def unzip(obj, ifile):
    import zipfile
    with zipfile.ZipFile(obj, 'r') as z:
        with z.open(ifile) as f:
            yield f


@P.Pipe
def as_csv_rows(obj, **kwargs):
    from csv import reader
    for row in reader(next(fopen_(obj)), **kwargs):
        yield row


@P.Pipe
def iformat(seq, fmt):
    for item in seq:
        yield fmt.format(item)


@P.Pipe
def loopcount(seq):
    for i, item in enumerate(seq):
        print(i)
        yield item


@P.Pipe
def timestamp(seq):
    from datetime import datetime
    for item in seq:
        print(datetime.now().strftime("%H:%M:%S.%f"))
        yield item


@P.Pipe
def iattach(seq, key, func, *args, **kwargs):
    for item in seq:
        item[key] = func(item, *args, **kwargs)
        yield item


@P.Pipe
def as_key(iterable, key, func=None, *args, **kwargs):
    #if type(func) is P.Pipe:
    #    for d in iterable:
    #        d[key] = d | func(*args, **kwargs)
    #        yield d
    #elif func:
    if func:
        for d in iterable:
            d[key] = func(d, *args, **kwargs)
            yield d
    else:
        for value in iterable:
            yield {key: value}


@P.Pipe
def getitem(iterable, key):
    for d in iterable:
        yield d[key]


@P.Pipe
def setitem(iterable, out, key):
    for d in iterable:
        out[key] = d
        yield out


@P.Pipe
def del_key(iterable, key):
    for d in iterable:
        del d[key]
        yield d


@P.Pipe
def debug_iterable(iterable):
    print("DEBUG iterable:", type(iterable))
    for item in iterable:
        yield item


@P.Pipe
def debug_item(iterable):
    for item in iterable:
        print("DEBUG item:", type(item))
        yield item


@P.Pipe
def as_set(iterable):
    return set(iterable)


if __name__ == "__main__":
    pass
