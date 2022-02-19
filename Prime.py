from Generator import gnp_random_connected_graph
import networkx
def algoritm(edges, edge_num):
    added_vertexes={0}
    Tree_edges=[]
    weights=[]
    next_vertex=0
    for i in range(edge_num-1)[::-1]:
        weights+=Get_closes_vertexes(next_vertex, edges[next_vertex], added_vertexes)
        weights.sort(key=lambda x:x[0])
        next_vertex=weights[0][1]
        added_vertexes.add(next_vertex)
        Tree_edges.append(weights.pop(0)[2])
        if len(weights)>i:
            weights=weights[:i]
    return networkx.Graph(Tree_edges) 

def Get_closes_vertexes(vertex, edges, Skip_edge):
    ansver=[]
    for geted_vertex in edges:
        if geted_vertex in Skip_edge:
            continue
        weight=edges[geted_vertex]['weight']
        ansver.append((weight, geted_vertex, (vertex, geted_vertex)))
    return ansver

if __name__=='__main__':
    print(algoritm(gnp_random_connected_graph(5, 0.5).degree._nodes, 5))
