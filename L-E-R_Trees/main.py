R_counter = 0
L_counter = 0
E_counter = 0
Node_object_container = []
number_of_nodes = 0

class Node:

    def __init__(self,id,color):
        self.id = id
        self.color = color
        self.left = None
        self.right = None
        self.left_colors = [0,0]
        self.right_colors = [0,0]
        self.total_colors = [0,0]

    def LER_check(self):
        LER_checker(self.left_colors,self.right_colors)

    def add_final_color(self,color):
        if color == 0:
            self.total_colors[0] +=1
        elif color ==1:
            self.total_colors[1] += 1

    def copy_left(self,other):
        self.left_colors[0] = other.total_colors[0]
        self.left_colors[1] = other.total_colors[1]

    def copy_right(self,other):
        self.right_colors[0] = other.total_colors[0]
        self.right_colors[1] = other.total_colors[1]

    def node_print_colors(self):
        print('Node ID: ', self.id)
        print("------>Left Colors: ", self.left_colors)
        print("------>Right Colors: ",self.right_colors)
        print("------>Total Colors: ",self.total_colors)

    def combine_colors(self):
        self.total_colors[0] = self.left_colors[0]+self.right_colors[0]
        self.total_colors[1] = self.left_colors[1] + self.right_colors[1]

    def add_left_colors(self,l_w,l_b):

        temp_left_white = self.left_colors[0]
        temp_left_black = self.left_colors[1]

        temp_left_white = temp_left_white+l_w
        temp_left_black = temp_left_black + l_b

        self.left_colors = [temp_left_white,temp_left_black]


    def add_right_colors(self, r_w, r_b):

        temp_right_white = self.right_colors[0]
        temp_right_black = self.right_colors[1]

        temp_right_white = temp_right_white + r_w
        temp_right_black = temp_right_black + r_b

        self.right_colors = [temp_right_white, temp_right_black]

    def is_leaf(self):
        if(self.left == None and self.right == None):
            return True
        else:
            return False

    def is_parent(self):
        if(self.left != None and self.right!=None):
            return True
        else:
            return False

    def connect(self,node,dir):
        if(dir == 0):
            if(self.left == None):
                self.left = node

        if(dir == 1):
            if (self.right == None):
                self.right = node


def nodes_print():
    global Node_object_container
    for Node in Node_object_container:
        print()
        print('[ID:', Node.id, 'C: ', Node.color,']')
        print('------->Left: ',Node.left)
        print('------->Right: ', Node.right)
        print()

def get_inputs():
    global number_of_nodes
    global Node_object_container
    number_of_nodes = input()
    number_of_nodes = int(number_of_nodes)
    node_colors = input().split()
    for i in range(number_of_nodes):
        color = int(node_colors[i])
        Node_object_container.append(Node(i,color))

    for i in range(number_of_nodes-1):
        parent_node, child_node, direction = input().split()
        parent_node = int(parent_node)
        child_node = int(child_node)
        direction = int(direction)
        Node_object_container[parent_node].connect(child_node,direction)

def get_inputs_from_file(dir):
    file = open(dir, 'r')
    global number_of_nodes
    global Node_object_container
    line_number = 0
    for line in file:
        if line_number == 0:
            number_of_nodes = line
            number_of_nodes = int(number_of_nodes)
        elif line_number == 1:
            node_colors = line.split()

            for i in range(number_of_nodes):
                color = int(node_colors[i])
                Node_object_container.append(Node(i, color))

            # print(temp_weights)
            # print(Leaf_reference)
        else:
            parent_node, child_node, direction = line.split()
            parent_node = int(parent_node)
            child_node = int(child_node)
            direction = int(direction)
            Node_object_container[parent_node].connect(child_node, direction)

        line_number += 1
    file.close()

def LER_checker(left, right):
    global R_counter
    global L_counter
    global E_counter
    wx = left[0]
    wwx = right[0]
    bx = left[1]
    bbx = right[1]

    if bx == 0 or bbx == 0 or wwx == 0 or wx == 0:
        return

    con_a = wx / bx
    con_b = wwx / bbx

    if con_a > con_b:
        L_counter += 1
    elif con_a == con_b:
        E_counter += 1
    elif con_a < con_b:
        R_counter += 1

    return


def LER_print():
    global L_counter
    global E_counter
    global R_counter

    print('LER Values')
    print('L------>', L_counter)
    print('E------>', E_counter)
    print('R------>', R_counter)

def depth_search_itr(root):
    global Node_object_container
    current_node = root
    stack=[]
    stack.append([current_node,0])


    while 1:
        # print(stack)
        # print('Currnet Node:',current_node)
        # input()
        if Node_object_container[current_node].left != None and stack[-1][1]== 0:
            # print("in Left")

            stack.append([Node_object_container[current_node].left,0])
            current_node = Node_object_container[current_node].left

        elif Node_object_container[current_node].right != None and stack[-1][1]== 1:
            # print("in Right")

            stack.append([Node_object_container[current_node].right,0])
            current_node = Node_object_container[current_node].right


        elif Node_object_container[current_node].is_leaf():
            # print("Going Up 1")
            previous_node = current_node
            #We look at what color this node is.
            color = Node_object_container[previous_node].color
            stack.pop()
            current_node = stack[-1][0]
            #The temp counter tells us if we have gone left or gone right
            #if the temp counter is 0 we are at a left leaf
            #if the temp counter is 1 we are at a right leaf
            temp_counter = stack[-1][1]
            if temp_counter == 0:
                if color == 0:
                    Node_object_container[current_node].add_left_colors(1,0)
                elif color == 1:
                    Node_object_container[current_node].add_left_colors(0,1)

            elif temp_counter == 1:
                if color == 0:
                    Node_object_container[current_node].add_right_colors(1,0)
                elif color == 1:
                    Node_object_container[current_node].add_right_colors(0,1)
            # Node_object_container[current_node].node_print_colors()

            temp_counter +=1
            stack[-1][1] = temp_counter

        elif stack[-1][1] ==1 and Node_object_container[current_node].right == None:
            # print("Big Pop Without Right")
            #We went left and there was no right
            previous_node = current_node
            color = Node_object_container[previous_node].color
            stack.pop()
            if len(stack) != 0:
                current_node = stack[-1][0]
                temp_counter = stack[-1][1]
            else:
                break
            temp_counter += 1
            stack[-1][1] = temp_counter
            Node_object_container[previous_node].combine_colors()
            if color == 0:
                Node_object_container[previous_node].add_final_color(0)
            elif color == 1:
                Node_object_container[previous_node].add_final_color(1)

            if temp_counter == 1:
                Node_object_container[current_node].copy_left(Node_object_container[previous_node])

            elif temp_counter == 2:
                Node_object_container[current_node].copy_right(Node_object_container[previous_node])

            # Node_object_container[previous_node].node_print_colors()
            # Node_object_container[current_node].node_print_colors()

        elif stack[-1][1] ==0 and Node_object_container[current_node].left == None:
            #There was no left and we are not at a leaf. There for we must go right.

            # print("in Right")
            stack.append([Node_object_container[current_node].right, 0])
            current_node = Node_object_container[current_node].right
            stack.pop()
            current_node = stack[-1][0]
            temp_counter = stack[-1][1]
            temp_counter += 1
            stack[-1][1] = temp_counter

        elif stack[-1][1] ==2:
            # print("----Big Pop!----")
            previous_node = current_node
            stack.pop()
            Node_object_container[previous_node].LER_check()
            # LER_print()
            Node_object_container[previous_node].combine_colors()
            # Node_object_container[previous_node].node_print_colors()

            color = Node_object_container[previous_node].color
            if len(stack) != 0:
                #ok so
                current_node = stack[-1][0]
                temp_counter = stack[-1][1]
                temp_counter += 1
                stack[-1][1] = temp_counter

                if color == 0:
                    Node_object_container[previous_node].add_final_color(0)
                elif color == 1:
                    Node_object_container[previous_node].add_final_color(1)

                if temp_counter == 1:
                    Node_object_container[current_node].copy_left(Node_object_container[previous_node])

                elif temp_counter == 2:
                    Node_object_container[current_node].copy_right(Node_object_container[previous_node])

                # Node_object_container[previous_node].node_print_colors()
                # Node_object_container[current_node].node_print_colors()

            else:
                break



# get_inputs_from_file('./datapub/pub10.in')
get_inputs()
depth_search_itr(0)
# nodes_print()
# deep_search(0)
# print("L: {} E:{} R:{}".format(L_counter,E_counter,R_counter))
print(L_counter,E_counter,R_counter)
