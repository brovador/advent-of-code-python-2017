#encoding: utf-8
import os

def main():
	input_file = './input.txt'

	with open(input_file, 'r') as f:
		lines = [l.strip() for l in f]
	
	r = 0
	for l in lines:
		l = map(int, l.split('\t'))
		r += max(l) - min(l)
	print r
	

if __name__ == '__main__':
	main()