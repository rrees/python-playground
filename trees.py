from collections import namedtuple

TreeNode = namedtuple('TreeNode', ['data', 'children'])

def create_tree(root, relations):

	def add_children(root, relations):
		return [TreeNode(data = child, children = add_children(child, relations)) for parent, child in relations if parent == root]

	root = TreeNode(data = root, children = add_children(root, relations))

	return root

def bfs_content(tree, unvisited=None, tree_content=None):
	#print(unvisited, tree_content)

	if tree_content == None:
		tree_content = []
	
	if unvisited == None:
		unvisited = [tree]

	if len(unvisited) == 0:
		print(unvisited)
		return tree_content

	current_node = unvisited[0]	

	tree_content.append(current_node.data)

	unvisited.extend(current_node.children)

	return bfs_content(tree, unvisited[1:], tree_content)









