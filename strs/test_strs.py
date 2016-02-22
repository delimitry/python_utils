#!/usr/bin/env python
#-*- coding: utf8 -*-

import unittest
from strs import disemvowel_text, xor_strings


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

    def test_disemvowel_text(self):
        self.assertEqual(disemvowel_text(''), '')
        self.assertEqual(disemvowel_text('AEUIOaeuio'), 'AEUIOaeuio')
        self.assertEqual(disemvowel_text('lynx'), 'lynx')
        self.assertEqual(disemvowel_text('some test'), 'sm tst')
        self.assertEqual(disemvowel_text('You can understand'), 'Y cn ndrstnd')
        self.assertEqual(disemvowel_text(
            'Some long (or not) text with punctuation!'),
            'Sm lng (r nt) txt wth pncttn!')


if __name__ == '__main__':
    unittest.main(verbosity=2)
