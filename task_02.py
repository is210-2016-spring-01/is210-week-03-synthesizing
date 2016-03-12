#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

SPANISH = inquisition.SPANISH

LINE_1 = len(SPANISH)

LINE_2 = SPANISH.index('Spanish')

FLEMISH = SPANISH[:19] + 'Flemish' + SPANISH[26:]


print LINE_1
print LINE_2
print FLEMISH
