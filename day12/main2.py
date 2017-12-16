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
	
	groups = 0
	
	while len(programs.keys()) > 0:
		pid_objective = programs.keys()[0]
		valid_pids = set([pid_objective])
		searched_pids = set([pid_objective])
		pid_list = programs[pid_objective]

		while len(pid_list) > 0:
			x = list(pid_list)[0]
			pid_list.remove(x)
			searched_pids.add(x)
			valid_pids.add(x)
			
			x_pids = programs[x]
			pid_list = pid_list.union([y for y in x_pids if y not in searched_pids])

		for x in valid_pids:
			del programs[x]
		groups += 1
	print groups






		


		
		
		

	
		
			

		


		

		
	

if __name__ == '__main__':
	main()