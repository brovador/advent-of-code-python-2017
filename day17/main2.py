#encoding: utf-8
import os
import re
import string


def main():
	input_file = './input.txt'

	with open(input_file, 'r') as f:
		lines = [l.strip() for l in f]
	
	spins = int(lines[0])
	insertions = 50000000
	state = [0]
	pos = 0

	def state_str(state, pos):
		return ' '.join(str(x) if i != pos else '({0})'.format(x) for i, x in enumerate(state))
	
	results = []
	for i in range(insertions):
		pos = (pos + (spins + 1)) % (i + 1)
		if pos == 0:
			results.append((i + 1))
	print results[-1]
	

if __name__ == '__main__':
	main()