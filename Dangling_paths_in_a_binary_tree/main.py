number_of_nodes = 0
root_node = None
Node_object_container = []
#Will contain values of 1 or 0.
#1 -> that node is a leaf
#0 - > that node is not a leaf
Leaf_reference = []

max_leaf_count = 0
min_leaf_count = 0

class Node:
    global Leaf_reference

    def __init__(self,weight,id):
        self.con1 = None
        self.con2 = None
        self.con3 = None
        self.id = id
        self.weight = weight
        self.degree = 0

    def is_parent(self):
        if(self.degree == 3):
            return 1
        else:
            return 0

    def leaf_check(self):
        if(self.degree>1):
            Leaf_reference[self.id] = 0

    def get_other_connection(self,current_connection):
        if(self.degree == 3):
            #We are at a parent Node, therefor this node is not part of a dangling tree
            return -1
        else:
            #This could be done in a more eligant way but this should work
            if(self.con1 == current_connection):
                if(self.con2 != None):
                    return self.con2
                elif (self.con3 != None):
                    return self.con3
            if (self.con2 == current_connection):
                if (self.con1 != None):
                    return self.con1
                elif (self.con3 != None):
                    return self.con3
            if (self.con3 == current_connection):
                if (self.con2 != None):
                    return self.con2
                elif (self.con1 != None):
                    return self.con1

    def get_upper_connection(self):
        if(self.degree > 1):
            #This node is not a leaf, therefor this function should not be called.
            return -1
        else:
            #This could be done in a more eligant way but this should work
            if(self.con1 != None):
                return self.con1
            if (self.con2 != None):
                return self.con2
            if (self.con3 != None):
                return self.con3

    def connect(self,Node_number):
        if self.con1 == None:
            self.con1 = Node_number
            self.degree += 1
            self.leaf_check()
            return 1
        if self.con2 == None:
            self.con2 = Node_number
            self.degree += 1
            self.leaf_check()
            return 1
        if self.con3 == None:
            self.con3 = Node_number
            self.degree += 1
            self.leaf_check()
            return 1
        else:
            return 0

def Nodes_print():
    global Node_object_container
    for Node in Node_object_container:
        print()
        print('[ID:', Node.id, 'W: ', Node.weight,']')
        print('------->Con1: ',Node.con1)
        print('------->Con2: ', Node.con2)
        print('------->Con3: ', Node.con3)
        print()

def get_inputs():
    global number_of_nodes
    global root_node
    global Node_object_container
    global Leaf_reference
    number_of_nodes, root_node = input().split()
    number_of_nodes = int(number_of_nodes)
    root_node = int(root_node)
    temp_weights = input().split()
    for i in range(number_of_nodes):
        weight = int(temp_weights[i])
        Node_object_container.append(Node(weight,i))
        Leaf_reference.append(1)
    for i in range(number_of_nodes-1):
        Node1, Node2 = input().split()
        Node1 = int(Node1)
        Node2 = int(Node2)
        if (Node_object_container[Node1].connect(Node2) == 0):
            print('Violation in Node Connector ... ')
        if (Node_object_container[Node2].connect(Node1) == 0):
            print('Violation in Node Connector ... ')

def get_inputs_from_file(dir):
    file = open(dir,'r')
    global number_of_nodes
    global root_node
    global Node_object_container
    global Leaf_reference
    line_number = 0
    for line in file:
        if line_number == 0:
            number_of_nodes, root_node = line.split()
            number_of_nodes = int(number_of_nodes)
            root_node = int(root_node)
        elif line_number == 1:
            temp_weights = line.split()

            for i in range(number_of_nodes):
                weight = int(temp_weights[i])
                Node_object_container.append(Node(weight, i))
                Leaf_reference.append(1)
            # print(temp_weights)
            # print(Leaf_reference)
        else:
            Node1, Node2 = line.split()
            Node1 = int(Node1)
            Node2 = int(Node2)
            if(Node_object_container[Node1].connect(Node2) == 0):
                print('Violation in Node Connector ... ')
            if (Node_object_container[Node2].connect(Node1) == 0):
                print('Violation in Node Connector ... ')




        line_number+=1
    file.close()

def find_leaves():
    global Leaf_reference
    global min_leaf_count
    global max_leaf_count
    min_leaf_count = 10**100
    for i in range(len(Leaf_reference)):
        if(Leaf_reference[i] == 1):
            # print('Leaf Found at: ', i)
            temp_weight = find_parent(i)
            if(temp_weight < min_leaf_count):
                min_leaf_count = temp_weight
            if(temp_weight> max_leaf_count):
                max_leaf_count = temp_weight

def find_parent(node):
    global Node_object_container
    #here we will traverse upwards until we find a prent node. ie a node with degree 3
    #the first time we enter this function we will be looking at a leaf
    next_node = Node_object_container[node].get_upper_connection()
    total_weight_counter = Node_object_container[node].weight
    current_node = node
    while(1):
        # wait = input()
        # print('Current Node: ', current_node)
        # print('Next Node: ', next_node)
        if(Node_object_container[next_node].is_parent()):
            #We have reached a parent node
            break
        else:
            previous_node = current_node
            current_node = next_node
            total_weight_counter = total_weight_counter + Node_object_container[current_node].weight
            next_node = Node_object_container[current_node].get_other_connection(previous_node)
    return total_weight_counter


# get_inputs_from_file('./datapub/pub10.in')
get_inputs()
find_leaves()
print(min_leaf_count,max_leaf_count)

# print(Node_object_container[1].get_upper_connection())
# print(Node_object_container[2].get_upper_connection())
# print(Node_object_container[5].get_upper_connection())
# print(Node_object_container[14].get_upper_connection())
# print(Node_object_container[10].get_upper_connection())
#
#
# print(Node_object_container[1].get_other_connection(0))
# print(Node_object_container[1].get_other_connection(2))



# get_inputs()
# Nodes_print()
# print(len(Node_object_container))
# print(type(Leaf_reference[0]))
