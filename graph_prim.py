from collections import namedtuple

Cost = namedtuple('Cost', ['vertex', 'link', 'weight'])

def prim_mst(edges, adjacency, n, s):
    def recalculate_costs(route_costs, visited, unvisited):                
        for i in range(len(route_costs)):
            cost = route_costs[i]
            #print("Calculating cost", cost, route_costs)
            if cost.vertex in visited:
                continue
            
            for node in visited:
                if (node, cost.vertex) in edges:
                    this_route_weight = edges[node, cost.vertex]

                    if this_route_weight <= cost.weight:
                        route_costs[i] = Cost(cost.vertex, node, this_route_weight)
        
        return route_costs   
            
            
    
    initial_weight = 1 + max(edges.values())
    
    routes = []
    visited = set([s])
    unvisited ={i for i in range(1,n+1) if not i == s}
    
    route_costs = [Cost(i, None, initial_weight) for i in range(1, 1 + n)]
    
    #print("Initial costs", route_costs)
    
    for i in range(len(route_costs)):
        cost = route_costs[i]
        if (cost.vertex, s) in edges:
            route_costs[i] = Cost(cost.vertex, s, edges[cost.vertex, s])
    
    while unvisited:        
        
        #print(unvisited, visited, routes, route_costs)
        
        adjacent_nodes = set()
        
        for node in visited:
            for adjacent_node in adjacency[node]:
                if adjacent_node in unvisited:
                    adjacent_nodes.add(adjacent_node)
        
        #print(adjacent_nodes)
        
        next_route = None
        
        min_weight = initial_weight
        next_route = None
        for node in adjacent_nodes:
            route = route_costs[node-1]
            if route.weight <= min_weight:
                min_weight = route.weight
                next_route = route
            
        #print("Next route", next_route)
        routes.append(next_route)
        
        visited.add(next_route.vertex)
        visited.add(next_route.link)
        
        for node in [next_route.link, next_route.vertex]:
            if node in unvisited:
                unvisited.remove(node)
        
        #print(unvisited, visited, routes, next_routes)
        
        recalculate_costs(route_costs, visited, unvisited)
        
        #print(route_costs)
                
                    
            
                    
        #print(unvisited, visited, routes, next_routes)
    
    return sum([c.weight for c in routes])    
    