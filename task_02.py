#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

SPAM = inquisition.SPANISH

VIKINGS = 'Spanish'

ITS = SPAM.index(VIKINGS)

FLEMISH = SPAM[0:ITS] + 'Flemish' + SPAM[ITS + len(VIKINGS):]
