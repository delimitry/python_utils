#!/usr/bin/env python
#-*- coding: utf-8 -*-

import unittest
from strs import (
    disemvowel, xor_strings, rotx, leet, bits_to_str, to_phonetic, num_to_human,
    capitalize_text, reverse_words, to_roman, from_roman, check_anagrams,
    to_base85, from_base85, ipv6_to_full, ipv6_rfc1924_encode, 
    ipv6_rfc1924_decode, to_tonal, from_tonal,
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

    def test_to_roman(self):
        with self.assertRaises(Exception):
            to_roman(0)
        with self.assertRaises(Exception):
            to_roman(4000)
        self.assertEqual(to_roman(1), 'I')
        self.assertEqual(to_roman(4), 'IV')
        self.assertEqual(to_roman(5), 'V')
        self.assertEqual(to_roman(8), 'VIII')
        self.assertEqual(to_roman(9), 'IX')
        self.assertEqual(to_roman(14), 'XIV')
        self.assertEqual(to_roman(19), 'XIX')
        self.assertEqual(to_roman(44), 'XLIV')
        self.assertEqual(to_roman(49), 'XLIX')
        self.assertEqual(to_roman(87), 'LXXXVII')
        self.assertEqual(to_roman(90), 'XC')
        self.assertEqual(to_roman(99), 'XCIX')
        self.assertEqual(to_roman(1838), 'MDCCCXXXVIII')
        self.assertEqual(to_roman(1954), 'MCMLIV')
        self.assertEqual(to_roman(1984), 'MCMLXXXIV')
        self.assertEqual(to_roman(3999), 'MMMCMXCIX')

    def test_from_roman(self):
        with self.assertRaises(Exception):
            from_roman('')
        with self.assertRaises(Exception):
            from_roman('ABC')
        self.assertEqual(from_roman('I'), 1)
        self.assertEqual(from_roman('IV'), 4)
        self.assertEqual(from_roman('V'), 5)
        self.assertEqual(from_roman('VIII'), 8)
        self.assertEqual(from_roman('IX'), 9)
        self.assertEqual(from_roman('XIV'), 14)
        self.assertEqual(from_roman('XIX'), 19)
        self.assertEqual(from_roman('XLIV'), 44)
        self.assertEqual(from_roman('XLIX'), 49)
        self.assertEqual(from_roman('LXXXVII'), 87)
        self.assertEqual(from_roman('XC'), 90)
        self.assertEqual(from_roman('XCIX'), 99)
        self.assertEqual(from_roman('MDCCCXXXVIII'), 1838)
        self.assertEqual(from_roman('MCMLIV'), 1954)
        self.assertEqual(from_roman('MCMLXXXIV'), 1984)
        self.assertEqual(from_roman('MMMCMXCIX'), 3999)

    def test_check_anagrams(self):
        self.assertEqual(check_anagrams('', ''), True)
        self.assertEqual(check_anagrams('a', 'a'), True)
        self.assertEqual(check_anagrams('a', 'b'), False)
        self.assertEqual(check_anagrams('123', '321'), True)
        self.assertEqual(check_anagrams('The eyes', 'They see'), True)

    def test_ipv6_to_full(self):
        val = 'ff01:0da8:0000:0000:0001:0000:0000:0001'
        ipv6_values = [
            'ff01:0da8:0:0:1:0:0:1', 
            'ff01:0da8::1:0:0:1', 
            'ff01:da8:0000:0:1::1', 
            'ff01:da8:0:0:1:0:0:1', 
            'ff01:da8:0:0:1::1', 
            'ff01:DA8:0:0:1::1', 
            'ff01:da8::0:1:0:0:1', 
            'ff01:da8::1:0:0:1', 
        ]
        self.assertTrue(all(ipv6_to_full(x) == val for x in ipv6_values))
        self.assertEqual(ipv6_to_full('ffff::ffff'), 
            'ffff:0000:0000:0000:0000:0000:0000:ffff')
        self.assertEqual(ipv6_to_full('::'), ipv6_to_full('0:0:0:0:0:0:0:0'))
        self.assertEqual(ipv6_to_full('::1'), ipv6_to_full('0:0:0:0:0:0:0:1'))

    def test_ipv6_rfc1924_encode(self):
        self.assertEqual(ipv6_rfc1924_encode(
            '1080:0:0:0:8:800:200c:417a'), '4)+k&C#VzJ4br>0wv%Yp')
        self.assertEqual(ipv6_rfc1924_encode(
            '1:2:3:4:5:6:7:8'), '8JQWOV7SkcR4tS1R_a')

    def test_ipv6_rfc1924_decode(self):
        self.assertEqual(ipv6_rfc1924_decode(
            '4)+k&C#VzJ4br>0wv%Yp'), '1080:0:0:0:8:800:200c:417a')
        val = 'ffff:2:3:4:5:6:7:ffff'
        self.assertEqual(ipv6_rfc1924_decode(ipv6_rfc1924_encode(val)), val)

    def test_to_base85(self):
        self.assertEqual(
            to_base85('Hello world', adobe=True), '<~87cURD]j7BEbo7~>')
        self.assertEqual(
            to_base85('abcd\x00\x00\x00\x00123', adobe=True), '<~@:E_Wz0etN~>')
        self.assertEqual(
            to_base85('\xff\xff\xff\xff'), 's8W-!')

    def test_from_base85(self):
        self.assertEqual(from_base85(to_base85('Abc 123!@#$')), 'Abc 123!@#$')
        self.assertEqual(from_base85(to_base85('AB')), 'AB')
        self.assertEqual(from_base85(to_base85('AB\xff')), 'AB\xff')
        self.assertEqual(
            from_base85('<~87cURD]j7BEbo7~>', adobe=True), 'Hello world')
        self.assertEqual(
            from_base85('<~z~>', adobe=True), '\x00\x00\x00\x00')
        self.assertEqual(
            from_base85('!!!!!'), '\x00\x00\x00\x00')

    def test_to_tonal(self):
        self.assertEqual(to_tonal(0x16), 'tonby')
        self.assertEqual(to_tonal(0x12a), 'sandetonko')
        self.assertEqual(to_tonal(0x700), 'rasan')
        self.assertEqual(to_tonal(0x1000), 'mill')
        self.assertEqual(to_tonal(0x10000), 'bong')
        self.assertEqual(to_tonal(0x100000000), 'tam')
        self.assertEqual(to_tonal(0x1000000000000), 'song')
        self.assertEqual(to_tonal(0x15100000), 'millsusantonbong')
        self.assertEqual(to_tonal(0x28d5b7e0f), 'detammemilllasansutonhubongramillposanfy')
        self.assertEqual(to_tonal(0x100000000000000000000), 'bongtran')

    def test_from_tonal(self):
        self.assertEqual(from_tonal('tonby'), 0x16)
        self.assertEqual(from_tonal('sandetonko'), 0x12a)
        self.assertEqual(from_tonal('rasan'), 0x700)
        self.assertEqual(from_tonal('mill'), 0x1000)
        self.assertEqual(from_tonal('bong'), 0x10000)
        self.assertEqual(from_tonal('tam'), 0x100000000)
        self.assertEqual(from_tonal('song'), 0x1000000000000)
        self.assertEqual(from_tonal('millsusantonbong'), 0x15100000)
        self.assertEqual(from_tonal('detammemilllasansutonhubongramillposanfy'), 0x28d5b7e0f)
        self.assertEqual(from_tonal('bongtran'), 0x100000000000000000000)


if __name__ == '__main__':
    unittest.main(verbosity=2)
