#!/usr/bin/python3
import argparse, os
parser = argparse.ArgumentParser(description="This is test tool")
parser.add_argument("-d",type=str, help="Type domain", required=True)

a=parser.parse_args()
os.system("host -t A {}".format(a.d))


