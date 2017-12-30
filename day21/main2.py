#encoding: utf-8
import os
import re
import string
import sys
import math


def main():
	input_file = './input.txt'

	with open(input_file, 'r') as f:	
		lines = [l.strip() for l in f]

	rules = {x.strip(): y.strip() for (x, y) in map(lambda x: x.split('=>'), lines)}

	def divide_pattern(pattern):
		pattern = pattern.split('/')
		pattern_size = len(pattern)
		block_size = 2 if len(pattern) % 2 == 0 else 3

		blocks_per_row = pattern_size / block_size
		n_blocks = blocks_per_row * blocks_per_row
		blocks = [[] for i in range(n_blocks)]

		for block_idx in range(n_blocks):
			block_x = block_idx % blocks_per_row
			block_y = block_idx / blocks_per_row

			pattern_x = block_x * block_size
			pattern_y = block_y * block_size

			for y in range(pattern_y, pattern_y + block_size):
				blocks[block_idx].append(pattern[y][pattern_x:pattern_x + block_size])
		
		for i, block in enumerate(blocks):
			blocks[i] = '/'.join(blocks[i])
		return blocks

	def merge_pattern(pattern_blocks):
		if len(pattern_blocks) == 1:
			return pattern_blocks[0]

		n_blocks = len(pattern_blocks)
		block_size = len(pattern_blocks[0].split('/'))

		blocks_per_row = int(math.sqrt(n_blocks))
		pattern_rows = blocks_per_row * block_size
		pattern = [[] for i in range(pattern_rows)]

		for block_idx, block in enumerate(pattern_blocks):
			block = block.split('/')
			block_x = block_idx % blocks_per_row
			block_y = block_idx / blocks_per_row
			pattern_line = block_y * block_size
			for block_line_idx, block_line in enumerate(block):
				pattern[pattern_line + block_line_idx].append(block_line)
		return '/'.join([''.join(line) for line in pattern])


	
	def rotate_pattern(pattern):
		pattern = pattern.split('/')
		# https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
		rotated = zip(*pattern[::-1])
		return '/'.join([''.join(s) for s in rotated])
	
	def flip_pattern(pattern):
		pattern = pattern.split('/')
		return '/'.join([x[::-1] for x in pattern])

	def desc(pattern):
		return pattern.replace('/', '\n')
	
	
	iterations = 18
	pattern = '.#./..#/###'
	for iteration in range(iterations):
		pattern_blocks = divide_pattern(pattern)
		for i, block in enumerate(pattern_blocks):
			for r, v in rules.iteritems():
				if len(r) != len(block):
					continue
				r_on = len([x for x in r if x == '#'])
				block_on = len([x for x in block if x == '#'])
				if r_on != block_on:
					continue
				for j in range(4):
					r = rotate_pattern(r)
					if block == r or block == flip_pattern(r):
						pattern_blocks[i] = v
						break
				else:
					continue
				break
		pattern = merge_pattern(pattern_blocks)
	print len([x  for x in desc(pattern) if x == '#'])
	

if __name__ == '__main__':
	main()