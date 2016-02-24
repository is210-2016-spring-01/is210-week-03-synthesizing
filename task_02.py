#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

SPANISH = inquisition.SPANISH

FLEMISH = SPANISH.replace('Spanish', 'Flemish', 1)

print FLEMISH
