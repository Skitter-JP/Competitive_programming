column_size = 0
row_size = 0
matrix = []
counted_areas = []
secure_areas = []

def limit_check(x,y,s):
    #print('y+s: ',y+s)
    #print('x+s:', x+s)
    if y+s >=row_size or x+s >=column_size:
        return 0
    else:
        return 1

def matrix_print():
    for i in range(len(matrix)):
        print(matrix[i])

def get_inputs():
    global matrix
    global column_size
    global row_size
    column_size, row_size = input().split()
    row_size = int(row_size)
    column_size = int(column_size)
    for i in range(column_size):
        row = list(map(int, input().split()))
        matrix.append(row)

def secure_cell_detect(pos):
    global matrix
    if matrix[pos[0]][pos[1]] == 1:
        return 1
    else:
        return 0

def block_scanner(pos):
    global matrix
    global secure_areas
    x = pos[0]
    y = pos[1]
    #print('Value at point: ' ,matrix[x][y])

    outter_counter = 1
    for i in range(1,row_size):
        if outter_counter > 3:
            #print("Counter passed 3")
            break
        if outter_counter == 3:
            #print("Counter is 3 storing i:", i)
            secure_areas.append(i)
        if limit_check(x, y, i) == 1:
            outter_counter+= L_scanner(x,y,i)
        else:
            #print("Limit exceed")
            break


def L_scanner(col,row,offset):
    global matrix
    count = 0
    # print('Node: ', row, col)
    for i in range(col,col+offset+1):
        # print("down position: ", i, row+offset, '->', matrix[i][row + offset])
        if secure_cell_detect([i,row+offset]) == 1:
            count+=1

    for i in range(row,row+offset):
        # print("right: ",col+offset, i, '->',matrix[col+offset][i])
        if secure_cell_detect([col+offset,i]) == 1:
            count+=1
    #print('Lscanner Returning: ', count)
    return count

def square_maker(xoffset,yoffset,size):
    inner_counter=0
    for i in range(size):
        for j in range(size):
            #print(matrix[i+xoffset][j+yoffset], end='')
            if secure_cell_detect([i+xoffset,j+yoffset]) == 1:
                inner_counter +=1
        #print()
    return inner_counter

def matrix_scanner():
    global matrix
    global column_size
    global row_size
    for i in range(column_size):
        #minus 1 because we dont have to scan the last element
        for j in range(row_size-1):
            #print(i,j)
            if secure_cell_detect([i,j]) == 1:
                block_scanner([i,j])


def output_generate():
    secure_areas.sort()
    counter =0
    temp = 0
    #print(secure_areas)
    for i in range(len(secure_areas)+1):
        if(i == len(secure_areas)):
            #print("at the end")
            counted_areas.append([temp,counter])
            break
        if(i == 0):
            counter =1
            temp = secure_areas[i]
        else:
            if(temp == secure_areas[i]):
                counter+=1
            else:
                counted_areas.append([temp,counter])
                temp = secure_areas[i]
                counter = 1

def output_print():
    for i in range(len(counted_areas)):
        print(counted_areas[i][0],counted_areas[i][1])




get_inputs()
matrix_scanner()
output_generate()
output_print()