# Robots = [6,10,3]
# visit_count = [2, 5, 4, 7, 1, 4, 3, 2, 8, 6, 2, 1, 6]
# number_of_commands = 3
# commands = [[[3,1,7],[1,0,5],[2,0,20]]]
# prefix_sum_array = []
# Len = 13
# time = 0
# Rad = 2

Robots = []
visit_count = []
number_of_commands = 0
commands = []
prefix_sum_array = []
Len = 0
time = 0
Rad = 0




def get_inputs():
    # Take in the intial data
    # Len = Size of Operating Space
    # Rad = Radius of Robots
    # Sec1,2,3 = Postition of Robots
    ##print("Enter Length, Radius, Robots Pos 1, Pos2, Pos3")
    global Rad
    Len, Rad, Sec1, Sec2, Sec3 =input().split()

    Robots.append(int(Sec1))
    Robots.append(int(Sec2))
    Robots.append(int(Sec3))
    ##print(Robots)

    Rad = int(Rad)
    #print("Radius: = ", Rad)

    #Get Visit Count
    #print("Weight of each element")
    inp=input().split()
    for i in inp:
        visit_count.append(int(i))
    #print(visit_count);

    #Get number commands to be expected
    #print("Enter number of commands the robots will get")
    number_of_commands = input()
    #print(number_of_commands);

    #
    #print("enter the commands")

    for i in range(int(number_of_commands)):
        commands.append([])
        commands[i].append(input().split())
    #print("Commands")
    #print(commands)

def generate_prefix_array(data_array):
    output_array = []
    for i in range(len(data_array)):
        if i == 0:
            output_array.append(data_array[0])
        else:
            output_array.append(output_array[i-1]+data_array[i])
    return output_array

def find_intersection(intervals, N):
    # First interval
    a = intervals[0][0]
    b = intervals[0][1]

    # Check rest of the intervals
    # and find the intersection
    for i in range(1, N):

        # If no intersection exists
        if (intervals[i][0] > b or intervals[i][1] < a):
            return(-1)

            # Else update the intersection
        else:
            a = max(a, intervals[i][0])
            b = min(b, intervals[i][1])
            return a, b

def weight_count(start,end,prefix_sum_array):
    move = None
    #if we are going left
    if start > end:
        temp = end
        end = start
        start = temp
    #if we started at zero no need to subtract
    if start == 0 :
        # #print("#print End Position Weight")
        move = prefix_sum_array[end]
    #if we start somewhere not at zero
    if start != 0:
        start -= 1
        # #print(prefix_sum_array[end])
        # #print(prefix_sum_array[start])
        move = prefix_sum_array[end] - prefix_sum_array[start]
    # #print(move)
    return move

def move_robot(Robot,direction,move_count):
    selected_robot_start_pos = Robots[Robot - 1]
    selected_robot_pos = Robots[Robot - 1]
    if(move_count != 0):
        move_count -= 1  # compensate for first position
    # #print(move_count)

    if direction == 0:
        # #print("In Left")
        #Go Left
        selected_robot_pos = selected_robot_pos - move_count
        if selected_robot_pos < 0:
            selected_robot_pos = 0
        # check if result is withing the bounds
    if direction == 1:
        # #print("In Right")
        # #print(selected_robot_pos)
        selected_robot_pos = selected_robot_pos + move_count
        if selected_robot_pos >= len(visit_count):
            selected_robot_pos = (len(visit_count)-1)
        # check if result is withing the bounds
        # #print(selected_robot_pos)

    #Update Robot

    Robots[Robot - 1] = selected_robot_pos
    #print("Robot ", Robot, " moved", "new position ", Robots[Robot - 1] )
    result_1 = None
    result_2 = None
    #print("StartPos", selected_robot_start_pos)
    #print("EndPos", selected_robot_pos)
    global time
    result_2 = weight_count(selected_robot_start_pos,selected_robot_pos,prefix_sum_array)
    time += result_2
    #print("Time without comp", result_2)
    global Rad
    #print("Radius in Move Robots: = ", Rad)
    result_1 = radius_detector(selected_robot_start_pos,selected_robot_pos,Robot,Rad)
    time += result_1
    #print("Time without comp", result_2)
    #print("Time with comp", result_1+ result_2)
    #print("#####################################")
    #print()
    #print()

def display_robot_pos(R,L):
    Pos = []
    for i in L:
        if R[0] == i or R[1] == i or R[2] == i:
            Pos.append("R")
        else:
            Pos.append("-")
    #print(visit_count)
    #print(Pos)

def get_radius_interval(robot_pos,radius):
    data = []
    data.append(robot_pos - radius)
    data.append(robot_pos + radius)
    return data

def merge_interval(interval1,interval2):
    merge = []
    if interval1[0] < interval2[0]:
        merge.append(interval1[0])
    else:
        merge.append(interval2[0])
    if interval1[1] > interval2[1]:
        merge.append(interval1[1])
    else:
        merge.append(interval2[1])
    return merge

def radius_detector(start,stop,robot,rad):
    if start > stop:
        temp = start
        start = stop
        stop = temp

    global time
    main_interval =[]
    main_interval.append(start)
    main_interval.append(stop)
    fixed_intervals = []
    R1 = 0
    R2 = 1
    R3 = 2

    if robot == 1:
        #print("Robot 1 Moved Detecting Radius")
        fixed_intervals.append(get_radius_interval(Robots[R2], rad))
        fixed_intervals.append(get_radius_interval(Robots[R3], rad))
    if robot == 2:
        #print("Robot 2 Moved Detecting Radius")
        fixed_intervals.append(get_radius_interval(Robots[R1], rad))
        fixed_intervals.append(get_radius_interval(Robots[R3], rad))
    if robot == 3:
        #print("Robot 3 Moved Detecting Radius")
        fixed_intervals.append(get_radius_interval(Robots[R1], rad))
        fixed_intervals.append(get_radius_interval(Robots[R2], rad))

    #print("Radius is: ", rad)
    #print("Main ", main_interval)
    #print("Fixed 1", fixed_intervals[0])
    #print("Fixed 2", fixed_intervals[1])

    intersection_1 = []
    intersection_2 = []
    intersection_3 = []


    intersection_1.append(main_interval)
    intersection_1.append(fixed_intervals[0])


    intersection_2.append(main_interval)
    intersection_2.append(fixed_intervals[1])

    intersection_3.append(find_intersection(intersection_1,len(intersection_1)))
    intersection_3.append(find_intersection(intersection_2,len(intersection_2)))

    # #print(find_intersection(intersection_1,len(intersection_1)))
    intersection_1 = find_intersection(intersection_1,len(intersection_1))
    # #print(find_intersection(intersection_2,len(intersection_2)))
    intersection_2 = find_intersection(intersection_2,len(intersection_2))

    #print(intersection_1)
    #print(intersection_2)

    if intersection_1 == -1 and intersection_2 == -1:
        #print("No Radius Intersections occurred")
        #print("Intersection 1")
        #print(intersection_1)
        #print("Intersection 2")
        #print(intersection_2)
        #print('No double times')
        return 0
    if intersection_1 == -1 and intersection_2 != -1:
        #print("Only one robot was met")
        #print(weight_count(intersection_2[0], intersection_2[1], prefix_sum_array))
        return weight_count(intersection_2[0], intersection_2[1], prefix_sum_array)
    if intersection_2 == -1 and intersection_3 != -1:
        #print("Only one robot was met")
        #print(weight_count(intersection_1[0], intersection_1[1], prefix_sum_array))
        return weight_count(intersection_1[0], intersection_1[1], prefix_sum_array)

    #print(intersection_3)
    if find_intersection(intersection_3,len(intersection_3)) != -1:
        double_merge = []
        #print("Merging both intersections")
        #print(merge_interval(intersection_3[0],intersection_3[1]))
        double_merge = merge_interval(intersection_3[0], intersection_3[1])
        #print('Double Time: =', weight_count(double_merge[0],double_merge[1],prefix_sum_array))
        return weight_count(double_merge[0],double_merge[1],prefix_sum_array)
    else:
        #print("Intersect cannot merge")
        #print("indvidual calculations")
        #print(weight_count(intersection_1[0],intersection_1[1],prefix_sum_array))
        #print(weight_count(intersection_2[0], intersection_2[1], prefix_sum_array))
        return weight_count(intersection_1[0],intersection_1[1],prefix_sum_array) + weight_count(intersection_2[0], intersection_2[1], prefix_sum_array)

get_inputs()
#print(Robots[0],Robots[1],Robots[2])
prefix_sum_array = generate_prefix_array(visit_count)
#print("Prefix Sum",prefix_sum_array)

display_robot_pos(Robots,range(len(visit_count)))

for i in range(len(commands)):
    a = int(commands[i][0][0])
    b = int(commands[i][0][1])
    c = int(commands[i][0][2])

    #print(a)
    #print(b)
    #print(c)
    move_robot(a,b,c)

display_robot_pos(Robots,range(len(visit_count)))

#print("Final Count")
print(time)
