import re

L = input().split(" ")
s = []

def rpn(list, s):
	for i in list:
		if i is '+':
			res = s[-2] + s[-1]
			s.pop()
			s.pop()
			s.append(res)
		elif i is '-':
			res = s[-2] - s[-1]
			s.pop()
			s.pop()
			s.append(res)
		elif i is '*':
			res = s[-2] * s[-1]
			s.pop()
			s.pop()
			s.append(res)
		elif i is '/':
			res = s[-2] / s[-1]
			s.pop()
			s.pop()
			s.append(res)
		elif i is '%':
			res = s[-2] % s[-1]
			s.pop()
			s.pop()
			s.append(res)
		elif int(i):
			s.append(int(i))
		print(s)
	return s[0]

print(rpn(L, s))