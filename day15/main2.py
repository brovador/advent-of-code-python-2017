#encoding: utf-8
import os
import re


def main():
	input_file = './input.txt'

	with open(input_file, 'r') as f:
		lines = [l.strip() for l in f]

	r = re.compile('Generator (\w) starts with (\d+)')
	generators = {}
	for l in lines:
		name, start = r.match(l).groups()
		generators[name] = int(start)
	
	def generator_sequence(factor, start_number, multiples):
		previous_val = start_number
		while True:
			val = (previous_val * factor) % 2147483647
			if val % multiples == 0:
				yield val
			previous_val = val
	
	a = generator_sequence(16807, generators['A'], 4)
	b = generator_sequence(48271, generators['B'], 8)

	s = ['0101000010011111100110000010010001001001100010001000010110001000',
	'0111011010111100101111101011000000110011011010001111010010000000',
	'0001111110100011110101000110010001000101001000001110100001111000',
	'0111011000000100101010011011000001100000010100110001010101001000',
	'0010110000100000100111100101100000011000100100101011101101010000'
	]

	count = 0
	for i in range(5 * 1000 * 1000):
		sa = '{0:032b}'.format(a.next())[16:]
		sb = '{0:032b}'.format(b.next())[16:]
		if sa == sb:
			count += 1
	print count
	



	
	

if __name__ == '__main__':
	main()