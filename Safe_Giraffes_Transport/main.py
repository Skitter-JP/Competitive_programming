import time

number_of_cities = 0
number_of_roads = 0
starting_city  = 0
target_city = 0
min_walk_length = 10**10000

node_container = []
first_exams = []
second_exams = []



class Node:
    global node_container

    def __init__(self, id):
        self.id = id
        self.type = None
        self.degree = 0
        self.connections = []

        self.unknown_connections = []
        self.num_unknown_con =0

        self.found_connections = []
        self.num_found_con = 0

        self.distance_to_end = None


    def add_connection(self, other_node):
        self.connections.append(other_node)
        self.degree += 1

    def add_unknown_con(self,node):
        self.unknown_connections.append(node)
        self.num_unknown_con+=1

    def add_found_con(self,node,distance):

        if node in self.unknown_connections:
            self.unknown_connections.remove(node)
            self.num_unknown_con-=1
        self.found_connections.append([node,distance])
        self.num_found_con+=1

    def is_connected(self,node):
        if node in self.found_connections:
            return True
        else:
            return False

def create_exan_exam_con(node1,node2,distance):
    global node_container
    node_container[node1].add_found_con(node2,distance)
    node_container[node2].add_found_con(node1, distance)

def node_print():
    for i in range(len(node_container)):
        print('----Node:{}----'.format(i))
        print('----Type: ', node_container[i].type)
        print('----Degree: ',node_container[i].degree)
        print('----Unkown Connections: ', node_container[i].unknown_connections)
        print('----# Unknown Con: ', node_container[i].num_unknown_con)
        print('----Found Connections: ', node_container[i].found_connections)
        print('----# Found Con: ', node_container[i].num_found_con)
        print('---Connections---')
        for j in range(len(node_container[i].connections)):
            print('-------->',node_container[i].connections[j])
        print('----------------------------')




def populate_unkown_connections():
    global first_exams
    global second_exams
    global node_container
    for i in first_exams:
        for k in second_exams:
            node_container[i].add_unknown_con(k)
    for i in second_exams:
        for k in first_exams:
            node_container[i].add_unknown_con(k)


def BFS_end(root,current_distance):

    global node_container
    global min_walk_length
    global target_city

    root_obj = node_container[root]

    if root_obj.distance_to_end != None:

        total_distance = root_obj.distance_to_end + current_distance + 1
        if total_distance < min_walk_length:
            min_walk_length = total_distance
        return
    else:

        q = []
        visited_nodes = []
        distance_of_node = []
        for i in range(number_of_cities):
            visited_nodes.append(False)
            distance_of_node.append(0)

        current_node_id = root
        cur_node_obj = node_container[current_node_id]
        visited_nodes[current_node_id] = True
        type = node_container[current_node_id].type
        q.extend(cur_node_obj.connections)

        for i in q:
            if i != current_node_id:
                visited_nodes[i] = True
                distance_of_node[i] = 1

                if i == target_city:

                    root_obj.distance_to_end = 1
                    total_distance = root_obj.distance_to_end + current_distance + 1
                    # print("End found from E2:{}, D:{}, TD:{}", i, distance_of_node[i], total_distance)
                    if total_distance < min_walk_length:
                        min_walk_length = total_distance
                    return

        while (q):

            current_node_id = q.pop(0)
            cur_node_obj = node_container[current_node_id]

            for i in cur_node_obj.connections:

                if not visited_nodes[i]:
                    q.append(i)
                    distance_of_node[i] = distance_of_node[current_node_id] + 1
                    visited_nodes[i] = True

                    if i == target_city:
                        root_obj.distance_to_end = distance_of_node[i]
                        total_distance = root_obj.distance_to_end + current_distance + 1
                        # print("End found from E2:{}, D:{}, TD:{}", i, distance_of_node[i], total_distance)
                        if total_distance < min_walk_length:
                            min_walk_length = total_distance
                        return


def BFS_start():
    global node_container
    global min_walk_length
    global starting_city
    q = []
    visited_nodes = []
    distance_of_node = []
    for i in range(number_of_cities):
        visited_nodes.append(False)
        distance_of_node.append(0)

    current_node_id = starting_city
    cur_node_obj = node_container[current_node_id]
    visited_nodes[current_node_id] = True
    type = node_container[current_node_id].type
    q.extend(cur_node_obj.connections)

    for i in q:
        if i != current_node_id:
            visited_nodes[i] = True
            distance_of_node[i] = 1
            i_node_obj = node_container[i]
            if i_node_obj.type != type and i_node_obj != None:
                if distance_of_node[i] < min_walk_length:
                    # print("1st E found, S:{} to E1:{}, Distance:{}, Type:{}".format(starting_city,i,distance_of_node[i],i_node_obj.type))
                    BFS_exam_to_exam(i,distance_of_node[i])

    while(q):

        current_node_id = q.pop(0)
        cur_node_obj = node_container[current_node_id]

        for i in cur_node_obj.connections:
            i_node_obj = node_container[i]
            if not visited_nodes[i]:
                q.append(i)
                distance_of_node[i] = distance_of_node[current_node_id]+1
                visited_nodes[i] = True

                if i_node_obj.type != type and i_node_obj.type !=None:
                    if distance_of_node[i] < min_walk_length:
                        # print("1st E found, S:{} to E1:{}, Distance:{}, Type:{}".format(starting_city,i,distance_of_node[i],i_node_obj.type))
                        BFS_exam_to_exam(i, distance_of_node[i])

def BFS_exam_to_exam(root,current_length):
    global node_container
    global min_walk_length

    root_obj = node_container[root]

    if root_obj.num_found_con !=0:
        for i in node_container[root].found_connections:

            if (i[1]+current_length) < min_walk_length:
                # print("Find_connection to: {}".format(i))
                BFS_end(i[0],i[1]+current_length)

    if root_obj.num_unknown_con !=0:
        #Here we will find the remaining connections

        q = []
        visited_nodes = []
        distance_of_node = []
        for i in range(number_of_cities):
            visited_nodes.append(False)
            distance_of_node.append(0)

        current_node_id = root
        cur_node_obj = node_container[current_node_id]
        visited_nodes[current_node_id] = True
        type = node_container[current_node_id].type
        q.extend(cur_node_obj.connections)

        for i in q:
            if i != current_node_id:
                visited_nodes[i] = True
                distance_of_node[i] = 1
                i_node_obj = node_container[i]
                if i_node_obj.type != type and i_node_obj.type != None and not cur_node_obj.is_connected(i):

                    create_exan_exam_con(root,i,distance_of_node[i])

                    if (distance_of_node[i]+current_length) < min_walk_length:
                        # print("------------>E1:{} to E2:{}, D:{}".format(root, i,distance_of_node[i]))
                        BFS_end(i,distance_of_node[i]+current_length)

                if root_obj.num_unknown_con == 0:
                    return

        while (q):

            if root_obj.num_unknown_con == 0:
                return

            current_node_id = q.pop(0)
            cur_node_obj = node_container[current_node_id]

            for i in cur_node_obj.connections:
                i_node_obj = node_container[i]
                if not visited_nodes[i]:
                    q.append(i)
                    distance_of_node[i] = distance_of_node[current_node_id] + 1
                    visited_nodes[i] = True

                    if i_node_obj.type != type and i_node_obj.type != None and not cur_node_obj.is_connected(i):

                        create_exan_exam_con(root, i, distance_of_node[i])

                        if (distance_of_node[i]+current_length) < min_walk_length:
                            # print("------------>E1:{} to E2:{}, D:{}".format(root, i,distance_of_node[i]))
                            BFS_end(i, distance_of_node[i] + current_length)

def get_inputs():
    global number_of_roads
    global number_of_cities
    global starting_city
    global target_city
    global first_exams
    global second_exams

    number_of_cities, number_of_roads, starting_city, target_city = input().split()
    number_of_cities = int(number_of_cities)
    number_of_roads = int(number_of_roads)
    starting_city = int(starting_city)
    target_city = int(target_city)

    for i in range(number_of_cities):
        temp_node = Node(i)
        node_container.append(temp_node)

    for i in range(number_of_roads):
        # connect some nodes here ...
        node1, node2 = input().split()
        node1 = int(node1)
        node2 = int(node2)
        node_container[node1].add_connection(node2)
        node_container[node2].add_connection(node1)

    temp_first_exam = input().split()
    temp_second_exam = input().split()

    # print(temp_first_exam)

    number_of_first_exams = int(temp_first_exam[0])
    number_of_second_exams = int(temp_second_exam[0])

    # print(number_of_first_exams)

    for i in range(number_of_first_exams):
        first_exams.append(int(temp_first_exam[i + 1]))
        node_container[int(temp_first_exam[i + 1])].type = 1
    for i in range(number_of_second_exams):
        second_exams.append(int(temp_second_exam[i + 1]))
        node_container[int(temp_second_exam[i + 1])].type = 2


# -----------TESTING FUNCTIONS---------------------
def get_inputs_from_file(dir):
    global number_of_roads
    global number_of_cities
    global starting_city
    global target_city
    global first_exams
    global second_exams

    file = open(dir, 'r')

    line_number = 0

    temp_first_exam = 0
    temp_second_exam = 0

    for line in file:
        if line_number == 0:
            number_of_cities, number_of_roads, starting_city, target_city = line.split()
            number_of_cities = int(number_of_cities)
            number_of_roads = int(number_of_roads)
            starting_city = int(starting_city)
            target_city = int(target_city)
            # print(number_of_cities, number_of_roads, starting_city, target_city)
            for i in range(number_of_cities):
                temp_node = Node(i)
                node_container.append(temp_node)
        elif line_number <= number_of_roads:
            node1, node2 = line.split()
            node1 = int(node1)
            node2 = int(node2)
            # print(node1,node2)
            node_container[node1].add_connection(node2)
            node_container[node2].add_connection(node1)

        elif line_number == number_of_roads + 1:
            temp_first_exam = line.split()
            # first_exam = int(first_exam)
            number_of_first_exams = int(temp_first_exam[0])
            for i in range(number_of_first_exams):
                first_exams.append(int(temp_first_exam[i + 1]))
                node_container[int(temp_first_exam[i + 1])].type = 1
            # print("First Exams: ",first_exams)
        elif line_number == number_of_roads + 2:
            temp_second_exam = line.split()
            number_of_second_exams = int(temp_second_exam[0])
            for i in range(number_of_second_exams):
                second_exams.append(int(temp_second_exam[i + 1]))
                node_container[int(temp_second_exam[i + 1])].type = 2
            # print("Second Exams: ",second_exams)

        line_number += 1

    file.close()

def get_reference_result(dir):

    file = open(dir)
    for line in file:
        awnser =  line.strip("\n")

    file.close()
    return int(awnser)

def reset_all_data():
    global number_of_cities
    global number_of_roads
    global starting_city
    global target_city
    global min_walk_length

    global node_container
    global first_exams
    global second_exams

    number_of_cities = 0
    number_of_roads = 0
    starting_city = 0
    target_city = 0
    min_walk_length = 10 ** 10000

    node_container = []
    first_exams = []
    second_exams = []

def test_all():

    correct_counter =0

    string = '../../pubdata/'

    for i in range(1,11):
        print('-----------------------------------')
        reset_all_data()
        if i < 10:
            end = 'pub0' + str(i)
        else:
            end = 'pub' + str(i)
        file = string + end

        file_out = file + '.out'

        file_in = file + '.in'
        print("Testing: ",file)
        main_start = time.time()
        get_inputs_from_file(file_in)
        populate_unkown_connections()
        BFS_start()
        main_end = time.time()
        print("Time:", main_end-main_start)
        print("Reference Awnser: ",get_reference_result(file_out))

        if get_reference_result(file_out) == min_walk_length:
            print("{} --- Good ! :)".format(min_walk_length))
            correct_counter+=1
        else:
            print("{} --- Bad :( ".format(min_walk_length))
        print('-----------------------------------')
    print("{}/10 Correct".format(correct_counter))

# -----------TESTING FUNCTIONS END-----------------

# test_all()

# get_inputs_from_file('./pubdata/pub02.in')
get_inputs()
populate_unkown_connections()
# node_print()
BFS_start()
print(min_walk_length)