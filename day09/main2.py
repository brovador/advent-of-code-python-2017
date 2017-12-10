#encoding: utf-8
import os
import re

def main():
	input_file = './input.txt'

	with open(input_file, 'r') as f:
		lines = [l.strip() for l in f]

	def clean_line(l):
		i = 0
		result = []
		while i < len(l):
			if l[i] == '!':
				i += 2
			else:
				result.append(l[i])
				i += 1
		return ''.join(result)

	def process_stream(stream):
		# sequences starts with { and ends with }
		# things separated by , (groups or garbage)
		# garbage starts with < and ends with >
		# any character after ! should be ignored
		result = 0
		garbage = False
		#print '\t' * score, stream
		while len(stream):
			c = stream[0]
			del stream[0]
			if not garbage:
				if c == '<':
					garbage = True
				elif c == '{':
					result += process_stream(stream)
				elif c == '}':
					break
			else:
				if c == '>':
					garbage = False
				else:
					result += 1
		return result
	
	scores = []
	for l in lines:
		l = list(clean_line(l))
		scores.append(process_stream(l))
	print sum(scores)
	

		
		
		

	
		
			

		


		

		
	

if __name__ == '__main__':
	main()