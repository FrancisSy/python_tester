#!/usr/bin/env python3
from bcolors import bcolors
from testcases import TestCase, TestCases

def add_one(x:int):
    return x+1

def main():
    tc = TestCases()
    tc.add_testcase(add_one, 2, 3)
    tc.add_testcase(add_one, 1, 5)
    tc.evaluate_tests()

if __name__ == '__main__':
    main()
