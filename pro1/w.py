#!/usr/bin/python3
import argparse,os, sys
parser=argparse.ArgumentParser(description="This is tool")
parser.add_argument("-reconall",type=str,help="Type Domain", required=False)
parser.add_argument("-d", type=str, help="Type Domain", required=True)
a=parser.parse_args()
os.system("host -t A {}".format(a.d))

