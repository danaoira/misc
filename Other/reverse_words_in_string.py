# Reverse Words in String
# Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.
# The input string does not contain leading or trailing spaces and the words are always separated by a single space.

# Given s = "the sky is blue",
# return "blue is sky the".

# Could you do it in-place without allocating extra space?

s = "the sky is blue"

for i in s.split(' ')[::-1]:
	printline(i, ' ')