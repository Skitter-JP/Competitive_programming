import time

number_of_nodes = 0
number_of_paths = 0

node_container = []
lake_node_reference = []

walk_counter = 0
class Node:
    global node_container

    def __init__(self,id):
        self.id = id
        self.type = None
        self.degree = 0
        self.connections = []
        self.visited = False


    def add_connection(self,other_node):
        self.connections.append(other_node)
        self.degree+=1
        node_container[other_node].connections.append(self.id)
        node_container[other_node].degree +=1

def node_print():
    for i in range(len(node_container)):
        print('----Node:{}----'.format(i))
        print('----Type: ', node_container[i].type)
        print('----Degree: ',node_container[i].degree)
        print('---Connections---')
        for j in range(len(node_container[i].connections)):
            print('-------->',node_container[i].connections[j])
        print('--------------')

def get_inputs_from_file(dir):
    global node_container
    global lake_node_reference
    global number_of_paths
    global number_of_nodes
    file = open(dir, 'r')
    line_number = 0

    temp_connection_data = []

    for line in file:
        if line_number == 0:
            number_of_nodes, number_of_paths = line.split()
            number_of_nodes = int(number_of_nodes)
            number_of_paths = int(number_of_paths)

            for i in range(number_of_nodes):
                # We generate all the nodes
                temp_node = Node(i)
                node_container.append(temp_node)

        elif line_number < number_of_paths+1:
            node1, node2 = line.split()
            node1 = int(node1)
            node2 = int(node2)
            temp_connection_data.append([node1, node2])
            # node_container[node1].add_connection(node2)

        else:
            node, type = line.split()
            node = int(node)
            if type == 'L':
                type = 0
                lake_node_reference.append(node)
            elif type == 'W':
                type = 1
            node_container[node].type = type
        line_number += 1

    file.close()

    for i in range(number_of_paths):
        node1 = temp_connection_data[i][0]
        node2 = temp_connection_data[i][1]
        # print(temp_connection_data[i])
        # print('ID: {}, Type: {} '.format(node1,node_container[node1].type ))
        # print('ID: {}, Type: {} '.format(node2,node_container[node2].type ))
        if node_container[node1].type != node_container[node2].type:

            node_container[node1].add_connection(node2)

def sort_connections():
    global node_container
    for node in node_container:
        node.connections.sort()

def get_inputs():
    global node_container
    global lake_node_reference

    temp_connection_data = []


    number_of_nodes,number_of_paths = input().split()
    number_of_nodes = int(number_of_nodes)
    number_of_paths = int(number_of_paths)

    for i in range(number_of_nodes):
        #We generate all the nodes
        temp_node = Node(i)
        node_container.append(temp_node)


    for i in range(number_of_paths):
        node1, node2 = input().split()
        node1 = int(node1)
        node2 = int(node2)
        temp_connection_data.append([node1,node2])
        # node_container[node1].add_connection(node2)


    for i in range(number_of_nodes):
        #get the types of nodes here
        node, type = input().split()
        node = int(node)
        if type == 'L':
            type = 0
            lake_node_reference.append(node)
        elif type == 'W':
            type =1
        node_container[node].type = type

    for i in range(number_of_paths):
        node1 = temp_connection_data[i][0]
        node2 = temp_connection_data[i][1]

        if node_container[node1].type != node_container[node2].type:
            node_container[node1].add_connection(node2)


def walk_finder():
    global node_container
    global lake_node_reference
    global walk_counter
    for i in lake_node_reference:
        avoid1 = []
        avoid2 = []
        # avoid2 = []
        # print('Node: ', i)
        if node_container[i].degree > 1:
            for j in node_container[i].connections:
                if j != i :
                    # print('------First Sub ID: ', j)
                    for k in node_container[j].connections:
                        if node_container[k].visited == False and k != i and k!=j:
                            # print('----------------Second Sub ID: ', k)
                            for l in node_container[k].connections:
                                if l != i and l!=j and l!=k and node_container[l].type == 1:
                                    # print('-----------------------Third Sub ID: ', l)
                                    for m in node_container[l].connections:
                                        if m == i:
                                            # print('--------------------------- Walk Found [{},{},{},{},{}]'.format(i,j,k,l,m))
                                            # avoid1.append(j)
                                            # avoid2.append(k)
                                            # avoid2.append(j)
                                            node_container[i].visited = True
                                            walk_counter+=2


# start = time.time()
# get_inputs_from_file('./datapub/pub09.in')
# end = time.time()
# print('Getting Data time',end - start)
# # sort_connections()
# # get_inputs()
# # node_print()
# # print(lake_node_reference)
# start = time.time()
# walk_finder()
# end = time.time()
# print('Walk finder time',end - start)
# print(walk_counter)

get_inputs()
walk_finder()
print(walk_counter)