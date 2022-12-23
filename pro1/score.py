#!/usr/bin/python3
import sys
n=float(sys.argv[1])
def score_arg():
	if n >= 0.9 and n <= 1.0: 
		print("A")
	elif n >= 0.8 and n <= 0.9:
		print("B")
	elif n >= 0.7 and n <= 0.8:
		print("C")
	elif n >= 0.6 and n <= 0.7:
		print("D")
	elif n == 0.6 and n < 0.6:
		print("F")
	else:
		print("GET A LIFE VRO")

score_arg()
