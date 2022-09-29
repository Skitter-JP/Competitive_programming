matrix = []
row_size = 0
column_size = 0
red_node_container = []
green_node_container = []
blue_node_container = []

robot_node =0

number_of_nodes = 0

RGB_parameter =10**100


class node():

    def __init__(self,id, x_pos, y_pos, type):
        self.id = id
        # self.x_pos = x_pos+1
        # self.y_pos = y_pos+1
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.type = type


def get_inputs():
    global matrix
    global column_size
    global row_size
    global robot_node
    global number_of_nodes
    global red_node_container
    global green_node_container
    global blue_node_container

    row_size, column_size = input().split()
    row_size = int(row_size)
    column_size = int(column_size)
    for i in range(row_size):
        row = list(input())
        for j in range(len(row)):
            if row[j] == 'X':
                temp_node = node(-1,j,i,'X')
                robot_node = temp_node
            elif row[j] == 'R':
                temp_node = node(number_of_nodes,j, i, 'R')
                red_node_container.append(temp_node)
                number_of_nodes += 1
            elif row[j] == 'G':
                temp_node = node(number_of_nodes,j, i, 'G')
                green_node_container.append(temp_node)
                number_of_nodes += 1
            elif row[j] == 'B':
                temp_node = node(number_of_nodes, j, i, 'B')
                blue_node_container.append(temp_node)
                number_of_nodes += 1
        matrix.append(row)

def get_inputs_from_file(dir):

    global matrix
    global column_size
    global row_size
    global robot_node
    global number_of_nodes
    global red_node_container
    global green_node_container
    global blue_node_container

    file = open(dir,'r')

    line_number = 0
    i =0
    for line in file:
        if line_number == 0:
            row_size, column_size = line.split()
            row_size = int(row_size)
            column_size = int(column_size)
        if line_number >0:
            line = line.rstrip('\n')
            row = list(line)

            for j in range(len(row)):
                if row[j] == 'X':
                    temp_node = node(-1, j, i, 'X')
                    robot_node = temp_node
                elif row[j] == 'R':
                    temp_node = node(number_of_nodes,j, i, 'R')
                    red_node_container.append(temp_node)
                    number_of_nodes += 1
                elif row[j] == 'G':
                    temp_node = node(number_of_nodes, j, i, 'G')
                    green_node_container.append(temp_node)
                    number_of_nodes += 1
                elif row[j] == 'B':
                    temp_node = node(number_of_nodes, j, i, 'B')
                    blue_node_container.append(temp_node)
                    number_of_nodes += 1
            i+=1
            matrix.append(row)
        line_number+=1

def color_node_print():
    global red_node_container
    global green_node_container
    global blue_node_container
    print('----------------ROBOT Node-----------------')
    print('Node ID: ', robot_node.id)
    print('--------Coordinate [X,Y] -> [{},{}]'.format(robot_node.x_pos, robot_node.y_pos))
    print('----------------RED Nodes-----------------')
    for node in red_node_container:
        print('Node ID: ',node.id)
        print('--------Coordinate [X,Y] -> [{},{}]'.format(node.x_pos,node.y_pos))
    print('---------------GREEN Nodes----------------')
    for node in green_node_container:
        print('Node ID: ',node.id)
        print('--------Coordinate [X,Y] -> [{},{}]'.format(node.x_pos,node.y_pos))

    print('---------------BLUE Nodes----------------')
    for node in blue_node_container:
        print('Node ID: ',node.id)
        print('--------Coordinate [X,Y] -> [{},{}]'.format(node.x_pos,node.y_pos))

def parameter_calculator(R_co,G_co,B_co):
    global robot_node
    temp_y =[robot_node.y_pos,R_co.y_pos,G_co.y_pos,B_co.y_pos]
    temp_x =[robot_node.x_pos,R_co.x_pos,G_co.x_pos,B_co.x_pos]



    min_y = min(temp_y)
    max_y = max(temp_y)
    min_x = min(temp_x)
    max_x = max(temp_x)

    # print('---------Area Calculator---------')
    # print('---->Given Nodes: ')
    # print('--------->R: [{},{}]'.format(R_co.x_pos, R_co.y_pos))
    # print('--------->G: [{},{}]'.format(G_co.x_pos, G_co.y_pos))
    # print('--------->B: [{},{}]'.format(B_co.x_pos, B_co.y_pos))
    # print('---------------------------------')
    # print('X [{},{}], Y[{},{}]'.format(min_x,max_x,min_y,max_y))


    line_y = max_y-min_y
    line_x = max_x-min_x

    parameter = (line_y*2)+(line_x*2)

    return parameter

def find_RGB_connection():
    global red_node_container
    global green_node_container
    global blue_node_container
    global RGB_parameter
    for R in red_node_container:
        for G in green_node_container:
            for B in blue_node_container:
                parameter =parameter_calculator(R,G,B)
                if parameter < RGB_parameter:
                    RGB_parameter = parameter
                # print(parameter)

get_inputs()
# get_inputs_from_file('pubdata/pub10.in')
# print(matrix)
# color_node_print()
find_RGB_connection()
# print('Min Area was: ', RGB_parameter)
print(RGB_parameter)