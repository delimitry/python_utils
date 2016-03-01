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


def bits_to_str(bits):
    """
    Convert a string of bits to string
    """
    return ''.join(chr(int(bits[i:i + 8], 2)) for i in xrange(0, len(bits), 8))


def to_phonetic(text):
    """
    Convert a text to phonetic alphabet text
    """
    alp = {
        # letters
        'A': 'Alpha',
        'B': 'Bravo',
        'C': 'Charlie',
        'D': 'Delta',
        'E': 'Echo',
        'F': 'Foxtrot',
        'G': 'Golf',
        'H': 'Hotel',
        'I': 'India',
        'J': 'Juliet',
        'K': 'Kilo',
        'L': 'Lima',
        'M': 'Mike',
        'N': 'November',
        'O': 'Oscar',
        'P': 'Papa',
        'Q': 'Quebec',
        'R': 'Romeo',
        'S': 'Sierra',
        'T': 'Tango',
        'U': 'Uniform',
        'V': 'Victor',
        'W': 'Whiskey',
        'X': 'X-ray',
        'Y': 'Yankee',
        'Z': 'Zulu',
        # digits
        '0': 'Zero',
        '1': 'One',
        '2': 'Two',
        '3': 'Three',
        '4': 'Four',
        '5': 'Five',
        '6': 'Six',
        '7': 'Seven',
        '8': 'Eight',
        '9': 'Nine',
    }
    return ' '.join([alp.get(x, x) for x in ''.join(text.split()).upper()])
