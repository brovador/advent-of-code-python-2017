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
	layers_idx = [-1] * n_layers
	
	delay = 0
	keys = sorted(configuration.keys())
	while True:
		for i in keys:
			n = configuration[i] - 1
			v = (delay + i) % (n * 2)
			v = 2 * n - v if v >= n else v
			if v == 0:
				break
		else:
			break
		delay += 1
	print delay







		


		
		
		

	
		
			

		


		

		
	

if __name__ == '__main__':
	main()