#encoding: utf-8
import os
import re
import string
import sys
import copy

def main():
	input_file = './input.txt'

	with open(input_file, 'r') as f:	
		matrix = [list(l.strip()) for l in f]

	def get_matrix_pos(local_pos):
		pos = local_to_matrix(local_pos)
		return matrix[pos[1]][pos[0]]
	
	def set_matrix_pos(local_pos, value):
		pos = local_to_matrix(local_pos)
		matrix[pos[1]][pos[0]] = value

	def local_to_matrix(pos):
		#        y-
		#        |
		#  x- --0,0--- x+
		#        |
		#        y+
		return (pos[0] + len(matrix) / 2, pos[1] + len(matrix) / 2)

	def resize_matrix(new_size):
		if new_size % 2 == 0: return '[ERR] Cant resize matrix into an odd number'
		if new_size < len(matrix): return '[ERR] New size is smaller than older'
		matrix_size = len(matrix)
		rows_to_add = new_size - matrix_size
		top_bottom_rows = rows_to_add / 2
		
		for i in range(top_bottom_rows):
			matrix.insert(0, list('.' * new_size))
			matrix.append(list('.' * new_size))
		for i, row in enumerate(matrix):
			if len(row) == new_size: continue
			matrix[i] = list('.' * top_bottom_rows) + row + list('.' * top_bottom_rows)
	
	def print_matrix():
		print pos, direction
		tmp = get_matrix_pos(pos)
		set_matrix_pos(pos, 'P')
		print '\n'.join([' '.join(row) for row in matrix])
		set_matrix_pos(pos, tmp)
	
	
	bursts = 10000
	pos = (0, 0)
	direction = (0, -1)
	resize_matrix(1001)
	infections = 0
	for i in range(bursts):

		current_node = get_matrix_pos(pos)
		directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
		current_direction = directions.index(direction)

		if current_node == '#':
			# turn right
			direction = directions[(current_direction + 1) % len(directions)]
			# clean node
			set_matrix_pos(pos, '.')
		else:
			# turn left
			direction = directions[(current_direction - 1) % len(directions)]
			# infect node
			set_matrix_pos(pos, '#')
			infections += 1
		pos = (pos[0] + direction[0], pos[1] + direction[1])

	print infections

	


	
	

if __name__ == '__main__':
	main()