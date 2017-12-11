#encoding: utf-8
import os
import re
import operator

def main():
	input_file = './input.txt'

	with open(input_file, 'r') as f:
		lines = [l.strip() for l in f]

	n = 256
	rounds = 64
	
	skip_size = 0
	position = 0
	lengths = [ord(x) for x in lines[0]]
	lengths += [17, 31, 73, 47, 23]
	numbers = range(n)

	def debug_print():
		result = []
		for i, x in enumerate(numbers):
			if i == position % len(numbers):
				result.append('[{0}]'.format(x))
			else:
				result.append(str(x))
		return ','.join(result)
	
	for r in range(rounds):
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
	
	chunks = zip(*[iter(numbers)] * 16)
	chunks = map(lambda c: reduce(operator.__xor__, c), chunks)
	print ''.join(map(lambda x: '{:02x}'.format(x), chunks))

		


		
		
		

	
		
			

		


		

		
	

if __name__ == '__main__':
	main()