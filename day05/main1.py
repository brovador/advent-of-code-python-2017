#encoding: utf-8
import os

def main():
	input_file = './input.txt'

	with open(input_file, 'r') as f:
		lines = [l.strip() for l in f]
	
	jumps = [int(l) for l in lines]
	pos = 0

	def print_jumps(jumps, pos):
		values = []
		for i, j in enumerate(jumps):
			values.append(str(j) if i != pos else '({0})'.format(j))
		return ' '.join(values)
	
	print_jumps(jumps, pos)
	i = 0
	while True:
		i += 1
		v = jumps[pos]
		jumps[pos] += 1
		pos += v
		#print '{0}: {1}'.format(i, print_jumps(jumps, pos))
		if pos >= len(jumps):
			break
	print i
	

if __name__ == '__main__':
	main()