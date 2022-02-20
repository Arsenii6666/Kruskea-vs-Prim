from Generator import gnp_random_connected_graph
import networkx

def algoritm(graph, edge_num):
    """
    Main part. Get graph and number of its vertexes. Retur tree with minimum weight.
    How it work: 0 edge geted to the tree. Than algoritm get weights and neme of edges,
    which are incedent to it (function Get_closes_vertexes).
    This edges sorted from one with less weight to bigger.
    1st edge is chosen, it and incedent vertexes is added to tree.
    Its maked edge_num-2 times.
    """
    edges=graph.degree._nodes
    added_vertexes={0}
    Tree_edges=[]
    weights=[]
    next_vertex=0
    for i in range(edge_num-1)[::-1]:
        weights+=Get_closes_vertexes(next_vertex, edges[next_vertex], added_vertexes)
        weights.sort(key=lambda x:x[0])
        while True:
            if weights[0][1] in added_vertexes:
                weights.pop(0)
                continue
            next_vertex=weights[0][1]
            break
        added_vertexes.add(next_vertex)
        Tree_edges.append(weights.pop(0)[2])
    return networkx.Graph(Tree_edges) 

def Get_closes_vertexes(vertex, edges, Skip_edge):
    """Get vertex, incident edges and set of edges, that was already eded to tree.
    Return list of this edges, which contai tuble with its weight and to incedent vertexes.
    If geted vertex is alrady in tree, incedent edege does not returned. """
    ansver=[]
    for geted_vertex in edges:
        if geted_vertex in Skip_edge:
            continue
        weight=edges[geted_vertex]['weight']
        ansver.append((weight, geted_vertex, (vertex, geted_vertex)))
    return ansver

if __name__=='__main__':
    print(algoritm(gnp_random_connected_graph(5, 0.5), 5))
