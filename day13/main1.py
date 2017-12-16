#encoding: utf-8
import os
import re

def main():
	input_file = './input.txt'

	with open(input_file, 'r') as f:
		lines = [l.strip() for l in f]

	configuration = {}
	r = re.compile('(\d+): (\d+)')
	for l in lines:
		x, y = map(int, r.match(l).groups())
		configuration[x] = y
	
	n_layers = max(configuration.keys()) + 1
	
	layers = [0] * n_layers
	layers_idx = [-1] * n_layers

	def update_state(second):
		for i in range(n_layers):
			if configuration.has_key(i):
				n = configuration[i] - 1
				v = second % (n * 2)
				if v >= n:
					v = 2 * n - v
				layers_idx[i] = v
			else:
				layers_idx[i] = -1
	
	def draw_state(second):
		for i in range(n_layers):
			if layers_idx[i] == 0:
				layers[i] = 'S'
			else:
				layers[i] = '.'
		print '\t'.join(layers)
	
	caught = 0
	for i in range(n_layers):
		update_state(i)
		caught += configuration[i] * i if layers_idx[i] == 0 else 0
	print caught







		


		
		
		

	
		
			

		


		

		
	

if __name__ == '__main__':
	main()