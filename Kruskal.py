from Generator import gnp_random_connected_graph
import networkx

def algoritm(edges, edge_num):
    mentioned_edges=set()
    vertexes={}
    weights=[]
    Tree=[]
    for vertex1 in range(edge_num):
        vertexes[vertex1]=f'{vertex1}'
        for vertex2 in edges[vertex1]:
            weight=edges[vertex1][vertex2]['weight']
            edge=(weight, (vertex1, vertex2))
            if edge[1][::-1] not in mentioned_edges:
                mentioned_edges.add(edge[1])
                weights.append(edge)
    weights.sort(key=lambda x: x[0])
    i=0
    for vertex in weights:
        vertex1=vertex[1][0]
        vertex2=vertex[1][1]
        if str(vertex2) in vertexes[vertex1]:
            continue
        new_set=vertexes[vertex1]+vertexes[vertex2]
        for ver in new_set:
            vertexes[int(ver)]=new_set
        Tree.append(vertex[1])
        i+=1
        if i==edge_num-1:
            return networkx.Graph(Tree)

if __name__=='__main__':
    print(algoritm(gnp_random_connected_graph(5, 0.5).degree._nodes, 5))
