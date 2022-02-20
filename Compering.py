import time
from tqdm import tqdm
from Generator import gnp_random_connected_graph
from networkx.algorithms import tree
from Prime import algoritm as Prime_alg
from Kruskal_1 import algoritm as Kruskal_alg
import matplotlib.pyplot as grafiks
def Itererions(vertexes, chance):
    NUM_OF_ITERATIONS = 50
    time_taken_code_1=0
    time_taken_code_2=0
    for i in tqdm(range(NUM_OF_ITERATIONS)):
        #note that we should not measure time of graph creation
        G = gnp_random_connected_graph(vertexes, chance, False)
        start = time.time()
        Kruskal_alg(G, vertexes)
        end = time.time()
        time_taken_code_1 += end - start
        start = time.time()
        Prime_alg(G, vertexes)
        end = time.time()
        time_taken_code_2+=end - start
    code_1=time_taken_code_1 / NUM_OF_ITERATIONS
    code_2=time_taken_code_2 / NUM_OF_ITERATIONS
    return code_1, code_2

x_cor=[]
prim_cor=[]
kruskal_cor=[]
for j in range(10):
    j+=1
    i=j*50
    j/=10

    j=1

    x_cor.append(i)
    result=Itererions(i, j)
    kruskal_cor.append(result[0])
    prim_cor.append(result[1])
grafiks.plot(x_cor, kruskal_cor, label = "Kruskal")
grafiks.plot(x_cor, prim_cor, label = "Prim")
grafiks.xlabel('x - num of vertexes')
grafiks.ylabel('y - average time')
grafiks.title(f'A graph comparison of two algorithms ({50} iterations, {j} complitness)')
grafiks.legend()
grafiks.show()

