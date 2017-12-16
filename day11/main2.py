#encoding: utf-8
import os
import re
import math
import string

def main():
	input_file = './input.txt'

	with open(input_file, 'r') as f:
		lines = [l.strip() for l in f]

	#using cube coordinates
	v_directions = {
		'n'  : ( 0,  1, -1),
		'ne' : ( 1,  0, -1),
		'se' : ( 1, -1,  0),
		's'  : ( 0, -1,  1),
		'sw' : (-1,  0,  1),
		'nw' : (-1,  1,  0)
	}

	def distance(a, b):
		return sum(map(lambda x: abs(x[0] - x[1]), zip(a,b))) / 2
	
	origin = (0, 0, 0)
	max_distance = 0
	for l in lines:
		directions = map(string.strip, l.split(','))
		end = (0, 0, 0)
		for direction in directions:
			end = map(sum, zip(end, v_directions[direction]))
			max_distance = max(max_distance, distance(origin, end))
	print max_distance

		


		
		
		

	
		
			

		


		

		
	

if __name__ == '__main__':
	main()