#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

VAR0 = inquisition.SPANISH

VAR1 = 'Spanish'

VAR2 = len(VAR1)

VAR3 = VAR0.index(VAR1)

FLEMISH = VAR0[:VAR3] + 'Flemish' + VAR0[VAR3+VAR2:]


print FLEMISH
