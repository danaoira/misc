#!/bin/python3

import sys

x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

# update location
def update_location(x, v):
	x = x + v
	return x

# check if same location
def is_same_location(a, b):
	if a == b:
		return True
	else:
		return False

# check if distance decreases
def is_dist_decr(x1, v1, x2, v2):
	if (x1 > x2) and (v1 > v2):
		print('a')
		return False
	elif (x2 > x1) and (v2 > v1):
		print('b')
		return False
	else:
		print('c')
		return True

# set locations
while(is_same_location(x1, x2) is False):
	# error check distance decrease
	if is_dist_decr(x1, v1, x2, v2) is False:
		print('NO')
		break

	# update locations
	x1 = update_location(x1, v1)
	x2 = update_location(x2, v2)

	if is_same_location(x1, x2) is True:
		print('YES')