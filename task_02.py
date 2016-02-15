#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition
SPANISH = inquisition.SPANISH
print SPANISH
print SPANISH.index('Spanish')
print SPANISH[1:19]
FLEMISH = SPANISH[:19] + 'Flemish' + SPANISH[26:]
print FLEMISH
