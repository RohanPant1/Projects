import networkx as nx
import matplotlib.pyplot as plt
import random
import math

g=nx.Graph()

# generate graph
nodes_classes = ['N30', 'T30']
waps =  {'N30':['WAP1', 'WAP2', 'WAP3'], 'T30':['WAP4', 'WAP5', 'WAP6']}
devices = {'N30': ['JIO0054', 'RIG0013', 'LOM0028'], 'T30':['LIG0098', 'PAN0092', 'TRU0124']}
count = 0

for clas in nodes_classes:
    g.add_node('IT', type='IT',  pos=[random.uniform(0, 5), random.uniform(0, 5)])
    g.add_node(clas, type='class',  pos=[random.uniform(0, 5), random.uniform(0, 5)])
    g.add_edge(clas, 'IT', connection='IT-class')
    for i in waps.values():
        for wap in i:
            g.add_node(wap, type='WAP', pos=[random.uniform(0, 5), random.uniform(0, 5)])
            g.add_edge(clas, wap, connection='class-wap' )
            count= count+1

for item in devices.keys():
    for device in devices[item]:
        g.add_node(device, type='device', pos=[random.uniform(0, 5), random.uniform(0, 5)])
        g.add_edge(device, item, connection =  'class-device')

pos = nx.get_node_attributes(g, "pos")

for i in devices.keys():
    for device in devices[i]:
        for wap in waps[i]:
            distance = math.sqrt(pow(pos[device][0]+pos[wap][0], 2)+ pow(pos[device][1]+pos[wap][1], 2))
            g.add_edge(device, wap, weight= distance, connection='WAP-device')

#setup dictionary to track number of devices in a class
device_count =  {}
nodes_type = nx.get_node_attributes(g, 'type')
nodes_devices = []
nodes_wap =  []

for item in nodes_type.keys():
    if nodes_type[item]=='device':
        nodes_devices.append(item)
    if nodes_type[item]=='WAP':
        nodes_wap.append(item)

#Count devices
def count_devices():
    global device_count
    global nodes_classes
    for item in nodes_classes:
        temp_count = 0
        for i in g.neighbors(item):
            if i in nodes_devices:
                temp_count = temp_count + 1
        device_count[item] = temp_count
count_devices()

#find_device
def find_device(device_name):
    dfs_stack = ['IT']
    visited =  []
    while len(dfs_stack)>0:
        current_node = dfs_stack.pop()
        if current_node not in visited:
            visited.append(current_node)
            for item in g.neighbors(current_node):
                if item not in visited:
                    dfs_stack.append(item)
        if device_name in visited:
            for i in g.neighbors(device_name):
                if g.nodes[i]['type']=='class':
                    print("It is in", i)
            break

# Heuristic part of solution begins
weight_limit = 10
cost = {}
for device in nodes_devices:
    cost[device]=random.randint(1, 10)
cost['None']=0

#initialise values
t_i = 100
t_f=0
temp_increment = .1
device_in_waps = {}
total_speed = 0
new_device_in_waps = {}
best_speed =0 
best_device_in_waps = {}
for setup in nodes_wap:
    device_in_waps[setup]=[[], weight_limit]

# generates a random solution
# inserts device into wap if it can be connected by it
def insert_wap():
    temp_list = device_wap[0]
    temp_list.append(device)
    device_wap[0]=temp_list
    device_wap[1]=device_wap[1]-cost[device]

#finds the bandwith from the waps to the devices
def find_speed(device):
    global new_speed
    global g
    new_speed = 0
    for wap in nodes_wap:
        for j in device[wap][0]:
            if g.has_edge(j, wap):
                new_speed = new_speed+ g[j][wap]['weight']
find_speed(device_in_waps)
total_speed = new_speed

#generates random solution
temp_count = 0
for clas in nodes_classes:
    temp_count = 0
    for device in devices[clas]:
        device_wap = device_in_waps[waps[clas][temp_count]]
        if device_wap[1]>=cost[device]:
            insert_wap()
        else:
            temp_count = temp_count+1
            device_wap = device_in_waps[waps[clas][temp_count]]
            insert_wap()

# swaps solution
def choose_swap(room):
    global new_device_in_waps
    choices = waps[room]
    random_choice = random.sample(choices, 2)
    new_device_in_waps = device_in_waps

    #randomising first device to swap
    first_rand  = random_choice[0]
    rand = {first_rand:new_device_in_waps[first_rand][0]}
    if len(rand[first_rand])>0:
        rand[first_rand] = random.choice(rand[first_rand])
    else:
        rand[first_rand]= 'None'
    
    #randomising second device to swap
    second_rand = random_choice[1]
    rand[second_rand]=new_device_in_waps[second_rand][0]
    if len(rand[second_rand])>0:
        rand[second_rand] = random.choice(rand[second_rand])
    else:
        rand[second_rand]= 'None'

    #placing new devices in dictionary: devices_in_waps
    for i in new_device_in_waps[first_rand][0]:
        temp_list = new_device_in_waps[first_rand][0]
        if i == rand[first_rand]: 
                temp_list.remove(i)
                temp_list.append(rand[second_rand])
                if rand[second_rand] =='None':
                    temp_list.remove(rand[second_rand])
                new_device_in_waps[first_rand][0] = temp_list
                new_device_in_waps[first_rand][1] = new_device_in_waps[first_rand][1] + cost[i] - cost[rand[second_rand]]
                break

    for i in new_device_in_waps[second_rand][0]:
        temp_list = new_device_in_waps[second_rand][0]
        if i == rand[second_rand]:
                temp_list.remove(i)
                temp_list.append(rand[first_rand])
                if rand[first_rand]=='None':
                    temp_list.remove(rand[first_rand])
                new_device_in_waps[second_rand][0] = temp_list
                new_device_in_waps[second_rand][1] = new_device_in_waps[second_rand][1] + cost[i] - cost[rand[first_rand]]
                break

def main_swap_solution(rooms):
    global new_device_in_waps
    check = False
    while check == False:
        choose_swap(rooms)
        check = True
        for i in new_device_in_waps.values():
            if i[1]<0:
                check=False

#executes the simulated annealing part of the solution
while t_i>t_f:
    main_swap_solution(clas)
    find_speed(new_device_in_waps)
    delta_speed = new_speed-total_speed
    probabilty_acceptance = math.e**(-1*delta_speed/t_i)

    if new_speed>total_speed:
        best_speed = new_speed
        best_device_in_waps = new_device_in_waps
    elif probabilty_acceptance>random.uniform(0, 1):
        total_speed = new_speed
        device_in_waps = new_device_in_waps
    t_i = t_i-temp_increment
print('The maximum speed of all devices combined is', best_speed)

#colors the edges which shows which which device is connected to which WAP
color_list = []
print('The optimal configuration is', best_device_in_waps)
for key in best_device_in_waps.keys():
    for j in device_in_waps[key][0]:
        if g.has_edge(j, key):
            this_tuple = (best_device_in_waps[key][0][0],key)
            color_list.append(this_tuple)

nx.draw(g,pos = pos, with_labels=True, font_size= 6)

nx.draw_networkx_edges(g, pos, edgelist=color_list, edge_color="red")
plt.show()    

