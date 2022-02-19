import time
from tqdm import tqdm
from Generator import gnp_random_connected_graph
from networkx.algorithms import tree
from Prime import algoritm as Prime_alg
from Kruskal import algoritm as Kruskal_alg
def Itererions(vertexes, chance, code_1_name, code_2_name):
    NUM_OF_ITERATIONS = 10000
    time_taken_code_1=0
    time_taken_code_2=0
    for i in tqdm(range(NUM_OF_ITERATIONS)):
        #note that we should not measure time of graph creation
        G = gnp_random_connected_graph(vertexes, chance, False)
        start = time.time()
        tree.minimum_spanning_tree(G)
        end = time.time()
        time_taken_code_1 += end - start
        start = time.time()
        Kruskal_alg(G.degree._nodes, vertexes)
        end = time.time()
        time_taken_code_2+=end - start
    code_1=time_taken_code_1 / NUM_OF_ITERATIONS
    code_2=time_taken_code_2 / NUM_OF_ITERATIONS
    if code_1<code_2:
        return code_1, code_1_name, code_2, code_2_name, code_2/code_1*100-100
    return code_2, code_2_name, code_1, code_1_name, code_1/code_2*100-100

for i, j in zip([5,10,15,20,25,30,35,40,45,50], range(10)):
    j+=1
    j/=10
    j=0.1
    result=Itererions(i, j, 'basik', 'Kazimir')
    with open('Data.txt', mode='a', encoding='utf-8') as f:
        f.write(f"{result[1]} (time {result[0]}) is quicker then {result[3]} (time {result[2]}) at {result[4]}%. (Verteves: {i}, Chance: {j})\n")
print()


