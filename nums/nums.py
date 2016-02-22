#!/usr/bin/env python
#-*- coding: utf8 -*-
"""
Module with functions for working with numbers
"""


def get_divisors_slow(num):
    """
    Get all the divisors of a number (slow version)
    """
    divisors = []
    for i in xrange(1, int(num * 0.5) + 1):
        if num % i == 0:
            divisors.append(i)
    if num:
        divisors.append(num)
    return divisors


def get_divisors(num):
    """
    Get all the divisors of a number
    """
    divisors = [n for n in xrange(1, int(num ** 0.5) + 1) if num % n == 0]
    return divisors + [num // n for n in divisors if n * n != num]


def is_prime(num):
    """
    Check that number is prime
    """
    for i in xrange(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_primes_less_than(num):
    """
    Get all prime numbers less than number `num`
    """
    return [n for n in xrange(2, num) if is_prime(n)]


def gcd(a, b):
    """
    Get greatest common divisor using Euclid's algorithm
    """
    while b:
        a, b = b, a % b
    return a
