#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

LEN_STRING = len('Spanish')

STRING = inquisition.SPANISH.index('Spanish')

STRING_LT = inquisition.SPANISH[0:STRING]

STRING_RT = inquisition.SPANISH[STRING + LEN_STRING:]

FLEMISH = STRING_LT + 'Flemish' + STRING_RT
