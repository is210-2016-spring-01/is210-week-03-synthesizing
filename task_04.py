#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides variables for formatting."""

NEWS = 'Hi {FNAME}! I have {NTYPE} news! I won the raffle with number {RNUM}!'
FNAME = 'Pat'
NTYPE = '*amazing*'
RNUM = 42

EMAIL = NEWS.format('Pat', '*amazing*', '42')
