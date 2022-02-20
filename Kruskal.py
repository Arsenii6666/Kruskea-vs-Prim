from Generator import gnp_random_connected_graph
import networkx

def algoritm(graph, edge_num):
    """
    Main part. Get graph and number of its vertexes.
    Retur tree with minimum weight.
    How it work: all edges geted and sorted, using as a key weight. Than edge with less weight geted.
    If incedent vertexes was not in one graph, we get it to the tree. Else, we get next edge. When we get edge_num-1 edges, alghoritm stoped.
    """
    weights=sorted(graph.edges(data=True), key=lambda x: x[2]["weight"])
    vertexes=set()
    Tree=[]
    for i in range(edge_num):
        vertexes.add(f'{i}')
    i=0
    #main algoritm
    for vertex in weights:
        vertex1=vertex[0]
        vertex2=vertex[1]
        vertex1_set=None
        vertex2_set=None
        for vertexes_set in vertexes:
            if str(vertex1) in vertexes_set:
                vertex1_set=vertexes_set
            if str(vertex2) in vertexes_set:
                vertex2_set=vertexes_set
            if vertex1_set==vertex2_set!=None:
                break
            if (None!=vertex1_set)&(vertex2_set!=None):
                i+=1
                Tree.append((vertex1, vertex2))
                new_set=vertex1_set+vertex2_set
                vertexes=vertexes-{vertex1_set, vertex2_set}
                vertexes.add(new_set)
                break
        if i==edge_num-1:
            return networkx.Graph(Tree)

if __name__=='__main__':
    print(algoritm(gnp_random_connected_graph(5, 0.5), 5))
