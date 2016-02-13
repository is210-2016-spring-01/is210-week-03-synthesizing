#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

A = inquisition.SPANISH

B = A.index('Spanish')

C = len('Spanish')

FLEMISH = A[:B] + 'Flemish' + A[B+C:]
