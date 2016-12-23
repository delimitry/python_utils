#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Module with functions for working with strings
"""

import re
import struct


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
    splitted = re.split(r'(\W+)', text)
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


def capitalize_text(text):
    """
    Capitalize text
    """
    pattern = re.compile(r'\w+')
    return pattern.sub(lambda x: x.group().capitalize(), text)


def reverse_words(text):
    """
    Reverse words in text
    """
    pattern = re.compile(r'\w+')
    return pattern.sub(lambda x: x.group()[::-1], text)


def to_roman(num):
    """
    Convert number to Roman numerals
    """
    if not 0 < num < 4000:
        raise Exception('Please use numbers from 1 to 3999')
    nums_to_roman_nums = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M',
    }
    out = ''
    for k in sorted(nums_to_roman_nums.keys(), reverse=True):
        quotient, remainder = divmod(num, k)
        num = remainder
        if quotient:
            out += nums_to_roman_nums.get(k) * quotient
    return out


def from_roman(s):
    """
    Convert from Roman numerals to number
    """
    if not s or not s.strip() or s.strip('MDCLXVI'):
        raise Exception('Please provide valid Roman number')
    roman_nums_to_nums = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000,
    }
    roman_numerals = [
        'CM', 'CD', 'XC', 'XL', 'IX', 'IV',
        'M', 'D', 'C', 'L', 'X', 'V', 'I'
    ]
    num = 0
    while s:
        for r in roman_numerals:
            if s.startswith(r):
                num += roman_nums_to_nums.get(r)
                s = s[len(r):]
                break
    return num


def check_anagrams(a, b):
    """
    Check that `a` and `b` are anagrams
    """
    if a and b and len(a) != len(b):
        return False
    return sorted(a.lower()) == sorted(b.lower())


def to_base85(s, adobe=False):
    """
    Encode data to Base85 (ASCII85)
    Adobe version is supported
    """
    # padding input string with zero bytes
    pad_size = (4 - len(s)) % 4
    s += pad_size * '\x00'
    # get groups by 4 bytes and save as 32-bit numbers
    numbers = [struct.unpack('>I', s[i:i + 4])[0] for i in xrange(0, len(s), 4)]
    encoded = []
    for num in numbers:
        # convert num into 5 radix-85 digits
        enc_part = []
        for _ in xrange(5):
            num, remainder = divmod(num, 85)
            enc_part.insert(0, remainder)
        if adobe and not any(enc_part):
            encoded += [ord('z') - 33]
        else:
            encoded += enc_part
    encoded = encoded[:-pad_size] if pad_size else encoded
    result = ''.join(chr(x + 33) for x in encoded)
    if adobe:
        result = '<~' + result + '~>'
    return result


def from_base85(s, adobe=False):
    """
    Decode data from Base85 (ASCII85)
    Adobe version is supported
    """
    # cut Adobe delimiters
    if adobe and s.startswith('<~') and s.endswith('~>'):
        s = s[2:-2]
    s = filter(lambda c: 33 <= ord(c) <= 117 or (c == 'z' and adobe), s)
    if adobe:
        s = s.replace('z', '!!!!!')
    # padding input string with 'u' bytes
    pad_size = (5 - len(s)) % 5
    s += pad_size * 'u'
    # get groups by 5 bytes
    values = [[ord(x) - 33 for x in s[i:i + 5]] for i in xrange(0, len(s), 5)]
    decoded = []
    for value in values:
        num = 0
        for i, v in enumerate(value):
            num += (85 ** (4 - i)) * v
        # convert to 32-bit number to 4 decimal bytes
        dec_part = []
        for _ in xrange(4):
            num, remainder = divmod(num, 256)
            dec_part.insert(0, remainder)
        decoded += dec_part
    decoded = decoded[:-pad_size] if pad_size else decoded
    return ''.join(chr(x) for x in decoded)


def ipv6_to_full(s):
    """Expand IPv6 from shortened to full"""
    if '::' in s:
        parts = [x or '0' for x in s.split('::')]
        if len(parts) != 2: 
            raise Exception('Invalid IPv6 format!')
        filler = ':' + ':'.join(['0' for _ in range(8 - s.count(':'))]) + ':'
        s = filler.join(parts)
    return ':'.join('%04x' % int(x, 16) for x in s.split(':'))


RFC1924_ALPHABET = (
    '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    '!#$%&()*+-;<=>?@^_`{|}~'
)


def ipv6_rfc1924_encode(s):
    """Encode IPv6 address to RFC1924"""
    s = filter(lambda c: c in ':0123456789ABCDEFabcdef', s)
    num = int(''.join([x.zfill(4) for x in s.split(':')]), 16)
    enc = []
    if not num:
        enc = [0, 0, 0, 0, 0, 0, 0, 0]
    while num:
        num, remainder = divmod(num, 85)
        enc.insert(0, remainder)
    return ''.join(RFC1924_ALPHABET[i] for i in enc)


def ipv6_rfc1924_decode(s):
    """Decode RFC1924 IPv6 address to standard hex representation"""
    # filter unexpected characters
    s = filter(lambda c: c in RFC1924_ALPHABET, s)
    indices = [RFC1924_ALPHABET.index(c) for c in s]
    num = 0
    for i, v in enumerate(indices):
        num += (85 ** (len(indices) - 1 - i)) * v
    # convert to hex
    hex_values = []
    if not num:
        hex_values = [0, 0, 0, 0, 0, 0, 0, 0]
    while num:
        num, remainder = divmod(num, 0x10000)
        hex_values.insert(0, remainder)
    return ':'.join('%x' % v for v in hex_values)
