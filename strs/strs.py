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


def disemvowel(text):
    """
    Remove vowels from words only if at least one consonant in the word
    """
    splitted = re.split('(\W+)', text)
    return ''.join([w.translate(None, 'AEUIOaeuio') or w for w in splitted])


def leet(text):
    """
    Make leet text from text
    """
    d = dict(zip('lzeastgoLZEASGTBO', '12345790123456780'))
    return ''.join(d.get(c, c) for c in text)


def rotx(s, x):
    """
    Rotate string by x (from -26 to 26)
    """
    a = 'abcdefghijklmnopqrstuvwxyz'
    x = x % 26
    b = a[x:] + a[:x]
    d = dict(zip(a + a.upper(), b + b.upper()))
    return ''.join(d.get(c, c) for c in s)
