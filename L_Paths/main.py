# matrix_size = 8
# number_of_matricies = 1
# main_matrix =[
#     [
#         [4, 5, 2, 3, 1, 2, 2, 2],
#         [2, 2, 2, 3, 1, 1, 1, 1],
#         [4, 3, 3, 3, 3, 3, 3, 3],
#         [7, 7, 7, 7, 6, 5, 5, 5],
#         [1, 1, 1, 7, 6, 6, 6, 6],
#         [8, 8, 1, 7, 5, 5, 5, 5],
#         [3, 8, 1, 7, 5, 1, 1, 1],
#         [3, 3, 1, 7, 5, 1, 1, 1]
#     ]
# ]


# matrix_size = 5
# number_of_matricies = 3
# main_matrix =[
#     [
#         [1, 8, 1, 8, 1],
#         [8, 8, 1, 8, 1],
#         [1, 1, 1, 8, 1],
#         [8, 8, 8, 8, 1],
#         [1, 1, 1, 1, 1]
#      ],
#     [
#         [4, 4, 4, 4, 4],
#         [5, 5, 5, 5, 4],
#         [5, 5, 5, 5, 4],
#         [1, 1, 5, 5, 4],
#         [5, 1, 5, 5, 4]
#     ],
#     [
#         [7, 7, 7, 2, 7],
#         [7, 7, 7, 2, 2],
#         [2, 2, 2, 7, 7],
#         [7, 7, 2, 7, 7],
#         [7, 7, 2, 7, 7]
#     ]
# ]

matrix_size = 0
number_of_matricies = 0
main_matrix =[]


found_L_tails = []

def exisitance_check(vector):
    global found_L_tails
    for i in range(len(found_L_tails)):
        if vector[0] == found_L_tails[i][0] and vector[1] == found_L_tails[i][1]:
            #print("Node Exists")
            return 1

    #print("Node Does Not Exist")
    return 0

def edge_checker(column,row):
    global matrix_size
    #if we detect that the given position is on the edge of the matrix we will return 1 if not on the edge we return -1
    if row == 0 or column == 0 or row == matrix_size-1 or column == matrix_size-1:
        return 1
    else:
        return 0

def edge_direction(column,row):
    global matrix_size
    #This function should only be called if edge_checker has return 1

    #Top Edge -> return 0
    if column == 0 and row != 0 and row != matrix_size-1:
        return 0
    #Bottom Edge -> return 1
    if column == matrix_size-1 and row != 0 and row != matrix_size-1:
        return 1
    #Left Edge -> return 2
    if column != 0 and column !=matrix_size-1 and row ==0:
        return 2
    #Right Edge -> return 3
    if column != 0 and column !=matrix_size-1 and row ==matrix_size-1:
        return 3
    #Top Left Corner  -> return 4
    if column == 0 and row == 0:
        return 4
    #Top Right Corner -> return 5
    if column == 0 and row == matrix_size-1:
        return 5
    #Bottom Left Corner -> return 6
    if column == matrix_size-1 and row == 0:
        return 6
    #Bottom Right Corner -> return 7
    if column == matrix_size-1 and row == matrix_size-1:
        return 7

def same_value(sub_matrix,look_vector,reference_vector):
    #Here we see if the values of the vectors are the same.
    if sub_matrix[look_vector[0]][look_vector[1]] == sub_matrix[reference_vector[0]][reference_vector[1]]:
        return 1
    else:
        return 0

def ignore(point1,point2):
    #this looks if point1 and point2 are pointing to the same place... checks if there pointers are the same.
    if point1[0] == point2[0] and point1[1] == point2[1]:
        return 1
    else:
        return 0

def kernal(sub_matrix,lookvector,previous_vector,restrction):
    #Here we look around if restrction is -1 then we look everywhere excep the previous vector.
    value = sub_matrix[lookvector[0]][lookvector[1]]
    counter = 0
    direction = 0
    #print("Restriction: ", restrction)
    if restrction == -1:
        #This means we are somewhere in the matrix.... no borders
        #Look Everywhere but previous_vector
        #look Up
        up = [lookvector[0]-1,lookvector[1]]
        down = [lookvector[0] + 1, lookvector[1]]
        left = [lookvector[0], lookvector[1] - 1]
        right = [lookvector[0], lookvector[1] + 1]
        if not ignore(up,previous_vector):
            if same_value(sub_matrix,up,previous_vector):
                direction = up
                counter+=1
        #look down
        if not ignore(down, previous_vector):
            if same_value(sub_matrix,down,previous_vector):
                direction = down
                counter += 1
        #look left
        if not ignore(left, previous_vector):
            if same_value(sub_matrix,left,previous_vector):
                direction = left
                counter += 1
        #look right
        if not ignore(right, previous_vector):
            if same_value(sub_matrix,right,previous_vector):
                direction = right
                counter += 1

    if restrction == 0:
        #Dont Look up
        down = [lookvector[0] + 1, lookvector[1]]
        left = [lookvector[0], lookvector[1] - 1]
        right = [lookvector[0], lookvector[1] + 1]
        if not ignore(down,previous_vector):
            if same_value(sub_matrix,down,previous_vector):
                direction = down
                counter += 1
        if not ignore(left, previous_vector):
            if same_value(sub_matrix,left,previous_vector):
                direction = left
                counter += 1
        if not ignore(right, previous_vector):
            if same_value(sub_matrix,right,previous_vector):
                direction = right
                counter += 1

    if restrction == 1:
        #Dont look down
        up = [lookvector[0]-1,lookvector[1]]
        left = [lookvector[0], lookvector[1] - 1]
        right = [lookvector[0], lookvector[1] + 1]

        if not ignore(up,previous_vector):
            if same_value(sub_matrix,up,previous_vector):
                direction = up
                counter += 1
        if not ignore(left, previous_vector):
            if same_value(sub_matrix,left,previous_vector):
                direction = left
                counter += 1
        if not ignore(right, previous_vector):
            if same_value(sub_matrix,right,previous_vector):
                direction = right
                counter += 1

    if restrction == 2:
        #dont look left
        up = [lookvector[0]-1,lookvector[1]]
        right = [lookvector[0], lookvector[1] + 1]
        down = [lookvector[0] + 1, lookvector[1]]

        if not ignore(up,previous_vector):
            if same_value(sub_matrix,up,previous_vector):
                direction = up
                counter += 1
        if not ignore(right, previous_vector):
            if same_value(sub_matrix,right,previous_vector):
                direction = right
                counter += 1
        if not ignore(down, previous_vector):
            if same_value(sub_matrix,down,previous_vector):
                direction = down
                counter += 1

    if restrction == 3:
        #dont look Right
        up = [lookvector[0] - 1, lookvector[1]]
        down = [lookvector[0] + 1, lookvector[1]]
        left = [lookvector[0], lookvector[1] - 1]

        if not ignore(up,previous_vector):
            if same_value(sub_matrix,up,previous_vector):
                direction = up
                counter += 1
        if not ignore(down, previous_vector):
            if same_value(sub_matrix,down,previous_vector):
                direction = down
                counter += 1
        if not ignore(left, previous_vector):
            if same_value(sub_matrix,left,previous_vector):
                direction = left
                counter += 1

    if restrction == 4:
        #dont look up and dont look left
        right = [lookvector[0], lookvector[1] + 1]
        down = [lookvector[0] + 1, lookvector[1]]

        if not ignore(right,previous_vector):
            if same_value(sub_matrix,right,previous_vector):
                direction = right
                counter += 1
        if not ignore(down, previous_vector):
            if same_value(sub_matrix,down,previous_vector):
                direction = down
                counter += 1

    if restrction == 5:
        #dont look up and dont look right
        left = [lookvector[0], lookvector[1] - 1]
        down = [lookvector[0] + 1, lookvector[1]]

        if not ignore(left,previous_vector):
            if same_value(sub_matrix,left,previous_vector):
                direction = left
                counter += 1
        if not ignore(down, previous_vector):
            if same_value(sub_matrix,down,previous_vector):
                direction = down
                counter += 1

    if restrction == 6:
        #dont look down and dont look left
        up = [lookvector[0]-1,lookvector[1]]
        right = [lookvector[0], lookvector[1] + 1]

        if not ignore(up,previous_vector):
            if same_value(sub_matrix,up,previous_vector):
                direction = up
                counter += 1
        if not ignore(right, previous_vector):
            if same_value(sub_matrix,right,previous_vector):
                direction = right
                counter += 1

    if restrction == 7:
        #dont look down and dont look right
        up = [lookvector[0] - 1, lookvector[1]]
        left = [lookvector[0], lookvector[1] - 1]

        if not ignore(up,previous_vector):
            if same_value(sub_matrix,up,previous_vector):
                direction = up
                counter += 1
        if not ignore(left, previous_vector):
            if same_value(sub_matrix,left,previous_vector):
                direction = left
                counter += 1
    if counter == 0:
        return [-2,-2]

    if counter != 1:
        return [-1,-1]
    else:
        return direction

def moving_parameter_check(sub_matrix,look_vector,previous_vector):

    if edge_checker(look_vector[0],look_vector[1]):
        #We are on the edge, we will not find where on the edge we are
        restrict = edge_direction(look_vector[0],look_vector[1])
    else:
        #We are somewhere on the inside of the matrix
        restrict = -1
    next_node = kernal(sub_matrix,look_vector,previous_vector,restrict)

    return next_node

def parameter_check(sub_matrix,column,row,direction):
    global matrix_size
    value = sub_matrix[column][row]
    counter = 0
    found_direction = 0
    #direction parameter will tell us where not to scan 0 => Top.... 1 => Right .... 2 => Bottom
    #the parameters will be for the point we need to check
    #this function should also return the dirrection if it is valid

    if direction == 0:
        #We need to check if we are at the extremes of the submatrix
        if row == 0:
            #we wont look left
            #Looking Right
            #print(sub_matrix[column][row + 1])
            if sub_matrix[column][row + 1] == value:
                counter += 1
                found_direction = [column,row + 1]
            #Looking Down
            #print(sub_matrix[column + 1][row])
            if sub_matrix[column + 1][row] == value:
                counter += 1
                found_direction = [column + 1,row]

        elif row == matrix_size-1:
            #we wont look right
            #Looking Left
            #print(sub_matrix[column][row - 1])
            if sub_matrix[column][row - 1] == value:
                counter += 1
                found_direction = [column,row - 1]
            #Looking Down
            #print(sub_matrix[column + 1][row])
            if sub_matrix[column + 1][row] == value:
                counter += 1
                found_direction = [column + 1,row]
        else:
            #we were not at the extreme so we look normally
            #Looking Left
            #print(sub_matrix[column][row-1])
            if sub_matrix[column][row-1] == value:
                return [-1,-1]
            #Look Right
            #print(sub_matrix[column][row+1])
            if sub_matrix[column][row+1] == value:
                return [-1,-1]
            #Looking Down
            #print(sub_matrix[column+1][row])
            if sub_matrix[column+1][row] == value:
                return [column+1,row]

    if direction == 1:
        #Looking Up
        #print(sub_matrix[column-1][row])
        if sub_matrix[column-1][row] == value:
            return [-1,-1]
        # Looking Down
        #print(sub_matrix[column + 1][row])
        if sub_matrix[column + 1][row] == value:
            return [-1,-1]
        #Looking Right
        #print(sub_matrix[column][row+1])
        if sub_matrix[column][row+1] == value:
            return [column,row+1]



    if direction == 2:
        if row == 0:
            #we wont look left
            #Looking Right
            #print(sub_matrix[column][row+1])
            if sub_matrix[column][row+1] == value:
                counter += 1
                found_direction = [column,row+1]
            #Looking Up
            #print(sub_matrix[column-1][row])
            if sub_matrix[column-1][row] == value:
                counter += 1
                found_direction = [column-1,row]

        elif row == matrix_size-1:
            #we wont look right
            #Looking Left
            #print(sub_matrix[column][row-1])
            if sub_matrix[column][row-1] == value:
                counter += 1
                found_direction = [column,row-1]
            #Looking Up
            #print(sub_matrix[column-1][row])
            if sub_matrix[column-1][row] == value:
                counter += 1
                found_direction = [column-1,row]
        else:
            #we look normally
            #Looking Left
            #print(sub_matrix[column][row-1])
            if sub_matrix[column][row-1] == value:
                return [-1,-1]
            #Looking Right
            #print(sub_matrix[column][row+1])
            if sub_matrix[column][row+1] == value:
                return [-1,-1]
            #Looking Up
            #print(sub_matrix[column-1][row])
            if sub_matrix[column-1][row] == value:
                return [column-1,row]
    if counter != 1:
        return [-1,-1]
    else:
        return found_direction

def bend_checker(vectorA,vectorB):
    if vectorA[1] == vectorB[1] and vectorA[0] != vectorB[0]:
        return 0
    elif vectorA[1] != vectorB[1] and vectorA[0] == vectorB[0]:
        return 0
    else:
        return 1

def three_way_scanner(sub_matrix):
    global matrix_size
    global found_L
    final_values = 0
    #The parameters will define which matrix we are working on since the main matrix will have sub matricies within them

    #Scan Topside
    #print("Starting Top Scan")
    for i in range(len(sub_matrix)):
        VectorA = [0,i]
        VectorB = parameter_check(sub_matrix,0,i,0)
        #print('Element Number: ', sub_matrix[0][i],'Vector: ', VectorB)
        #print('---------------------------------------')
        VectorC = []
        if VectorB[0] != -1:
            #We have already found two elements
            counter = 2
            turns = 0
            #print("Neighbour found ! ... start looking....")

            #We found a valid place
            while True:
                if turns > 1:
                    break;
                #print("Previous Vector: ", VectorA)
                #print("Looking Vector: ", VectorB)
                VectorC = moving_parameter_check(sub_matrix, VectorB, VectorA)
                #print('Found Vector: ', VectorC)
                if VectorC[0] == -1:
                    break
                if VectorC[0] == -2:
                    #print("End Found")
                    if edge_checker(VectorB[0],VectorB[1]) and turns == 1:
                        found_L_tails.append(VectorB) #This should be the end of an L
                        L_value = sub_matrix[VectorB[0]][VectorB[1]]
                        total_value = L_value*counter
                        #print("We have reached the end with some many counts: ", counter, 'NumberValue Was: ', L_value ,'Total is : ', total_value )
                        final_values += total_value
                        #print("Saving...")
                        break
                    else:
                        #print("We did not reach the end so it was invalid... breaking")
                        break
                if bend_checker(VectorA,VectorC):
                    turns+=1
                    #print("Bend Detected ... Bends: ", turns)

                counter+=1
                VectorA = VectorB
                VectorB = VectorC
            #print('Counter: ', counter)
    #print("Starting Bottom Scan")
    for i in range(len(sub_matrix)):
        VectorA = [matrix_size-1, i]
        if exisitance_check(VectorA):
            continue
        VectorB = parameter_check(sub_matrix, matrix_size-1, i, 2)
        #print('Element Number: ', sub_matrix[matrix_size-1][i], 'Vector: ', VectorB)
        #print('---------------------------------------')
        VectorC = []
        if VectorB[0] != -1:

            # We have already found two elements
            counter = 2
            turns = 0
            #print("Neighbour found ! ... start looking....")

            # We found a valid place
            while True:
                if turns > 1:
                    break;
                #print("Previous Vector: ", VectorA)
                #print("Looking Vector: ", VectorB)
                VectorC = moving_parameter_check(sub_matrix, VectorB, VectorA)
                #print('Found Vector: ', VectorC)
                if VectorC[0] == -1:
                    break
                if VectorC[0] == -2:
                    #print("End Found")
                    if edge_checker(VectorB[0], VectorB[1]) and turns == 1:
                        L_value = sub_matrix[VectorB[0]][VectorB[1]]
                        total_value = L_value * counter
                        #print("We have reached the end with some many counts: ", counter, 'NumberValue Was: ', L_value, 'Total is : ', total_value)
                        #print("Saving...")
                        final_values += total_value
                        break
                    else:
                        #print("We did not reach the end so it was invalid... breaking")
                        break
                if bend_checker(VectorA, VectorC):
                    turns += 1
                    #print("Bend Detected ... Bends: ", turns)

                counter += 1
                VectorA = VectorB
                VectorB = VectorC
            #print('Counter: ', counter)
    return final_values




def matrix_iterator():
    global number_of_matricies
    global main_matrix
    for i in range(number_of_matricies):
        print(three_way_scanner(main_matrix[i]))




def matrix_print():
    global main_matrix
    global matrix_size
    global number_of_matricies
    for i in range(number_of_matricies):
        print('---------------')
        for j in range(len(main_matrix[i])):
            print(main_matrix[i][j])
        print('---------------')

def get_inputs():
    global main_matrix
    global matrix_size
    global number_of_matricies
    matrix_size, number_of_matricies = input().split()
    matrix_size = int(matrix_size)
    number_of_matricies = int(number_of_matricies)

    for i in range(number_of_matricies):
        sub_matrix = []
        for j in range(matrix_size):
            temp = list(map(int, input().split()))
            sub_matrix.append(temp)
        main_matrix.append(sub_matrix)



get_inputs()
matrix_iterator()
# matrix_print()
# print(main_matrix)


