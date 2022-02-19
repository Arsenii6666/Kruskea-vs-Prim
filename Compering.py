import time
from tqdm import tqdm
from Generator import gnp_random_connected_graph
from networkx.algorithms import tree
from Prime import algoritm as Prime_alg
from Kruskal import algoritm as Kruskal_alg
NUM_OF_ITERATIONS = 100000
time_taken_basic=0
time_taken_my=0
for i in tqdm(range(NUM_OF_ITERATIONS)):
    # note that we should not measure time of graph creation
    G = gnp_random_connected_graph(100, 0.1, False)
    start = time.time()
    Kruskal_alg(G.degree._nodes, 100)
    end = time.time()
    time_taken_my+=end - start
    start = time.time()
    tree.minimum_spanning_tree(G)
    end = time.time()
    time_taken_basic += end - start
basic_result=time_taken_basic / NUM_OF_ITERATIONS
My_result=time_taken_my / NUM_OF_ITERATIONS
print(basic_result)
print(My_result)
print('My algoritm is '+str(My_result/basic_result*100-100)+'% slower')