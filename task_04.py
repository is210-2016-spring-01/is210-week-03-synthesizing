#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides variables for formatting."""

NEWS = 'Hi {friend}! I have {0} news! I won the raffle with number {1}!'.format('Pat', '*amazing*', '42')

FNAME = 'Pat'
NTYPE = '*amazing*'
RNUM = 42

{friend} == FNAME
{0} == NTYPE
{1} == RNUM
EMAIL = 'Hi {friend} ! I have NTYPE news! I won the raffle with number {1:6f}!'.format('Pat', '*amazing*', '42')
print EMAIL























