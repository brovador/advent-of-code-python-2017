#encoding: utf-8
import os

def main():
	input_file = './input.txt'

	with open(input_file, 'r') as f:
		lines = [l.strip() for l in f]
	
	def elements_tuple_gen():
		r = []
		i = 0
		num_prev = 0
		while True:
			r.append(i * 2 * 4)
			result = (0, 1, 1)
			if i > 0:
				num = num_prev + r[i]
				result = (i, num_prev + 2, num + 1)
				num_prev = num
			yield result
			i += 1

	
	result = 0
	for l in lines:
		l = int(l)
		g = elements_tuple_gen()
		while True:
			r = g.next()
			if r[1] <= l <= r[2]:
				
				ring, ring_start, ring_end = r
				ring_side_size = ring * 2
				
				weights = []
				for i in range(ring_side_size):
					weights.append(abs(i - ring_side_size / 2 + 1))

				l_side = (l - ring_start) / ring_side_size
				l_side_pos = l - (l_side * ring_side_size + ring_start)
				l_side_weight = weights[l_side_pos]
				result = l_side_weight + ring
				break
		print result

	

if __name__ == '__main__':
	main()