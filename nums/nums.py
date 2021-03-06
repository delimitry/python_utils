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
    num = abs(num)
    divisors = [n for n in xrange(1, int(num ** 0.5) + 1) if num % n == 0]
    return divisors + [num // n for n in divisors if n * n != num]


def is_prime(num):
    """
    Check that number is prime
    """
    if num < 2:
        return False
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
    if not a and not b:
        raise Exception('GCD for numbers 0 and 0 is undefined')
    while b:
        a, b = b, a % b
    return a


def is_lucky(num, digits=6):
    """
    Check that number is lucky
    Lucky numbers are the positive integers with a sum of digits in left 
    half is equal to the sum in the right. If length of the number is less 
    than `digits` (by default 6), the number is padded with zeros.
    """
    if digits % 2:
        raise Exception('Please provide the even `digits` value')
    str_num = str(num).zfill(digits)
    if len(str_num) % 2 or num < 0:
        return False
    left = sum([int(d) for d in str_num[:len(str_num) / 2]])
    right = sum([int(d) for d in str_num[len(str_num) / 2:]])
    return left == right
