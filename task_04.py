#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides variables for formatting."""

NEWS = "Hi {}! I have {} news! I won the raffle with number {:0>6}!"

FNAME = 'Pat'
NTYPE = '*amazing*'
RNUM = 42

EMAIL = NEWS.format(FNAME, NTYPE, RNUM)

print EMAIL
