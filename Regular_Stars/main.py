import time

node_container = []
node_leaf_reference = []
potential_roots = []

number_of_nodes = 0
number_of_edges = 0

graph_counter = 0

regular_star_counter = 0



class Node():
    global node_leaf_reference
    global potential_roots

    def __init__(self,id):
        self.id = id
        self.is_leaf = True
        self.degree = 0
        self.connections = []
        self.graph_id = -1
        self.distance_from_star = 0
        self.in_potential_roots = False
        self.distance_from_root = 0
        self.visited = False

    def add_connection(self,node):
        self.connections.append(node)
        self.degree+=1
        if self.degree > 1:
            self.is_leaf = False
            node_leaf_reference[self.id] = 0
        if self.degree > 2 and self.in_potential_roots == False:
            potential_roots.append(self.id)
            self.in_potential_roots = True


def node_print():
    global node_container
    global potential_roots
    for i in node_container:
        print('---------------------------')
        print("Node ID: ",i.id)
        print("Degree:",i.degree)
        print("Is Leaf: ",i.is_leaf)
        print("Graph ID:",i.graph_id)
        print("Distance From Star:", i.distance_from_star)
        print("Connections")
        # for j in range(len(i.connections)):
        #     print('----->',i.connections[j])
        for j in i.connections:
            print('----->',j)
        print('---------------------------')
    print("Potential Roots:", potential_roots)
    print("Leaves Nodes:",node_leaf_reference)


def BFS(root):
    global node_container
    global graph_counter
    global number_of_nodes


    q = []



    current_node = root
    current_node_obj = node_container[current_node]
    current_node_obj.graph_id = graph_counter
    current_node_obj.visited = True
    current_node_obj.distance_from_root = 0
    q.extend(current_node_obj.connections)

    leaf_dist = -1

    for i in q:
        i_node_obj = node_container[i]
        if i != current_node:
            i_node_obj.visited = True
            i_node_obj.distance_from_root = 1
            i_node_obj.graph_id = graph_counter
            i_node_obj.distance_from_star = i_node_obj.distance_from_root
            if i_node_obj.is_leaf:
                if leaf_dist == -1:
                    leaf_dist = i_node_obj.distance_from_root
                else:
                    if i_node_obj.distance_from_root != leaf_dist:
                        return 0



    while(q):

        current_node = q.pop(0)
        current_node_obj = node_container[current_node]

        for i in current_node_obj.connections:
            i_node_obj = node_container[i]
            if i_node_obj.visited == False:
                q.append(i)
                i_node_obj.distance_from_root = current_node_obj.distance_from_root+1
                i_node_obj.visited = True
                i_node_obj.graph_id = graph_counter
                i_node_obj.distance_from_star = i_node_obj.distance_from_root
                if i_node_obj.is_leaf:
                    if leaf_dist == -1:
                        leaf_dist = i_node_obj.distance_from_root
                    else:
                        if i_node_obj.distance_from_root != leaf_dist:
                            return 0

    return 1



def graph_finder():
    global node_container
    global potential_roots
    global graph_counter
    global regular_star_counter

    for i in potential_roots:
        # print("Starting at: ",i)
        BFS_r=BFS(i)
        if BFS_r == 1:
            regular_star_counter+=1
        graph_counter+=1


def get_inputs():
    global node_container
    global node_leaf_reference
    global number_of_nodes
    global number_of_edges


    number_of_nodes,number_of_edges = input().split()

    number_of_nodes = int(number_of_nodes)
    number_of_edges = int(number_of_edges)

    for i in range(number_of_nodes):
        node_obj = Node(i)
        node_container.append(node_obj)
        node_leaf_reference.append(1)


    for i in range(number_of_edges):
        node1,node2 = input().split()
        node1 = int(node1)
        node2 = int(node2)

        node_obj = node_container[node1]
        node_obj.add_connection(node2)
        node_obj = node_container[node2]
        node_obj.add_connection(node1)

# -----------Testing Functions----------------------------------
def reset_all_data():
    global node_container
    global node_leaf_reference
    global potential_roots
    global number_of_nodes
    global number_of_edges
    global graph_counter
    global regular_star_counter

    node_container = []
    node_leaf_reference = []
    potential_roots = []
    number_of_nodes = 0
    number_of_edges = 0
    graph_counter = 0
    regular_star_counter = 0


def get_reference_result(dir):
    file = open(dir)
    for line in file:
        awnser = line.strip("\n")

    file.close()
    return int(awnser)

def get_inputs_from_file(dir):
    global node_container
    global node_leaf_reference
    global number_of_nodes
    global number_of_edges


    file = open(dir,'r')

    line_number = 0

    for line in file:

        if line_number == 0:
            number_of_nodes, number_of_edges = line.split()
            number_of_nodes = int(number_of_nodes)
            number_of_edges = int(number_of_edges)
            for i in range(number_of_nodes):
                node_obj = Node(i)
                node_container.append(node_obj)
                node_leaf_reference.append(1)
            line_number += 1


        else:
            node1, node2 = line.split()
            node1 = int(node1)
            node2 = int(node2)
            node_obj = node_container[node1]
            node_obj.add_connection(node2)
            node_obj = node_container[node2]
            node_obj.add_connection(node1)


    file.close()


def test_all(type):
    correct_counter = 0
    string = './pubdata/'
    if (type > 10 or type < 1) and type != -1:
        print("Type must be between 1 and 10")
        return ValueError
    if type != -1:
        for i in range(type, type+1):
            print('-----------------------------------')
            reset_all_data()
            if i < 10:
                end = 'pub0' + str(i)
            else:
                end = 'pub' + str(i)
            file = string + end

            file_out = file + '.out'

            file_in = file + '.in'
            print("Testing: ", file)
            main_start = time.time()
            get_inputs_from_file(file_in)
            graph_finder()
            # reg_star_finder()
            # node_print()
            print("Number of Graphs: ",graph_counter)
            main_end = time.time()
            print("Time:", main_end - main_start)
            print("Reference Awnser: ", get_reference_result(file_out))

            if get_reference_result(file_out) == regular_star_counter:
                print("{} --- Good ! :)".format(regular_star_counter))
                correct_counter += 1
            else:
                print("{} --- Bad :( ".format(regular_star_counter))
            print('-----------------------------------')


    else:
        for i in range(1, 11):
            print('-----------------------------------')
            reset_all_data()
            if i < 10:
                end = 'pub0' + str(i)
            else:
                end = 'pub' + str(i)
            file = string + end

            file_out = file + '.out'

            file_in = file + '.in'
            print("Testing: ", file)
            main_start = time.time()
            get_inputs_from_file(file_in)
            graph_finder()
            # reg_star_finder()
            # node_print()
            print("Number of Graphs: ", graph_counter)
            main_end = time.time()
            print("Time:", main_end - main_start)
            print("Reference Awnser: ", get_reference_result(file_out))

            if get_reference_result(file_out) == regular_star_counter:
                print("{} --- Good ! :)".format(regular_star_counter))
                correct_counter += 1
            else:
                print("{} --- Bad :( ".format(regular_star_counter))
            print('-----------------------------------')
        print("{}/10 Correct".format(correct_counter))

# -----------Testing Functions END------------------------------

# test_all(10)
# test_all(-1)


get_inputs()
graph_finder()
print(regular_star_counter)

# get_inputs()
# get_inputs_from_file('./pubdata/pub01.in')
# node_print()
# graph_finder()
# print(graph_counter)
# reg_star_finder()
# print("found reg stars: ",regular_star_counter)
# node_print()



