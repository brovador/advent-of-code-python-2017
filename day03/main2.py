#encoding: utf-8
import os

def main():
	input_file = './input.txt'

	with open(input_file, 'r') as f:
		lines = [l.strip() for l in f]
	
	l = int(lines[0])
	
	m = {}
	m[(0, 0)] = 1

	def find_adjacents(coord):
		l = []
		for i in range(-1, 2):
			for j in range(-1, 2):
				l.append((coord[0] + i, coord[1] + j, ))
		l.remove(tuple(coord))
		return l

	r  = 0
	searching = True
	while searching:
		r += 1
		for i in range(4):
			coords = []
			if i == 0:
				#right-side coords
				coords = [[r, j] for j in range(-r + 1, r + 1)]
			elif i == 1:
				#top-side coords
				coords = [[j, r] for j in reversed(range(-r, r))]
			elif i == 2:
				#left-side coords
				coords = [[-r, j] for j in reversed(range(-r, r))]
			else:
				#bottom-side coords
				coords = [[j, -r] for j in range(-r + 1, r + 1)]
			for coord in coords:
				adjacents = find_adjacents(coord)
				s = 0
				s+= sum(m[a] for a in adjacents if a in m)
				m[tuple(coord)] = s
				if s > l:
					print s
					return

if __name__ == '__main__':
	main()