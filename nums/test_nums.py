#!/usr/bin/env python
#-*- coding: utf8 -*-

import unittest
from nums import *


class Test(unittest.TestCase):
    """
    Test nums module
    """

    def test_get_divisors(self):
        self.assertEqual(sorted(get_divisors(0)), [])
        self.assertEqual(sorted(get_divisors(1)), [1])
        self.assertEqual(sorted(get_divisors(2)), [1, 2])
        self.assertEqual(sorted(get_divisors(10)), [1, 2, 5, 10])
        self.assertEqual(sorted(get_divisors(5040)), [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 24, 28,
            30, 35, 36, 40, 42, 45, 48, 56, 60, 63, 70, 72, 80, 84, 90, 105,
            112, 120, 126, 140, 144, 168, 180, 210, 240, 252, 280, 315, 336,
            360, 420, 504, 560, 630, 720, 840, 1008, 1260, 1680, 2520, 5040])
        # for negative numbers divisors are the same as for positive
        self.assertEqual(sorted(get_divisors(-10)), [1, 2, 5, 10])

    def test_is_prime(self):
        self.assertEqual(is_prime(0), False)
        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(3), True)
        self.assertEqual(is_prime(4), False)
        self.assertEqual(is_prime(100), False)
        self.assertEqual(is_prime(311), True)

    def test_get_primes_less_than(self):
        self.assertEqual(get_primes_less_than(-1), [])
        self.assertEqual(get_primes_less_than(2), [])
        self.assertEqual(get_primes_less_than(3), [2])
        self.assertEqual(get_primes_less_than(12), [2, 3, 5, 7, 11])

    def test_gcd(self):
        self.assertEqual(gcd(2, 2), 2)
        self.assertEqual(gcd(22, 137), 1)
        self.assertEqual(gcd(0, 137), 137)
        self.assertEqual(gcd(15, 20), 5)
        self.assertEqual(gcd(15, -20), -5)
        with self.assertRaises(Exception):
            # undefined for 0 and 0
            gcd(0, 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
