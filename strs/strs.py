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


def num_to_human(num):
    """
    Convert number to human readable
    """
    big_nums = {
        2: 'Hundred',
        3: 'Thousand',
        6: 'Million',
        9: 'Billion',
        12: 'Trillion',
        15: 'Quadrillion',
        18: 'Quintillion',
        21: 'Sextillion',
        24: 'Septillion',
        27: 'Octillion',
        30: 'Nonillion',
        33: 'Decillion',
        36: 'Undecillion',
        39: 'Duodecillion',
        42: 'Tredecillion',
        45: 'Quattuordecillion',
        48: 'Quindecillion',
        51: 'Sexdecillion',
        54: 'Septendecillion',
        57: 'Octodecillion',
        60: 'Novemdecillion',
        63: 'Vigintillion',
        66: 'Unvigintillion',
        69: 'Duovigintillion',
        72: 'Tresvigintillion',
        75: 'Quattuorvigintillion',
        78: 'Quinquavigintillion',
        81: 'Sesvigintillion',
        84: 'Septemvigintillion',
        87: 'Octovigintillion',
        90: 'Novemvigintillion',
        93: 'Trigintillion',
        96: 'Untrigintillion',
        99: 'Duotrigintillion',
        102: 'Trestrigintillion',
        105: 'Quattuortrigintillion',
        108: 'Quinquatrigintillion',
        111: 'Sestrigintillion',
        114: 'Septentrigintillion',
        117: 'Octotrigintillion',
        120: 'Noventrigintillion',
        123: 'Quadragintillion',
        153: 'Quinquagintillion',
        183: 'Sexagintillion',
        213: 'Septuagintillion',
        243: 'Octogintillion',
        273: 'Nonagintillion',
        303: 'Centillion',
        306: 'Uncentillion',
        309: 'Duocentillion',
        312: 'Trescentillion',
        333: 'Decicentillion',
        336: 'Undecicentillion',
        363: 'Viginticentillion',
        366: 'Unviginticentillion',
        393: 'Trigintacentillion',
        423: 'Quadragintacentillion',
        453: 'Quinquagintacentillion',
        483: 'Sexagintacentillion',
        513: 'Septuagintacentillion',
        543: 'Octogintacentillion',
        573: 'Nonagintacentillion',
        603: 'Ducentillion',
        903: 'Trecentillion',
        1203: 'Quadringentillion',
        1503: 'Quingentillion',
        1803: 'Sescentillion',
        2103: 'Septingentillion',
        2403: 'Octingentillion',
        2703: 'Nongentillion',
        3003: 'Millinillion',
    }

    small_nums = {
        0: 'Zero',
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        10: 'Ten',
        11: 'Eleven',
        12: 'Twelve',
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen',
        16: 'Sixteen',
        17: 'Seventeen',
        18: 'Eighteen',
        19: 'Nineteen',
        20: 'Twenty',
        30: 'Thirty',
        40: 'Forty',
        50: 'Fifty',
        60: 'Sixty',
        70: 'Seventy',
        80: 'Eighty',
        90: 'Ninety',
    }

    def get_zeros(num):
        """
        Get zeros in number using big nums dictionary
        """
        for zeros in sorted(big_nums, reverse=True):
            if len(str(num)) > zeros:
                return zeros
        return 0

    def small_to_human(num):
        """
        Convert small number to human readable
        """
        out = []
        if not num:
            return small_nums.get(num)
        while num:
            if num > 99:
                # get hundreds quotient and continue with remainder as num
                quotient, remainder = divmod(num, 100)
                out.extend([small_nums.get(quotient), big_nums.get(2)])
                num = remainder
            elif num > 19:
                # all two-digit numbers > 19 - are tens and ones combination
                # so get tens quotient and continue with remainder as num
                quotient, remainder = divmod(num, 10)
                out.append(small_nums.get(quotient * 10))
                num = remainder
            else:
                out.append(small_nums.get(num))
                break
        return ' '.join(out)

    def big_to_human(num):
        """
        Convert big number to human readable
        """
        out = []
        if not num:
            out.append(small_to_human(num))
        while num:
            zeros = get_zeros(num)
            quotient, remainder = divmod(num, 10 ** zeros)
            num = remainder
            if quotient < 1000:
                out.append(small_to_human(quotient))
            else:
                out.append(big_to_human(quotient))
            big_num_name = big_nums.get(zeros, '')
            if big_num_name:
                out.append(big_num_name)
        return ' '.join(out)

    sign = '' if num >= 0 else 'Minus '
    return sign + big_to_human(abs(num))


# print num_to_human(123456789012345678901234567890)
# print 'One Hundred Twenty Three Octillion Four Hundred Fifty Six Septillion Seven Hundred Eighty Nine Sextillion Twelve Quintillion Three Hundred Forty Five Quadrillion Six Hundred Seventy Eight Trillion Nine Hundred One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety'

