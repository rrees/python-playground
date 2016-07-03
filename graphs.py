def recreate_path(i, j, previous):
	path = []
	path_node = j
	while path_node:
		path.insert(0, path_node)
		path_node = previous[path_node]
	return [i] + path

def shortest_route(i, j, n, edges, path_weights=None, previous=None, remaining=None):
	if not remaining == None and len(remaining) == 0:
		return (recreate_path(i,j, previous), path_weights[j])

	if path_weights == None:
		initial_weight = 1 + sum(edges.values())
		path_weights = {p:0 if p == i else initial_weight for p in range(n)}

	if remaining == None:
		remaining = [p for p in range(n)]
		remaining = sorted(remaining, key = lambda x: path_weights[x])

	if previous == None:
		previous = {}	

	current_node = remaining[0]

	adjacent_nodes = [b for a, b in edges.keys() if a == current_node]
		
	#print(adjacent_nodes)

	for node in adjacent_nodes:
		next_step = path_weights[current_node] + edges[(current_node, node)]
		if path_weights[node] > next_step:
			previous[node] = current_node
			path_weights[node] = next_step

	remaining = remaining[1:]

	return shortest_route(i, j, n, edges, path_weights, previous, remaining)


