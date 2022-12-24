#!/usr/bin/python3
import argparse, os, sys
parser=argparse.ArgumentParser(description="This is tool")
parser.add_argument("-d", type=str, help="Type Domain", required=True)
parser.add_argument("-reconall",help="Type Domain", required=False, action="store_true")


a = parser.parse_args()
def func():
	print("================SOA==================")
	os.system("host -t SOA {}".format(a.d))
	print("=================A====================")
	os.system("host -t A {}".format (a.d))
	print("=================NS===================")
	os.system("host -t NS {}".format(a.d))
	print("=================MX===================")
	os.system("host -t MX {}".format(a.d))

def func2():
	print("==================A===============")
	os.system("host -t A {}".format(a.d))
if (a.reconall) == True:
	func()
else :
	func2()
