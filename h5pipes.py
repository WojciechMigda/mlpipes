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
#  Filename: h5pipes.py
#
#  Decription:
#      HDF5 pipes
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
#  2016-01-08   wm              Initial version
#
################################################################################
"""

from __future__ import print_function

import pipe as P

__author__ = 'Wojciech Migda'
__date__ = '2016-01-08'
__version__ = '0.0.1'
__all__ = [
    'h5new'
]


@P.Pipe
def h5new(iterable):
    from h5py import File
    for fname in iterable:
        with File(fname, 'w') as f:
            yield f


@P.Pipe
def h5open(iterable):
    from h5py import File
    for fname in iterable:
        with File(fname, 'r') as f:
            yield f

if __name__ == "__main__":
    pass
