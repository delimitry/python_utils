#!/usr/bin/env python
#-*- coding: utf8 -*-
"""
Module with functions for working with strings
"""


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
    Remove vowels from text
    """
    result = ''
    for w in text.split():
        translated = w.translate(None, 'aeuio')
        if len(translated) < 1:
            result += w
        else:
            result += translated
        result += ' '
    return result
