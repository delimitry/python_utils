#!/usr/bin/env python
#-*- coding: utf8 -*-

import unittest
from strs import (
    disemvowel, xor_strings, rotx, leet, bits_to_str, to_phonetic, num_to_human,
    capitalize_text, reverse_words
)


class Test(unittest.TestCase):
    """
    Test strs module 
    """

    def test_xor_strings(self):
        self.assertEqual(xor_strings('', ''), '')
        self.assertEqual(xor_strings('123', '123'), '\x00\x00\x00')
        self.assertEqual(xor_strings('test', '    '), 'TEST')
        self.assertEqual(xor_strings('\x00', '\x01'), '\x01')
        with self.assertRaises(Exception):
            xor_strings('123', '1')

    def test_disemvowel(self):
        self.assertEqual(disemvowel(''), '')
        self.assertEqual(disemvowel('AEUIOaeuio'), 'AEUIOaeuio')
        self.assertEqual(disemvowel('lynx'), 'lynx')
        self.assertEqual(disemvowel('some test'), 'sm tst')
        self.assertEqual(disemvowel('You can understand'), 'Y cn ndrstnd')
        self.assertEqual(disemvowel(
            'Some long (or not) text with punctuation!'),
            'Sm lng (r nt) txt wth pncttn!')

    def test_rotx(self):
        self.assertEqual(rotx('', 0), '')
        self.assertEqual(rotx('abc', 1), 'bcd')
        self.assertEqual(rotx('ABC', 1), 'BCD')
        self.assertEqual(rotx('abc', 26), 'abc')
        self.assertEqual(rotx('ABC', 26), 'ABC')
        self.assertEqual(rotx('A B C', -1), 'Z A B')
        self.assertEqual(rotx('The popular cipher', 13), 'Gur cbchyne pvcure')
        self.assertEqual(rotx('Gur cbchyne pvcure', 13), 'The popular cipher')

    def test_leet(self):
        self.assertEqual(leet(''), '')
        self.assertEqual(leet('this is a leet test'), '7hi5 i5 4 1337 7357')
        self.assertEqual(leet('buy my drum'), 'buy my drum')

    def test_bits_to_str(self):
        self.assertEqual(bits_to_str(''), '')
        self.assertEqual(bits_to_str('0'), '\x00')
        self.assertEqual(bits_to_str('1'), '\x01')
        self.assertEqual(bits_to_str('00000000'), '\x00')
        self.assertEqual(bits_to_str('11111111'), '\xff')
        self.assertEqual(bits_to_str('001111110'), '?\x00')
        self.assertEqual(bits_to_str(bin(ord('~'))[2:]), '~')
        self.assertEqual(bits_to_str(
            '011000010110001001100011001100010011001000110011'), 'abc123')

    def test_to_phonetic(self):
        self.assertEqual(to_phonetic(''), '')
        self.assertEqual(to_phonetic('a'), 'Alpha')
        self.assertEqual(to_phonetic('0'), 'Zero')
        self.assertEqual(to_phonetic('test'), 'Tango Echo Sierra Tango')
        self.assertEqual(to_phonetic('ABC'), 'Alpha Bravo Charlie')
        self.assertEqual(to_phonetic('123'), 'One Two Three')

    def test_num_to_human(self):
        self.assertEqual(num_to_human(0), 'Zero')
        self.assertEqual(num_to_human(-0), 'Zero')
        self.assertEqual(num_to_human(1), 'One')
        self.assertEqual(num_to_human(123), 'One Hundred Twenty Three')
        self.assertEqual(num_to_human(-123), 'Minus One Hundred Twenty Three')
        self.assertEqual(num_to_human(1000), 'One Thousand')
        self.assertEqual(num_to_human(1000000), 'One Million')
        self.assertEqual(num_to_human(3 * 10 ** 63), 'Three Vigintillion')
        self.assertEqual(
            num_to_human(123456789012345678901234567890),
            'One Hundred Twenty Three Octillion Four Hundred Fifty Six '
            'Septillion Seven Hundred Eighty Nine Sextillion Twelve '
            'Quintillion Three Hundred Forty Five Quadrillion Six Hundred '
            'Seventy Eight Trillion Nine Hundred One Billion Two Hundred '
            'Thirty Four Million Five Hundred Sixty Seven Thousand Eight '
            'Hundred Ninety'
        )

    def test_capitalize_text(self):
        self.assertEqual(capitalize_text(''), '')
        self.assertEqual(capitalize_text('abc'), 'Abc')
        self.assertEqual(capitalize_text('some text'), 'Some Text')
        self.assertEqual(capitalize_text(
            'Some long (or not) text/message - with punctuation!'),
            'Some Long (Or Not) Text/Message - With Punctuation!')

    def test_reverse_words(self):
        self.assertEqual(reverse_words(''), '')
        self.assertEqual(reverse_words('rotator'), 'rotator')
        self.assertEqual(reverse_words('some text'), 'emos txet')
        self.assertEqual(reverse_words(
            'some text with numbers 123, and/or punctuation'),
            'emos txet htiw srebmun 321, dna/ro noitautcnup')

if __name__ == '__main__':
    unittest.main(verbosity=2)
