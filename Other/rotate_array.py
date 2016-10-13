# Rotate Array
# Rotate an array of n elements to the right by k steps.

print('Enter integers, separated by commas:')
l = [int(x) for x in input().split(',')]
k = int(input('Enter how many steps to rotate: '))

def rotate_array(l, k):
	arr_a = []
	arr_b = []

	for i in range(0, k+1):
		arr_a.append(l[i])

	for j in range(k+1, len(l)):
		arr_b.append(l[j])

	return arr_b + arr_a

print(rotate_array(l, k))