#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

STRLEN = len('Spanish')

NETSTR = len(inquisition.SPANISH)

TARGETSTR = inquisition.SPANISH.index('Spanish')

ENDTARGETSTR = TARGETSTR + STRLEN

STR_LT = inquisition.SPANISH[0:TARGETSTR]

STR_RT = inquisition.SPANISH[ENDTARGETSTR:NETSTR]

FLEMISH = STR_LT + 'Flemish' + STR_RT
