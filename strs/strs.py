#!/usr/bin/env python
#-*- coding: utf8 -*-
"""
Module with functions for working with strings
"""

import re


def xor_strings(a, b):
    """
    Get the result from XORing two strings
    """
    if len(a) != len(b):
        raise Exception('The lengths of the strings must be the same!')
    res = ''.join([chr(ord(a[i]) ^ ord(b[i])) for i in xrange(len(a))])
    return res


def disemvowel_text(text):
    """
    Remove vowels from words only if at least one consonant in the word
    """
    splitted = re.split('(\W+)', text)
    return ''.join([w.translate(None, 'AEUIOaeuio') or w for w in splitted])
