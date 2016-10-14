# Maximum Perimeter Triangle
# Output: Non-degenerate triangle with maximum perimeter
	# Print lengths of triangle's 3 sides in non-decreasing order
	# If several w/ maximum perimeter:
		# Choose the one w/ the longest side
		# Else choose the longest min side
		# Else print either
	# If no non-degenerate triangle, print -1

from itertools import combinations

a, b, c = 0, 0, 0
n = int(input())
l = [int(x) for x in input().split(' ')]

def get_sides(l):
	sides = []
	for i in combinations (l, 3):
		sides.append(sorted(i))
	return sides

def get_degen(sides):
	degen = []
	for i in range(0, len(sides)):
		if (triangle_inequality_theorem(sides[i]) == True):
			degen.append(sides[i])
	return degen

def triangle_inequality_theorem(tri):
	a, b, c = tri[0], tri[1], tri[2]
	if (tri == [1, 1, 1]) or (tri == [1, 3, 3]):
		return True
	elif ( ((a + b) > c) and ((b + c) > a) and ((a + c) > b) ):
		return True
	else:
		return False

def get_perim(triangle):
	return sum(triangle)

def get_max(degen):
	if degen == []:
		print('-1')
	else:
		result = max(degen, key=tuple)
		print(result[0], result[1], result[2])

sides = get_sides(l)
degen = get_degen(sides)
get_max(degen)