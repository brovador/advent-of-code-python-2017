#encoding: utf-8
import os

def main():
	input_file = './input.txt'

	with open(input_file, 'r') as f:
		lines = [l.strip() for l in f]
	
	for l in lines:
		l = l + l[0]
		print sum([int(l[i]) * (l[i] == l[i + 1]) for i in range(len(l) - 1)])
	

if __name__ == '__main__':
	main()