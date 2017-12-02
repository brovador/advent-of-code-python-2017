#encoding: utf-8
import os

def main():
	input_file = './input.txt'

	with open(input_file, 'r') as f:
		lines = [l.strip() for l in f]
	
	r = 0
	for l in lines:
		l = sorted(map(int, l.split('\t')))[::-1]
		for i in l:
			l2 = filter(lambda x: x <= i / 2, l)
			s = sum([(i / x) if i % x == 0 else 0 for x in l2])
			if s > 0:
				r += s
				break
	print r
	

if __name__ == '__main__':
	main()