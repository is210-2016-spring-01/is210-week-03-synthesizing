#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

WORD = 'Spanish'
FRONT = inquisition.SPANISH[0:inquisition.SPANISH.index(WORD)]
BACK = inquisition.SPANISH[inquisition.SPANISH.index(WORD) + len(WORD):]
FLEMISH = FRONT + 'Flemish' + BACK
