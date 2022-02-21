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

def Print_Grafic(Use_big_data: bool, Num_of_vertexes=None, complitness=None):
    x_cor=[]
    prim_cor=[]
    kruskal_cor=[]
    for j in range(10):
        j+=1
        i=j*5
        if Use_big_data:
            i*=10
        j/=10
        if (Num_of_vertexes==None)&(complitness==None):
            return "Please give more information(Num_of_vertexes or complitness)"
        if  (Num_of_vertexes!=None)&(complitness!=None):
            return "You give to much data"
        if complitness==None:
            j=complitness
            x=i
            x_axis_name='x - num of vertexes'
            answer=f"{j} complitness"
        else:
            i=Num_of_vertexes
            x=j
            x_axis_name='x - complitness'
            answer=f"{i} vertexes"

        x_cor.append(x)
        result=Itererions(i, j)
        kruskal_cor.append(result[0])
        prim_cor.append(result[1])
    grafiks.plot(x_cor, kruskal_cor, label = "Kruskal")
    grafiks.plot(x_cor, prim_cor, label = "Prim")
    grafiks.xlabel(x_axis_name)
    grafiks.ylabel('y - average time')
    grafiks.title(f'A graph comparison of two algorithms ({50} iterations, {answer})')
    grafiks.legend()
    grafiks.show()

