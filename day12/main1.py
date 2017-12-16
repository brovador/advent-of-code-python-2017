#encoding: utf-8
import os
import re

def main():
	input_file = './input.txt'

	with open(input_file, 'r') as f:
		lines = [l.strip() for l in f]

	r = re.compile('(\d+) <-> (.+)')
	programs = {}
	for l in lines:
		pid, pids = r.match(l).groups()
		pid = int(pid)
		pids = set([int(x.strip()) for x in pids.split(',')])
		programs[pid] = programs.get(pid, set([])).union(pids)
	
	pid_objective = 0
	valid_pids = set([0])
	searched_pids = set([0])
	pid_list = programs[pid_objective]

	while len(pid_list) > 0:
		x = list(pid_list)[0]
		pid_list.remove(x)
		searched_pids.add(x)
		valid_pids.add(x)
		
		x_pids = programs[x]
		pid_list = pid_list.union([y for y in x_pids if y not in searched_pids])

	print len(valid_pids)





		


		
		
		

	
		
			

		


		

		
	

if __name__ == '__main__':
	main()