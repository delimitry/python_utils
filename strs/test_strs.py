#!/usr/bin/env python
#-*- coding: utf8 -*-

import unittest
from strs import disemvowel, xor_strings, rotx, leet, bits_to_str


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


if __name__ == '__main__':
    unittest.main(verbosity=2)
