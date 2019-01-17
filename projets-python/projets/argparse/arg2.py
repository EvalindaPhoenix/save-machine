#!/usr/local/bin/python3
#-*- coding: utf-8 -*-

# Source : https://www.bogotobogo.com/python/python_argparse.php
# arg2.py

import argparse
import sys

def int_args(args=None):
    parser = argparse.ArgumentParser(description='Processing integers.')
    parser.add_argument('integers',
                        metavar='N',
                        type=int,
                        nargs='+',
                        help='integer args')
    return parser.parse_args()

if __name__ == '__main__':
    print(int_args(sys.argv[1:]))
