#!/usr/bin/python3
import argparse
parser = argparse.ArgumentParser(description="This is test tool")
parser.add_argument("-d",type=str, help="Type domain", required=True)

parser.add_argument("-c",type=str, help="Type domain", required=True)
a=parser.parse_args()
print(a)
print(a.d)
print(a.c)


