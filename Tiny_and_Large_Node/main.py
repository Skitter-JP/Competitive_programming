number_of_nodes = 0
number_of_edges = 0
node_container = []

node_grades = []

tiny_node = []
large_node = []

class Node():
    def __init__(self,id):
        self.id = id
        self.degree = 0
        self.grade =0
        self.visited = False
        self.distance = 0
        self.distance_from_root = 0
        self.connections = []

    def add_connection(self,node):
        self.connections.append(node)
        self.degree+=1

def node_print():
    global node_container

    for i in node_container:
        print('---------------------------')
        print("Node ID: ",i.id)
        print("Degree:",i.degree)
        print("Grade:", i.grade)
        print("Connections")
        # for j in range(len(i.connections)):
        #     print('----->',i.connections[j])
        for j in i.connections:
            print('----->',j)
        print('---------------------------')

def get_grades():
    global node_container
    global min_grade
    global max_grade
    global potential_large_nodes
    global potential_tiny_nodes
    global tiny_node
    global large_node

    for node in node_container:
        temp_grade = 0
        for n in node.connections:
            temp_grade = temp_grade + node_container[n].degree
        node.grade = temp_grade
        temp = [node.grade,node.id]
        node_grades.append(temp)

    tiny_node = min(node_grades)
    large_node = max(node_grades)


def BFS(root,target):
    global node_container
    global number_of_nodes

    q = []

    current_node = root
    current_node_obj = node_container[current_node]
    current_node_obj.visited = True
    current_node_obj.distance_from_root = 0
    q.extend(current_node_obj.connections)



    for i in q:
        i_node_obj = node_container[i]
        if i != current_node:
            i_node_obj.visited = True
            i_node_obj.distance_from_root = 1

            if i_node_obj.id == target:
                return i_node_obj.distance_from_root

    while (q):

        current_node = q.pop(0)
        current_node_obj = node_container[current_node]

        for i in current_node_obj.connections:
            i_node_obj = node_container[i]
            if i_node_obj.visited == False:
                q.append(i)
                i_node_obj.distance_from_root = current_node_obj.distance_from_root + 1
                i_node_obj.visited = True
                if i_node_obj.id == target:
                    return i_node_obj.distance_from_root







def get_inputs():
    global node_container
    global number_of_nodes
    global number_of_edges

    number_of_nodes,number_of_edges = input().split()
    number_of_nodes = int(number_of_nodes)
    number_of_edges = int(number_of_edges)

    for i in range(number_of_nodes):
        temp_node = Node(i)
        node_container.append(temp_node)

    for i in range(number_of_edges):
        node1,node2 = input().split()
        node1 = int(node1)
        node2 = int(node2)
        node_container[node1].add_connection(node2)
        node_container[node2].add_connection(node1)




get_inputs()
get_grades()
# node_print()
print(tiny_node[1], large_node[1],BFS(tiny_node[1],large_node[1]))

