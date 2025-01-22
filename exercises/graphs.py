from collections import namedtuple

SearchData = namedtuple('SearchData', ['path_weights', 'previous', 'remaining'])

def recreate_path(i, j, previous):
	path = []
	path_node = j
	while path_node:
		path.insert(0, path_node)
		path_node = previous[path_node]
	return [i] + path

def shortest_route(i, j, n, edges, search_data=None):

	if search_data == None:
		initial_weight = 1 + sum(edges.values())
		path_weights =  {p:0 if p == i else initial_weight for p in range(n)}

		search_data = SearchData(
			path_weights = path_weights,
			previous = {},
			remaining = sorted([p for p in range(n)], key = lambda x: path_weights[x])
			)

	if search_data and len(search_data.remaining) == 0:
		return (recreate_path(i,j, search_data.previous), search_data.path_weights[j])

	current_node = search_data.remaining[0]

	adjacent_nodes = [b for a, b in edges.keys() if a == current_node]
		
	#print(adjacent_nodes)

	for node in adjacent_nodes:
		next_step = search_data.path_weights[current_node] + edges[(current_node, node)]
		if search_data.path_weights[node] > next_step:
			search_data.previous[node] = current_node
			search_data.path_weights[node] = next_step

	return shortest_route(i, j, n, edges, search_data = SearchData(
		path_weights = search_data.path_weights,
		previous = search_data.previous,
		remaining = search_data.remaining[1:]
		))


