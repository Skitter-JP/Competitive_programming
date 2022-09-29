column_size = 0
row_size = 0
matrix_robots = []

robot_counter = 0
robots = []
degrees = []
output = []



class robot:
    def __init__(self, number=None):
        self.number = number
        self.vector = []
        self.counter = 0
        self.neighbour = []


def get_inputs():
    global matrix_robots, column_size,row_size
    column_size, row_size = input().split()
    row_size = int(row_size)
    column_size = int(column_size)
    for i in range(column_size):
        row = list(map(int, input().split()))
        matrix_robots.append(row)

def create_robot_node(position):
    global robot_counter
    temp = robot(robot_counter)
    robot_counter+=1
    temp.vector=position
    robots.append(temp)
    return robot_counter-1

def robot_detect(position):
    col = position[0]
    row = position[1]
    if matrix_robots[col][row] == 1:
        #We have found a robot
        return 1
    if matrix_robots[col][row] == 2:
        #We have found an obstical
        return 2
    else:
        #We have found nothing
        return 0

def robot_node_exisitance_check(postion):
    global robots
    for i in range(robot_counter):
        if robots[i].vector == postion:
            #print("Robots Exists")
            return i
    #print("Robot was not found")
    return -1

def next_robot_detect(position):
    right = []
    down = []
    col = position[0]
    row = position[1]
    #We will only scan rightwards and downwards
    #Going Right
    for i in range(row+1,row_size):
        #print('Col: ', col, 'i: ', i, 'row+1: ', row+1, 'row_size: ', row_size)
        if matrix_robots[col][i] == 2:
            #Boundry Dectected
            # invalid nothing found
            break
        if matrix_robots[col][i] == 1:
            #Robot Found
            right=[col,i]
            break
        if matrix_robots[col][i] == 0:
            #Nothing Found... Next
            continue
    # Going Down
    for i in range(col+1,column_size):
        if matrix_robots[i][row] == 2:
            #Boundry Dectected
            #invalid nothing found
            break
        if matrix_robots[i][row] == 1:
            #Robot Found
            down=[i,row]
            break
        if matrix_robots[i][row] == 0:
            #Nothing Found... Next
            continue
    return right, down

def node_linker(R1,R2):
    robots[R1].counter+=1
    robots[R1].neighbour.append(R2)
    robots[R2].counter+=1
    #robots[R2].neighbour.append(R1)

def matrix_scanner():

    #print(column_size)
    #print(row_size)
    for i in range(column_size):
        for j in range(row_size):
            #print("-------New Iteration---------", [i,j])
            if robot_detect([i,j]) == 1:

                #print("Robot Found -> ", [i,j])
                #print("Checking if Robot Node Exsits")
                mainRobotNumber = robot_node_exisitance_check([i,j])
                #print(mainRobotNumber)
                if mainRobotNumber > -1 :
                    #print("Robot Node Exists")
                    pass
                else:
                    #print("Robot Node Does not Exists")
                    #Here we will create a robot node
                    mainRobotNumber = create_robot_node([i,j])

                #Now we find robots that are connected to the above robot
                R,D = next_robot_detect([i,j])
                if R == []:
                    #No Robots to the right were found
                    #print("No Robots to the Right")
                    pass
                else:
                    #Robots to the right were found
                    #print("Robots to the Right Found: ", R)
                    #We should check if this robots node exsits
                    RightRobo = robot_node_exisitance_check(R)
                    if RightRobo > - 1:
                        #print("Rightward Robot found ... linking")
                        # Right Nieghbour nodes exsits... no need to create a new node
                        # Now we should link the nodes and increment the counters
                        node_linker(mainRobotNumber,RightRobo)
                    else:
                        #Node does not exsits -> we should create a new node
                        RightRobo = create_robot_node(R)
                        if  RightRobo > -1:
                            #print("Rightward Robot not found ... creating...Accessing: ", robots[RightRobo].vector)
                            #print("linking...")
                            #Node Created Sucessfully
                            #Now we should link the nodes and increment the counters
                            node_linker(mainRobotNumber, RightRobo)
                if D == []:
                    # No Robots downwardswere found
                    #print("No Robots downwards")
                    pass
                else:
                    # Robots to the right were found
                    #print("Robots to the Downward Found: ", D)
                    #We should check if this node exists
                    DownRobo = robot_node_exisitance_check(D)
                    if DownRobo > -1 :
                        #print("Downward Robot found ... linking")
                        #Down Nieghbour nodes exsits... no need to create a new node
                        # Now we should link the nodes and increment the counters
                        node_linker(mainRobotNumber, DownRobo)
                    else:
                        #Node does not exsits -> we should create a new node
                        DownRobo = create_robot_node(D)

                        if  DownRobo > -1:
                            #print("Downward Robot not found ... creating...Accessing: ", robots[DownRobo].vector)
                            #print("linking...")
                            #Node Created Sucessfully
                            #Now we should link the nodes and increment the counters
                            node_linker(mainRobotNumber, DownRobo)

def node_printer():
    for i in range(len(robots)):
        temp = robots[i]
        print("Robot: ",temp.number," Vector: ",temp.vector, "Degree: ",temp.counter, "Neighbours: ",temp.neighbour)

def get_degrees():
    global degrees
    degree_counter = 0
    for i in range(robot_counter):
        temp = robots[i]
        if temp.neighbour != []:

            degree_counter = degree_counter+temp.counter
            #print(i, "Connections Exsit: Number of connections is : ", len(temp.neighbour), 'Counter is : ', degree_counter)
            for j in range(len(temp.neighbour)):
                #print("--------In nested loop: ", temp.neighbour[j] )
                temp2 = robots[temp.neighbour[j]]
                degree_counter = degree_counter+temp2.counter
                degrees.append(degree_counter)
                #print("--------In nested loop: ", temp.neighbour[j], 'Counter is : ',degree_counter)
                degree_counter = degree_counter-temp2.counter
        degree_counter=0

def setup_output():
    global output
    for i in range(9):
        output.append([i,0])

def degree_print():
    degrees.sort()
    counter = 0
    temp = 0
    for i in range(len(degrees) + 1):
        if (i == len(degrees)):
            #print("at the end")
            output[temp][1]=counter
            break
        if (i == 0):
            counter = 1
            temp = degrees[i]
        else:
            if (temp == degrees[i]):
                counter += 1
            else:
                output[temp][1]=counter
                temp = degrees[i]
                counter = 1
    for i in range(2,len(output)):
        print(output[i][0], output[i][1])


get_inputs()
matrix_scanner()
# node_printer()
get_degrees()
setup_output()
degree_print()

