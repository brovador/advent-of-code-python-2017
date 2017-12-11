#encoding: utf-8
import os
import re

def main():
	input_file = './input.txt'

	with open(input_file, 'r') as f:
		lines = [l.strip() for l in f]

	n = 256
	skip_size = 0
	position = 0
	lengths = [int(x) for x in lines[0].split(',')]
	numbers = range(n)

	def debug_print():
		result = []
		for i, x in enumerate(numbers):
			if i == position % len(numbers):
				result.append('[{0}]'.format(x))
			else:
				result.append(str(x))
		return ','.join(result)

	for l in lengths:
		tmp = []
		for i in range(l):
			p = (position + i) % len(numbers)
			tmp.append(numbers[p])
		tmp = tmp[::-1]
		for i in range(l):
			p = (position + i) % len(numbers)
			numbers[p] = tmp[i]
		position += l + skip_size
		skip_size += 1
	print numbers[0] * numbers[1]
		


		
		
		

	
		
			

		


		

		
	

if __name__ == '__main__':
	main()