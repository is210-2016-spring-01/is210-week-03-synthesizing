#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

VALUE = 'Spanish'

VALUE_LEN = len(VALUE)

IMPORT = inquisition.SPANISH

POSITION = IMPORT.index(VALUE)

FLEMISH = IMPORT[:POSITION] + 'Flemish' + IMPORT[POSITION + VALUE_LEN:]
