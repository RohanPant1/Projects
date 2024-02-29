import networkx as nx
import matplotlib.pyplot as plt
import math
import random

n = 20
# generate graph
g = nx.random_geometric_graph(n, radius=0.5, seed=2)
nx.draw(g)
pos = nx.get_node_attributes(g, "pos")
for i in range(len(pos)):
    for j in range(i+1, len(pos)):
        dist = math.sqrt(pow(pos[i][0]+pos[j][0], 2)+ pow(pos[i][1]+pos[j][1], 2))
        g.add_edge(i, j, weight=dist)

#initialise values
t_i = 100
t_f=0
temp_increment = 0.1

#generate path
path = list(g.nodes()).copy()
path.append(0)
distance = 0
for i in range(0, len(path)-1):
    distance = distance + g[path[i]][path[i+1]]["weight"]

#swap path function
def swap_path():
    global new_path
    global new_distance

    new_path = path
    swap_number = random.sample(range(0, n-1), 2)
    temp = new_path[swap_number[0]]
    new_path[swap_number[0]] = new_path[swap_number[1]]
    new_path[swap_number[1]] = temp
    new_path[-1] = new_path[0]
    new_distance = 0
    for i in range(0, len(path)-1):
        new_distance = new_distance + g[new_path[i]][new_path[i+1]]["weight"]

#goes through all the iterations
while t_i>t_f:
    swap_path()
    # 1/(1+math.exp(delta_distance/t_i))
    delta_distance = new_distance - distance
    probabilty_acceptance = math.e**(-1*delta_distance/t_i)

    if new_distance>distance:
         best_distance =  new_distance
         best_path= new_path
    elif probabilty_acceptance>random.uniform(0, 1):
        distance = new_distance
        path = new_path
    t_i = t_i-temp_increment

print(path)
print(distance)
    
plt.show()    

