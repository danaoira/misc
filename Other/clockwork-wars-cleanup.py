# Project: 		Clockwork Wars Cleanup
# Description: 	A greedy sort to simulate the tile cleanup for the Clockwork Wars board game.
# Input: 		A randomized list of alphanumeric values.
# Output:		A sorted list of alphanumeric values in a matrix.
# Programmer:	Dana Oira Toribio
# Duration:		8/6/2016 - 8/6/2016

# Outline:
	# Value generation
		# Values: V1-V7, C1-C7, L1-L7, F1-F7, T1-T7, M1-M7, S1-S7
		# RegEx: [(C|F|L|M|S|T|V)(1-7)]
	# Randomize values
	# Place values into matrix
	# Print results to file

import random

alpha = ['C', 'F', 'L', 'M', 'S', 'T', 'V']

def create_tiles(alpha):
	tiles = []
	for i in alpha:
		for j in range(1, 8):
			val = i + str(j)	# => 'C1', 'C2', etc
			tiles.append(val)
	random.shuffle(tiles)
	return tiles

def create_matrix(row, col):
	return [['  ' for x in range(col)] for y in range(row)]

def write_input(f, val):
	f.write(str(val) + '\n\n')

def write_result(res):
	for i in res:
		f.write(str(i) + '\n')
	f.write('\n')

def update_result(tiles):
	for i in tiles:
		f.write('Round ' + str(tiles.index(i) + 1) + ' (' + str(i) + ')\n')
		result[int(i[1]) - 1][alpha.index(i[0])] = i	# ex. C1 => [0][1]
		write_result(result)

f = open('results.txt', 'w')

print('Running Clockworks Wars Cleanup')

print('... creating randomized list')
tiles = create_tiles(alpha)
write_input(f, tiles)

print('... creating matrix')
result = create_matrix(7, 7)

print('... updating result')
write_result(result)
update_result(tiles)

print('... completed result for ' + str(len(tiles)) + ' tiles')