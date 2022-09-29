row_size =0
column_size =0
matrix_pond = []
found_fish = []
counted_fish = []

# row_size = 18
# column_size = 8
#
# matrix_pond = [
#     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 2, 0, 0, 0, 2, 0],
#     [0, 2, 1, 1, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 1, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 2, 0, 0, 1, 0, 1, 0],
#     [0, 0, 2, 0, 0, 0, 2, 1, 1, 1, 2, 0, 0, 0, 1, 0, 1, 0],
#     [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 2, 0],
#     [0, 0, 2, 0, 1, 2, 1, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]



def get_inputs():
    global matrix_pond
    global row_size
    global column_size
    column_size, row_size = input().split()
    row_size = int(row_size)
    column_size = int(column_size)
    for i in range(column_size):
        row = list(map(int, input().split()))
        matrix_pond.append(row)


def direction_detector(position):
    hits = 0
    rvalue = 0
    row = position[0]
    column = position[1]
    #print("In Direction Detect: row->", row," coloumn->",column)
    if(matrix_pond[row-1][column] == 1):
        #Going up
        hits +=1
        rvalue = 0
    if(matrix_pond[row][column+1] == 1):
        #Going Right
        hits += 1
        rvalue = 1
    if(matrix_pond[row+1][column] == 1):
        #Going Down
        hits += 1
        rvalue = 2
    if(matrix_pond[row][column-1] == 1):
        #Going Left
        hits += 1
        rvalue = 3

    if (hits == 1):
        # We wont ever look for a fish going lefttwards or upwards
        if (rvalue == 3 or rvalue == 0):
            return -1
        else:
            return rvalue
    if (hits > 1):
        return -1

def body_head_detector(position):
    row = position[0]
    column = position[1]
    if(matrix_pond[row][column] == 2 ):
        #If there is 2 we have reach the tail
        return 2
    if(matrix_pond[row][column] == 1 ):
        #If there is a one we still looking at the body
        return 1
    else:
        #If there is something else maybe a zero, we have then found the end with no tail
        return 0

def parameter_check(position, direction):
    row = position[0]
    column = position[1]
    if(direction == 1):
        #We are going Rightwards so we will look up and down
        if(matrix_pond[row-1][column] == 0 and matrix_pond[row+1][column] == 0):
            return True
        else:
            return False
    if(direction == 2):
        # We are going downwards so we will look left and right
        if(matrix_pond[row][column-1] == 0 and matrix_pond[row][column+1] == 0):
            return True
        else:
            return False

def find_fish(head):
    row = head[0]
    column = head[1]
    #print(row,column)
    direction = direction_detector(head)
    #print("Direction:  ", direction)
    if direction == -1:
        #Skip this head it is either not valid or its a tail
        return
    #print("Head is Valid")
    if direction == 1:
        #print("Going Right")
        #The body is going Rightwards
        #Counter is set to one because the head has already been found
        counter = 1
        for i in range(column+1,row_size,1):

            if(parameter_check([row,i],direction)):
                #print('position : ', row, " ", i, ' Valid')
                #Position is good Now we check if its a body or tail
                if(body_head_detector([row,i]) == 1):
                    #We have a body part
                    #print('Body Part -> : ', row, " ", i, ' Valid')
                    counter +=1
                    #We move to the next iteration
                    continue
                if (body_head_detector([row,i]) == 2):
                    # We have a tail
                    #print('Tail -> : ', row, " ", i, ' Valid')
                    counter += 1
                    #We no longer need to keep looking so we break the for loop
                    #print("Breaking For loop.... no need to carry on")
                    break
                else:
                    #print("Head/Body check failed returning")
                    #No data needs to be stored so we return the function
                    return
            else:
                #print("Parameter Check failed. Returning")
                #Position is bad return function
                return
        #Store the Size of the fish
        #print("Storing Fish -> Counter: ", counter)
        found_fish.append(counter)
        return

    if direction == 2:
        #print("Going Down")
        #The body is going downwards
        counter = 1
        for i in range(row+1, column_size,1):
            if (parameter_check([i,column], direction)):
                #print('position : ', row, " ", i, ' Valid')
                # Position is good Now we check if its a body or tail
                if (body_head_detector([i,column]) == 1):
                    #print('Body Part -> : ', row, " ", i, ' Valid')
                    # We have a body part
                    counter += 1
                    # We move to the next iteration
                    continue
                if (body_head_detector([i,column]) == 2):
                    # We have a tail
                    #print('Tail -> : ', row, " ", i, ' Valid')
                    counter += 1
                    # We no longer need to keep looking so we break the for loop
                    #print("Breaking For loop.... no need to carry on")
                    break
                else:
                    #print("Head/Body check failed returning")
                    # No data needs to be stored so we return the function
                    return
            else:
                #print("Parameter Check failed. Returning")
                # Position is bad return function
                return
        # Store the Size of the fish
        #print("Storing Fish -> Counter: ", counter)
        found_fish.append(counter)
        return

def head_dector(position):
    row = position[0]
    column = position[1]
    if(matrix_pond[row][column] == 2 ):
        return True
    else:
        return False

def matrix_scanner():
    for i in range(1,column_size-1):
        for j in range(1, row_size-1):
            if(head_dector([i,j])):
                #print("Head Detected: ", [i,j])
                find_fish([i,j])

def output_generate():
    found_fish.sort()
    counter =0
    temp = 0
    #print(found_fish)
    for i in range(len(found_fish)+1):
        if(i == len(found_fish)):
            #print("at the end")
            counted_fish.append([temp,counter])
            break
        if(i == 0):
            counter =1
            temp = found_fish[i]
        else:
            if(temp == found_fish[i]):
                counter+=1
            else:
                counted_fish.append([temp,counter])
                temp = found_fish[i]
                counter = 1

def output_print():
    for i in range(len(counted_fish)):
        print(counted_fish[i][0],counted_fish[i][1])


get_inputs()
matrix_scanner()
output_generate()
output_print()