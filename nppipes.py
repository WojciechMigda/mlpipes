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
#  Filename: nppipes.py
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
    'as_array', 'loadtxt', 'genfromtxt', 'take', 'expand_dims',
    'strip', 'place', 'putmask', 'astype', 'as_columns', 'label_encoder',
    'fit_transform', 'transform', 'dstack',
]


@P.Pipe
def as_array(iterable):
    from numpy import array
    for item in iterable:
        yield array(item)


@P.Pipe
def loadtxt(iterable, *args, **kwargs):
    from numpy import loadtxt
    for item in iterable:
        yield loadtxt(item, *args, **kwargs)


@P.Pipe
def genfromtxt(iterable, *args, **kwargs):
    from numpy import genfromtxt
    for item in iterable:
        yield genfromtxt(item, *args, **kwargs)


@P.Pipe
def take(seq, *args, **kwargs):
    from numpy import take
    for item in seq:
        yield take(item, *args, **kwargs)
    return


@P.Pipe
def expand_dims(seq, *args, **kwargs):
    from numpy import expand_dims
    for item in seq:
        yield expand_dims(item, *args, **kwargs)
    return

@P.Pipe
def strip(iterable, *args, **kwargs):
    from numpy.core.defchararray import strip
    for item in iterable:
        yield strip(item, *args, **kwargs)


@P.Pipe
def place(iterable, pred, vals):
    from numpy import place
    for item in iterable:
        place(item, pred(item), vals)
        yield item


@P.Pipe
def putmask(iterable, *args, **kwargs):
    from numpy import putmask
    for item in iterable:
        putmask(item, *args, **kwargs)
        yield item


@P.Pipe
def astype(iterable, tp):
    for item in iterable:
        yield item.astype(tp)


@P.Pipe
def as_columns(iterable):
    for item in iterable:
        for i in range(item.shape[1]):
            yield item[:, i]


@P.Pipe
def label_encoder(n=1):
    from sklearn.preprocessing import LabelEncoder
    for item in range(n):
        yield LabelEncoder()


@P.Pipe
def standard_scaler(n=1, **kwargs):
    from sklearn.preprocessing import StandardScaler
    for item in range(n):
        yield StandardScaler(**kwargs)

@P.Pipe
def fit_transform(iterable, models):
    from itertools import izip
    for X, clf in izip(iterable, models):
        yield clf.fit_transform(X)


@P.Pipe
def transform(iterable, models):
    from itertools import izip
    for X, clf in izip(iterable, models):
        yield clf.transform(X)


@P.Pipe
def dstack(iterable):
    from numpy import dstack
    yield dstack(tuple(iterable))


if __name__ == "__main__":
    pass
