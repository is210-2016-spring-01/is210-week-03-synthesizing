#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides variables for formatting."""

NEWS = 'Hi {friend}! I have {0} news! I won the raffle with number {1:0>6}!'
FNAME = 'Pat'
NTYPE = '*amazing*'
RNUM = 42

print NEWS.format(friend='FNAME', 'NTYPE', 'RNUM')

EMAIL = 'Hi Pat! I have *amazing* news! I won the raffle with number 000042!'

print EMAIL
