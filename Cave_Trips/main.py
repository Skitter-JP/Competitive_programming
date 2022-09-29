import time

node_container = []
number_of_caves = 0
number_of_direct_paths = 0
length_min = 0
length_max = 0

number_of_hikes = 0

found_hikes = []

time_in_find_hikes = 0

loop_find_time=0

group_counter = 0

class Node:
    def __init__(self,id):
        self.id = id
        self.degree = 0
        self.connections = []
        self.con_dic = {}


    def add_connection(self,node,distance):
        self.connections.append([node,distance])
        self.con_dic[node] = distance
        self.degree+=1

    def sort_connections(self):
        self.connections.sort()

    def node_in_connections(self,node_seek):

        if node_seek in self.con_dic:
                return True
        return False


def node_print():
    global node_container

    for i in node_container:
        print('---------------------------')
        print("Node ID: ", i.id)
        print("Degree:", i.degree)
        print("Connections")
        # for j in range(len(i.connections)):
        #     print('----->',i.connections[j])
        for j in i.connections:
            print('----->', j)
        print('---------------------------')


def get_inputs():
    global node_container
    global number_of_caves
    global length_max
    global length_min
    global number_of_direct_paths

    number_of_caves,number_of_direct_paths,length_min,length_max = input().split()
    number_of_caves = int(number_of_caves)
    number_of_direct_paths = int(number_of_direct_paths)
    length_min = int(length_min)
    length_max = int(length_max)

    for i in range(number_of_caves):
        node_container.append(Node(i))

    for i in range(number_of_direct_paths):
        node1,node2,length = input().split()
        node1 = int(node1)
        node2 = int(node2)
        length = int(length)
        node_container[node1].add_connection(node2,length)
        node_container[node2].add_connection(node1, length)


def get_inputs_from_file(dir):
    global node_container
    global number_of_caves
    global length_max
    global length_min
    global number_of_direct_paths

    file = open(dir,'r')

    line_number = 0

    for line in file:

        if line_number == 0:
            number_of_caves, number_of_direct_paths, length_min, length_max = line.split()
            number_of_caves = int(number_of_caves)
            number_of_direct_paths = int(number_of_direct_paths)
            length_min = int(length_min)
            length_max = int(length_max)

            for i in range(number_of_caves):
                node_container.append(Node(i))

            line_number += 1
        else:
            node1, node2, length = line.split()
            node1 = int(node1)
            node2 = int(node2)
            length = int(length)
            node_container[node1].add_connection(node2, length)
            node_container[node2].add_connection(node1, length)

    file.close()


def sort_node_connections():
    global node_container

    for node in node_container:
        node.sort_connections()

def max_distance_check(dis):
    global length_max

    if dis <= length_max:
        return True
    else:
        return False

def min_distance_check(dis):
    global length_min

    if dis >= length_min:
        return True
    else:
        return False



def hike_finder():
    global node_container
    global number_of_caves
    global length_max
    global length_min
    global found_hikes
    global number_of_hikes
    global time_in_find_hikes
    global con_loop



    for i in range(number_of_caves):
        node1_obj = node_container[i]
        # print('1st Node: ',node1_obj.id)

        for j in reversed(node1_obj.connections):
            node2_obj = node_container[j[0]]
            if i >= node2_obj.id:
                break
            if not max_distance_check(j[1]):
                continue
            # print('-------->2nd Node: ', node2_obj.id)

            for k in reversed(node2_obj.connections):
                node3_obj = node_container[k[0]]
                if node3_obj.id <= node1_obj.id:
                    break
                if not max_distance_check(j[1] + k[1]):
                    # print('-------->Max Distance Reached')
                    continue

                # print('----------------------->3rd Node: ', node3_obj.id)

                # if node_in_connections(node3_obj,node1_obj.id):
                if node3_obj.node_in_connections(node1_obj.id):
                    # print('----------------------->Loop Found')
                    continue


                for l in reversed(node3_obj.connections):
                    node4_obj = node_container[l[0]]

                    if node4_obj.id <= node2_obj.id:
                        break
                    if not max_distance_check(j[1]+ k[1]+l[1]):
                        # print('----------------------->Max Distance Reached')
                        continue

                    # print('------------------------------------->4th Node: ', node4_obj.id)

                    # if node_in_connections(node4_obj, node2_obj.id):
                    if node4_obj.node_in_connections(node2_obj.id):
                        # print('------------------------------------->Loop Found')
                        continue


                    for m in node4_obj.connections:

                        node5_obj = node_container[m[0]]
                        if node5_obj.id > i:
                            break
                        # if node5_obj.id == node3_obj.id:
                        #     continue
                        # print('------------------------------------------------->5th Node: ', node5_obj.id)
                        if i == m[0]:
                            if max_distance_check(j[1] + k[1] + l[1] + m[1]) and min_distance_check(
                                    j[1] + k[1] + l[1] + m[1]):
                                # print('-------------------------------------------------------->Hike Found: ({},{},{},{},{})'.format(i,j[0],k[0],l[0],m[0]))
                                # print('-------------------------------------------------------->Distance: ', j[1]+ k[1]+l[1]+m[1])
                                number_of_hikes += 1
                                break




get_inputs()
sort_node_connections()
hike_finder()

print(number_of_hikes)


