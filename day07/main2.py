#encoding: utf-8
import os
import re
import collections

def main():
	input_file = './input.txt'

	with open(input_file, 'r') as f:
		lines = [l.strip() for l in f]
	
	nodes = {}
	# each node is a tuple defined by: name, weight, parent

	def update_node(name, weight = 0, parent = None, children = []):
		node = nodes.get(name, {'weight' : weight, 'parent' : parent, 'children' : []})
		if parent:
			node['parent'] = parent
		if weight:
			node['weight'] = weight
		if children:
			node['children'] = children
		nodes[name] = node

	r = re.compile('(\w+) \((\d+)\)')
	for l in lines:
		parts = l.split('->')
		name, weight = r.match(parts[0]).groups()
		children = [] if len(parts) == 1 else [x.strip() for x in parts[1].split(',')]
		map(lambda c: update_node(c, parent = name), children)
		update_node(name, int(weight), children = children)

	root = {k: v for k, v in nodes.iteritems() if v['parent'] is None}.keys()[0]

	def calculate_weight(name):
		node = nodes[name]
		result = node['weight']
		for c in node['children']:
			result += calculate_weight(c)
		node['total_weight'] = result
		return result
	
	calculate_weight(root)
	
	def print_branch(name, indent = 0):
		if indent > 1:
			return
		print '\t' * indent, '{0} ({1} - {2})'.format(name, nodes[name]['weight'], nodes[name]['total_weight'])
		children = {k: v for k, v in nodes.iteritems() if v['parent'] == name}
		for k in children:
			print_branch(k, indent + 1)
	
	# find first node un-balanced but with balanced sub-towers
	def search_unbalanced(node):
		result = None
		weights = [nodes[name]['total_weight'] for name in nodes[node]['children']]
		weights = collections.Counter(weights).most_common()
		if len(weights) == 1:
			# all child balanced, current node is the one to balance
			result = node
		else:
			# search in the unbalanced child
			node_to_search = [name for name in nodes[node]['children'] if nodes[name]['total_weight'] == weights[1][0]][0]
			print '{0} -> {1}'.format(node, node_to_search)
			result = search_unbalanced(node_to_search)
		return result
	
	node_to_balance = search_unbalanced(root)
	node_to_balance_data = nodes[node_to_balance]
	
	node_to_balance_total_weight = node_to_balance_data['total_weight']
	node_to_balance_parent = node_to_balance_data['parent']
	node_to_balance_siblings_weight = [nodes[name]['total_weight'] for name in nodes[node_to_balance_parent]['children']][0]
	weight_diff = node_to_balance_siblings_weight - node_to_balance_total_weight
	
	print node_to_balance_data['weight'] + weight_diff

		




	
	# print_branch(root)


	# cnt = collections.Counter([nodes[n]['total_weight'] for n in nodes[root]['children']])
	# weights = cnt.most_common()
	# weight_update = reduce(lambda x, y: x[0] - y[0], weights)
	# node_to_update = [nodes[name] for name in nodes[root]['children'] if nodes[name]['total_weight'] == weights[1][0]][0]
	# print node_to_update['weight'] + weight_update
	
	
	
		
		

		
	

if __name__ == '__main__':
	main()