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
#  Filename: pipipes.py
#
#  Decription:
#      Numpy pipes
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
    'as_array'
]


@P.Pipe
def as_array(seq):
    from numpy import array
    yield array(next(seq))


@P.Pipe
def loadtxt(obj, *args, **kwargs):
    from numpy import loadtxt
    yield loadtxt(next(obj), *args, **kwargs)


@P.Pipe
def genfromtxt(obj, *args, **kwargs):
    from numpy import genfromtxt
    yield genfromtxt(next(obj), *args, **kwargs)


@P.Pipe
def itake(seq, *args, **kwargs):
    from numpy import take
    for item in seq:
        yield take(item, *args, **kwargs)
    return


@P.Pipe
def iexpand_dims(seq, *args, **kwargs):
    from numpy import expand_dims
    for item in seq:
        yield expand_dims(item, *args, **kwargs)
    return


if __name__ == "__main__":
    pass
