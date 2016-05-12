
try:
    import matplotlib.pyplot as plt
except:
    raise

import networkx as nx
import itertools

G=nx.Graph()

def connected(tup):
    unconnected = list(tup)
    flag = True
    for vertex in tup:
        for test in unconnected:
            if vertex == test:
                continue
            if not G.has_edge(vertex,test):
                flag = False
    return flag
        
def create(g):
    G.add_edges_from(g)
    max_len_clique = 0;
    max_clique = []
    tuples = []
    for i in xrange(3,len(G.nodes())):
         tuples.extend(list(itertools.combinations(G.nodes(),i)))
    for tup in tuples:
        if connected(tup):
            if(len(tup)>max_len_clique):
                max_clique = tup;
                max_len_clique = len(tup)
    nx.draw(G)
    plt.savefig("simple_path.png") # save as png
    plt.show() # display
    print max_clique

if __name__ == "__main__":
    create([(0,1),(0,3),(0,4),(1,3),(1,4),(2,4),(2,5),(3,4),(4,5),(5,8),(6,7),(7,4),(7,8)])