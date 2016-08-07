# Project: 		Clockwork Wars Cleanup
# Description: 	A program to simulate the tile cleanup for the Clockwork Wars board game.
# Input: 		A randomized list of alphanumeric values.
# Output:		A sorted list of alphanumeric values in a matrix.
# Programmer:	Dana Oira Toribio
# Duration:		8/6/2016 - TBA

# TO DO
	# Value generation
		# Values: V1-V7, C1-C7, L1-L7, F1-F7, T1-T7, M1-M7, S1-S7
		# Regex: [(C|F|L|M|S|T|V)(1-7)]
	# Randomize values
	# Do some sort of sort
	# Print each result

import random

def generate_tiles():
	tiles = []
	alpha = ['C', 'F', 'L', 'M', 'S', 'T', 'V']

	for i in alpha:
		for j in range(1, 8):
			val = i + str(j)
			tiles.append(val)
	random.shuffle(tiles)
	return tiles

tiles = gen_tiles()
print(tiles)