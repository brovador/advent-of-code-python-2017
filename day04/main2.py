#encoding: utf-8
import os

def main():
	input_file = './input.txt'

	with open(input_file, 'r') as f:
		lines = [l.strip() for l in f]
	
	valid = 0
	for l in lines:
		words = l.split()
		words = [''.join(sorted(w)) for w in words]
		for i, w in enumerate(words):
			rest = words[i + 1:]
			if w in rest: break
		else:
			valid += 1
	print valid

	

if __name__ == '__main__':
	main()