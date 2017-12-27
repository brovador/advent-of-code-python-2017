#encoding: utf-8
import os
import re
import string
import sys


def main():
	input_file = './input.txt'

	with open(input_file, 'r') as f:	
		lines = [l for l in f]

	maze = [[] for i in range(len(lines))]
	for i, line in enumerate(lines):
		map(lambda x: maze[i].append(x), line)
	
	
	if not all([len(x) == len(maze[0]) for x in maze]):
		print '[ERR] Unbalanced maze'
		print [len(x) for x in maze]
		return
	
	#    | y
	#  --+-- x (x, y)
	#    |
	pos = (0, 0)
	d = (0, 1)
	for i, x in enumerate(maze[0]):
		if x == '|':
			pos = (i, 0)
			break
	
	def maze_pos(pos):
		result = ' '
		if pos[1] < len(maze) and pos[0] < len(maze[pos[1]]):
			result = maze[pos[1]][pos[0]]
		return result
	
	def add_coords(c1, c2):
		return (c1[0] + c2[0], c1[1] + c2[1])
	
	letters = []
	while True:
		c = maze_pos(pos)
		# print c, pos, d, letters
		# raw_input()
		if c == '|' or c == '-':
			# continue with same direction
			# check if need to pass under
			pass
		elif c == '+':
			# change direction to the opposite axis
			if d[0] != 0:
				# change from x to y axis
				d1 = (0, -1)
				c1 = maze_pos(add_coords(pos, d1))
				d = d1 if c1 != ' ' else (0, 1)
			else:
				# change from y to x axis
				d1 = (-1, 0)
				c1 = maze_pos(add_coords(pos, d1))
				d = d1 if c1 != ' ' else (1, 0)
		elif c == ' ':
			# no next direction, end of the road
			break
		else:
			# letter found
			letters.append(c)
		pos = add_coords(pos, d)
	print ''.join(letters)





	

	

if __name__ == '__main__':
	main()