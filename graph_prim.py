from collections import namedtuple

Cost = namedtuple('Cost', ['vertex', 'link', 'weight'])

def prim_mst(edges, adjacency, n, s):
    def recalculate_costs(route_costs, visited, unvisited):                
        for i in range(len(route_costs)):
            for node in adjacency[i+1]:
                cost = route_costs[i]

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

    for node in adjacency[s]:
        route_costs[node - 1] = Cost(node, s, edges[node, s])
    
    while unvisited:        
        
        #print(unvisited, visited, routes, route_costs)
        
        next_route = None
        
        min_weight = initial_weight
        next_route = None
        for node in unvisited:
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
    