#!/usr/local/bin/python3
#-*- coding: utf-8 -*-

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("key")
args = parser.parse_args()
print(args.echo)
