#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

ORIG_VAL = 'Spanish'

NEW_VAL = 'Flemish'

STORY = inquisition.SPANISH

ORIG_VAL_LEN = len(ORIG_VAL)

VAL_LOCATOR = inquisition.SPANISH.index(ORIG_VAL)

FLEMISH = STORY[:VAL_LOCATOR] + NEW_VAL + STORY[VAL_LOCATOR + ORIG_VAL_LEN:]

print FLEMISH
