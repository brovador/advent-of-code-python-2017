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
	
	def generator_sequence(factor, start_number):
		previous_val = start_number
		while True:
			val = (previous_val * factor) % 2147483647
			yield val
			previous_val = val
	
	a = generator_sequence(16807, generators['A'])
	b = generator_sequence(48271, generators['B'])

	count = 0
	for i in range(40 * 1000 * 1000):
		sa = '{0:032b}'.format(a.next())[16:]
		sb = '{0:032b}'.format(b.next())[16:]
		if sa == sb:
			count += 1
	print count
	



	
	

if __name__ == '__main__':
	main()