import copy
import time
column_size = 0
row_size = 0


horizontal_wing_container = []

number_of_horizontal_wings = 0

vertical_wing_container_sorted = []
vertical_wing_container = []
number_of_vertical_wings = 0

temp_wing_container = []

max_h_size = 0

matrix = []
V_ref_matrix = []
H_ref_matrix = []

# #OG Martix pubdata 1
# matrix = [
# # 0    1    2    3    4    5    6    7    8
# ['.', '.', '.', '.', '.', '.', 'o', 'o', '.'], #0
# ['.', 'X', '.', 'X', '.', '.', 'X', '.', 'o'], #1
# ['.', '.', 'o', '.', '.', 'o', '.', '.', '.'], #2
# ['.', '.', 'X', '.', '.', '.', '.', '.', 'o'], #3
# ['.', 'o', '.', '.', 'o', 'X', '.', '.', '.'], #4
# ['o', 'o', 'o', '.', '.', '.', 'o', '.', 'o'], #5
# ]
# column_size = 9
# row_size = 6



class vertical_wing_node:
    def __init__(self, number=None):
        self.wing_number = number
        self.start_pos =0
        self.end_pos =0
        self.size =0
        self.column =0
        self.harzard =0
        self.harzard_pos =0

class horizontal_wing_node:
    def __init__(self, number=None):
        self.wing_number = number
        self.start_pos =0
        self.end_pos =0
        self.size =0
        self.row =0
        self.harzard =0
        self.harzard_pos =0


def place_ref_v_node(ID, COL, SP, SIZE):
    global V_ref_matrix
    for i in range(SIZE):
        if V_ref_matrix[i+SP][COL] != -1:
            continue
        else:
            V_ref_matrix[i+SP][COL] = ID

def place_ref_h_node(ID, ROW, SP, SIZE):
    global H_ref_matrix
    for i in range(SIZE):
        if H_ref_matrix[ROW][i+SP] != -1:
            continue
        else:
            H_ref_matrix[ROW][i + SP] = ID

def find_vertical_wing():
    #iterating through the columns
    for column_itr in range(column_size):
        #we are in a new column therefor we have a new wing... all values are now zero...
        wing_start=0
        wing_end=0
        haz_counter = 0
        haz_pos = 0

        #print("-----------")
        #Now we will iterate through the rows....
        for row_itr in range(row_size):
            #print("Colum:", column_itr, "-- Row: ", row_itr)
            #print(matrix[row_itr][column_itr], end='')

            #if we find a spot that is good
            if matrix[row_itr][column_itr] == '.':
                #we extend the wing
                wing_end+=1
                #print("->point found counter ... -> ", wing_end)
                #no longer need to look at the rest... so we pass to the next iteration...
                pass
            #if we find a spot that is bad...
            if matrix[row_itr][column_itr] == 'X':
                #print("->X found",end='')
                #we now check of big the size of the wing is...
                #wing_size_temp = wing_size_calculator(wing_start,wing_end)
                #if the wing size is greater than 2 we will save this wing...

                if valid_vertical_wing_size_check(wing_start, wing_end):
                    #print("... wing size is valid... size: ", wing_end-wing_start)

                    create_vertical_wing_node(wing_start,wing_end-1,wing_end-wing_start,column_itr,haz_counter,haz_pos)
                #we now reset all the counters...

                wing_start = row_itr+1
                wing_end = row_itr+1
                haz_counter = 0
                haz_pos = 0
                #print("... New wing starting at: ", wing_start)
                pass
            #if we find a suspicous spot...
            if matrix[row_itr][column_itr] == 'o':

                if haz_counter == 0:
                    #this is the first hazard we have found...
                    haz_counter += 1
                    wing_end += 1
                    haz_pos = row_itr
                    #print("->o found ... haz counter valid ... counter ... -> ", wing_end)
                else:
                    #this is not the first hazard we have found...
                    if valid_vertical_wing_size_check(wing_start, wing_end):
                        #wing size is big enough...storing the wing...
                        create_vertical_wing_node(wing_start, wing_end-1, wing_end - wing_start, column_itr, haz_counter, haz_pos)
                    #the wing will now start one elemnt after the previous hazard
                    wing_start = haz_pos+1

                    #I dont think wing_end should be reset...
                    #wing_end = 0
                    #We instead increment it since we are now counting this new hazard...
                    wing_end += 1
                    #hazounter will be set to 1 since the start of this wing is a hazard...
                    haz_counter = 1
                    #the hazard will also be the start of this wing...
                    haz_pos = row_itr
                pass


        #end of the column for loop...
        #in what case would we still need to store information ?
        #if we get to the end and we only had one hazard... that is when we need to save it...
        #print()
        if valid_vertical_wing_size_check(wing_start, wing_end) and haz_counter <=1:
            #print("at end.... adding wing")
            create_vertical_wing_node(wing_start, wing_end-1, wing_end - wing_start, column_itr, haz_counter, haz_pos)
            # if haz_counter == 1:

def find_horizontal_wing():
    # Side to Side wings.....
    #iterating through the rows  except for the first and last rows...
    for row_itr in range(1,row_size-1):

        #we are in a new row therefor we have a new wing...
        #wings start at 1 since 0 is resevered for the vertical wings...
        wing_start=1
        wing_end=1
        haz_counter = 0
        haz_pos = 0

        #print("-----------")
        #Now we will iterate through the columns.... except for the first and last columns...
        for column_itr in range(1,column_size-1):

            #print("Colum:", column_itr, "-- Row: ", row_itr)
            #print(matrix[row_itr][column_itr], end='')

            #if we find a spot that is good
            if matrix[row_itr][column_itr] == '.':
                #we extend the wing
                wing_end+=1
                #print("->point found counter ... -> ", wing_end)
                #no longer need to look at the rest... so we pass to the next iteration...
                pass
            #if we find a spot that is bad...
            if matrix[row_itr][column_itr] == 'X':
                #print("->X found",end='')
                #we now check of big the size of the wing is...
                #if the wing size is greater than 0 we will save this wing...

                if valid_horizontal_wing_size_check(wing_start, wing_end):
                    #print("... wing size is valid... size: ", wing_end-wing_start)

                    create_horizontal_wing_node(wing_start,wing_end-1,wing_end-wing_start,row_itr,haz_counter,haz_pos)
                #we now reset all the counters...

                wing_start = column_itr+1
                wing_end = column_itr+1
                haz_counter = 0
                haz_pos = 0
                #print("... New wing starting at: ", wing_start)
                pass
            #if we find a suspicous spot...
            if matrix[row_itr][column_itr] == 'o':

                if haz_counter == 0:
                    #this is the first hazard we have found...
                    haz_counter += 1
                    wing_end += 1
                    haz_pos = column_itr
                    #print("->o found ... haz counter valid ... counter ... -> ", wing_end)
                else:
                    #this is not the first hazard we have found...
                    if valid_horizontal_wing_size_check(wing_start, wing_end):
                        #wing size is big enough...storing the wing...
                        create_horizontal_wing_node(wing_start, wing_end-1, wing_end - wing_start, row_itr, haz_counter, haz_pos)
                    #the wing will now start one elemnt after the previous hazard
                    wing_start = haz_pos+1

                    #I dont think wing_end should be reset...
                    #wing_end = 0
                    #We instead increment it since we are now counting this new hazard...
                    wing_end += 1
                    #hazounter will be set to 1 since the start of this wing is a hazard...
                    haz_counter = 1
                    #the hazard will also be the start of this wing...
                    haz_pos = column_itr
                pass


        #end of the column for loop...
        #in what case would we still need to store information ?
        #if we get to the end and we only had one hazard... that is when we need to save it...
        #print()
        if valid_horizontal_wing_size_check(wing_start, wing_end) and haz_counter <=1:
            #print("at end.... adding wing")
            create_horizontal_wing_node(wing_start, wing_end-1, wing_end - wing_start, row_itr, haz_counter, haz_pos)
            # if haz_counter == 1:

def create_vertical_wing_node(SP,EP,SIZE,COL,HAZ,HAZ_POS):
    global vertical_wing_container
    global number_of_vertical_wings
    temp = vertical_wing_node(number_of_vertical_wings)
    temp.start_pos = SP
    temp.end_pos = EP
    temp.size = SIZE
    temp.column = COL
    temp.harzard = HAZ
    temp.harzard_pos = HAZ_POS
    vertical_wing_container.append(temp)
    place_ref_v_node(number_of_vertical_wings, COL, SP, SIZE)
    number_of_vertical_wings+=1

def create_horizontal_wing_node(SP,EP,SIZE,ROW,HAZ,HAZ_POS):
    global horizontal_wing_container
    global number_of_horizontal_wings
    temp = horizontal_wing_node(number_of_horizontal_wings)
    temp.start_pos = SP
    temp.end_pos = EP
    temp.size = SIZE
    temp.row = ROW
    temp.harzard = HAZ
    temp.harzard_pos = HAZ_POS
    place_ref_h_node(number_of_horizontal_wings, ROW, SP, SIZE)
    horizontal_wing_container.append(temp)

    number_of_horizontal_wings+=1

def wing_size_calculator(start,end):
    return end-start

def valid_vertical_wing_size_check(start,end):
    if end-start > 2:
        return True
    else:
        return False

def print_vertical_wings():
    global vertical_wing_container
    global number_of_vertical_wings
    print("----------Printing Vertical Wings--------------")
    for i in range(number_of_vertical_wings):
        print("----------START--------------")
        print("Col: ", vertical_wing_container[i].column)
        print("Number:",vertical_wing_container[i].wing_number)
        print("Start: ",vertical_wing_container[i].start_pos)
        print("End: ",vertical_wing_container[i].end_pos)
        print("Size: ",vertical_wing_container[i].size)
        print("Haz: ",vertical_wing_container[i].harzard)
        print("Haz_pos: ",vertical_wing_container[i].harzard_pos)
        print("----------END--------------")
    print("----------End of Vertical Wings--------------")

def wing_size_calculator(start,end):
    return end-start

def valid_horizontal_wing_size_check(start,end):
    #possibly needs to be greater than 2... we will see later...
    if end-start > 1:
        return True
    else:
        return False

def print_horizontal_wings():
    global horizontal_wing_container
    global number_of_horizontal_wings
    print("----------Printing Horizontal Wings--------------")
    for i in range(number_of_horizontal_wings):
        print("----------START--------------")
        print("Col: ", horizontal_wing_container[i].row)
        print("Number:",horizontal_wing_container[i].wing_number)
        print("Start: ",horizontal_wing_container[i].start_pos)
        print("End: ",horizontal_wing_container[i].end_pos)
        print("Size: ",horizontal_wing_container[i].size)
        print("Haz: ",horizontal_wing_container[i].harzard)
        print("Haz_pos: ",horizontal_wing_container[i].harzard_pos)
        print("----------END--------------")
    print("----------END of Horizontal Wings--------------")

def vertical_wing_distance(v_wing_1,v_wing_2):
    global vertical_wing_container
    distance = vertical_wing_container[v_wing_2].column - vertical_wing_container[v_wing_1].column
    #print('V1: ', v_wing_1,'and V2: ', v_wing_2, ' - > Distance is: ', distance)
    return distance-1

def on_edge(V_wing_pos, H_wing_pos):
    global vertical_wing_container
    global number_of_vertical_wings

    global horizontal_wing_container
    global number_of_horizontal_wings

    V_start = vertical_wing_container[V_wing_pos].start_pos
    V_end = vertical_wing_container[V_wing_pos].end_pos

    H_row = horizontal_wing_container[H_wing_pos].row

    if V_start == H_row or V_end == H_row:
        #print('H wing is on the edge of the V wing !')
        return False
    else:
        return True

def wing_connector_with_ref_old():
    global vertical_wing_container
    global number_of_vertical_wings

    global horizontal_wing_container
    global number_of_horizontal_wings

    global V_ref_matrix
    global H_ref_matrix

    #We iterate though the V wings
    for first_v_wing in range(number_of_vertical_wings):
        print('------------------------------------------')
        print("First V Wing: {}".format(first_v_wing))
        current_col = vertical_wing_container[first_v_wing].column
        start_pos = vertical_wing_container[first_v_wing].start_pos
        end_pos = vertical_wing_container[first_v_wing].end_pos

        for i in range(vertical_wing_container[first_v_wing].size):

            if current_col == 0:
                j =1
            else:
                j=0


            temp_H_wing_ID = H_ref_matrix[start_pos+i][current_col+j]

            if temp_H_wing_ID == -1:
                continue
            H_wing_obj = horizontal_wing_container[temp_H_wing_ID]
            if H_wing_obj.start_pos > current_col+1 or H_wing_obj.row == end_pos:
                break



            if H_wing_obj.row == start_pos:
                continue

            print("------>H Wing: {}".format(temp_H_wing_ID))

            for k in range(2,(horizontal_wing_container[temp_H_wing_ID].size+1)):

                temp_col = horizontal_wing_container[temp_H_wing_ID].start_pos+k

                temp_sec_v_wing = V_ref_matrix[start_pos+i][temp_col]
                print("------------>Sec V Wing: {}".format(temp_sec_v_wing))

                if temp_sec_v_wing == -1:
                    continue

                temp_sec_obj = vertical_wing_container[temp_sec_v_wing]





                left_temp = [vertical_wing_container[first_v_wing].start_pos,
                             vertical_wing_container[first_v_wing].end_pos,
                             vertical_wing_container[first_v_wing].column,
                             vertical_wing_container[first_v_wing].harzard,
                             vertical_wing_container[first_v_wing].harzard_pos
                             ]
                middle_temp = [horizontal_wing_container[temp_H_wing_ID].start_pos,
                               horizontal_wing_container[temp_H_wing_ID].end_pos,
                               horizontal_wing_container[temp_H_wing_ID].row,
                               horizontal_wing_container[temp_H_wing_ID].harzard,
                               horizontal_wing_container[temp_H_wing_ID].harzard_pos
                               ]
                right_temp = [vertical_wing_container[temp_sec_v_wing].start_pos,
                              vertical_wing_container[temp_sec_v_wing].end_pos,
                              vertical_wing_container[temp_sec_v_wing].column,
                              vertical_wing_container[temp_sec_v_wing].harzard,
                              vertical_wing_container[temp_sec_v_wing].harzard_pos
                              ]
                H_finder(left_temp, middle_temp, right_temp)
        print('------------------------------------------')

def wing_connector_with_ref_old_2():
    global vertical_wing_container
    global number_of_vertical_wings

    global horizontal_wing_container
    global number_of_horizontal_wings

    global V_ref_matrix
    global H_ref_matrix

    for first_v_wing in range(number_of_vertical_wings):
        print('------------------------------------------')
        print("First V Wing: {}".format(first_v_wing))

        FW_obj = vertical_wing_container[first_v_wing]

        for i in range(1,FW_obj.size-1):
            #we iterate in the body of the first wing...

            #if we are dealing with a V wing on the left most side
            if FW_obj.column ==0:
                edge = 1
            else:
                edge =0

            H_wing_start = H_ref_matrix[FW_obj.start_pos+i][FW_obj.column+edge]

            if H_wing_start == -1:
                continue

            HW_obj = horizontal_wing_container[H_wing_start]



            # while(H_wing_start < number_of_horizontal_wings):
            while (HW_obj.start_pos <= FW_obj.column+1):

                col_itr =0

                print("------>H Wing: {}".format(H_wing_start))

                S_wing_start = V_ref_matrix[HW_obj.row][FW_obj.column+2+col_itr]

                if S_wing_start == -1:

                    col_itr +=1
                    
                    continue

                SW_obj = vertical_wing_container[S_wing_start]

                if SW_obj.column > HW_obj.end_pos + 1:
                    H_wing_start += 1
                    HW_obj = horizontal_wing_container[H_wing_start]
                    continue

                while(S_wing_start < number_of_vertical_wings):


                    SW_obj = vertical_wing_container[S_wing_start]



                    if SW_obj.column > HW_obj.end_pos+1:
                        break

                    print("------------>Sec V Wing: {}".format(S_wing_start))
                    left_temp = [FW_obj.start_pos,
                                 FW_obj.end_pos,
                                 FW_obj.column,
                                 FW_obj.harzard,
                                 FW_obj.harzard_pos
                                 ]
                    middle_temp = [HW_obj.start_pos,
                                   HW_obj.end_pos,
                                   HW_obj.row,
                                   HW_obj.harzard,
                                   HW_obj.harzard_pos
                                   ]
                    right_temp = [SW_obj.start_pos,
                                  SW_obj.end_pos,
                                  SW_obj.column,
                                  SW_obj.harzard,
                                  SW_obj.harzard_pos
                                  ]
                    H_finder(left_temp, middle_temp, right_temp)

                    S_wing_start+=1
                H_wing_start += 1
                HW_obj = horizontal_wing_container[H_wing_start]

def wing_connector_with_ref():
    global vertical_wing_container
    global number_of_vertical_wings

    global horizontal_wing_container
    global number_of_horizontal_wings

    global V_ref_matrix
    global H_ref_matrix

    global row_size
    global column_size

    global max_h_size

    for fw in range(number_of_vertical_wings):
        fw_obj = vertical_wing_container[fw]

        if fw_obj.column >= column_size-2:
            break

        # print('------------------------------------------')
        # print("First V Wing: {}".format(fw))

        for i in range(fw_obj.start_pos+1,fw_obj.end_pos-1):
            hw = H_ref_matrix[i][fw_obj.column]
            if hw == -1:
                hw = H_ref_matrix[i][fw_obj.column+1]
                if hw == -1:
                    continue
            hw_obj = horizontal_wing_container[hw]
            while(hw_obj.start_pos <= fw_obj.column+1 and hw_obj.row == i):

                if hw_obj.end_pos == fw_obj.column:
                    hw +=1
                    hw_obj = horizontal_wing_container[hw]
                    continue

                # print("------>H Wing: {}".format(hw))

                for j in range(fw_obj.column+1,hw_obj.end_pos+2):

                    if j == column_size:
                        break

                    sw = V_ref_matrix[hw_obj.row][j]
                    # print("------1------>Sec V Wing: {} .. j:{}".format(sw,j))
                    if sw == -1:
                        continue
                    sw_obj = vertical_wing_container[sw]


                    while(sw_obj.start_pos < hw_obj.row and sw_obj.column == j):
                        # print("------1------>Sec V Wing: {} .. j:{}".format(sw,j))



                        if sw_obj.end_pos == hw_obj.row:

                            sw+=1
                            if sw == number_of_vertical_wings:
                                break
                            sw_obj = vertical_wing_container[sw]
                            continue


                        temp_size = fw_obj.size+hw_obj.size+sw_obj.size
                        if temp_size < max_h_size:
                            sw += 1
                            if sw == number_of_vertical_wings:
                                break
                            sw_obj = vertical_wing_container[sw]
                            continue

                        left_temp = [fw_obj.start_pos,
                                     fw_obj.end_pos,
                                     fw_obj.column,
                                     fw_obj.harzard,
                                     fw_obj.harzard_pos
                                     ]
                        middle_temp = [hw_obj.start_pos,
                                       hw_obj.end_pos,
                                       hw_obj.row,
                                       hw_obj.harzard,
                                       hw_obj.harzard_pos
                                       ]
                        right_temp = [sw_obj.start_pos,
                                      sw_obj.end_pos,
                                      sw_obj.column,
                                      sw_obj.harzard,
                                      sw_obj.harzard_pos
                                      ]
                        # print('checking:{}-{}-{}'.format(fw_obj.wing_number,hw_obj.wing_number,sw_obj.wing_number))

                        H_finder(left_temp, middle_temp, right_temp)
                        sw += 1
                        if sw ==number_of_vertical_wings:
                            break
                        sw_obj = vertical_wing_container[sw]
                hw += 1
                hw_obj = horizontal_wing_container[hw]

def H_finder(left_wing,center_wing,right_wing):
    global max_h_size

    #print("-------------------------H_FINDER-------------------------")
    #we will get the 3 wings in arrarys.
    # we first need to trim the center wing such that it is in between the two vertical wings.
    # we will need to check if we have not cut away a hazard, if yes then we update the hazard counter.
    center_wing = center_trim(left_wing[2],center_wing,right_wing[2])

    #we then check if there are hazards in the center wing and if there are hazards in the veritcal wing
    #in other words... do we have two hazards that are inline horizontally with each other.
    #if yes we return zero because we cannot get rid of horizontally inline hazards.
    if inline_harzard_detect(left_wing,center_wing,right_wing):
        # print("In line detect found.... returning...")
        #There is an inline hazard which automatically voids this potential H
        return
    #we now trim the vertical wing such that they are inline
        #we find which vertical wing has the largest starting value. -> the wing that has the lowest starting position
        #we the find which vertical wing has the small ending value. -> the wing that has the highest ending value.
        #we then pop the starting and ending postion to these found values and we also check if we have not poped any hazards away
    left_wing,right_wing =vertical_trim(left_wing,right_wing,center_wing[2])
    if left_wing[0] == -1 or right_wing[0] == -1:
        #print("Vertical error on line 29")
        #The vertical_trim found an error. so this H is no longer valid
        return
    # print("Left Wing after veritcal trim... ",left_wing)
    # print("Right Wing after veritcal trim... ",right_wing)
    # print("Center Wing after veritcal trim... ",center_wing)
    #we should now have an H wing that has the correct shape.
    #We will now scan how many hazards we have.
    hazards = left_wing[3] + right_wing[3] + center_wing[3]
    if hazards <= 1:
        #print("only 1 hazard ... checking size !")
        # if hazard less or equal to 1 we than count the size of our H.
        h_size = get_H_size(left_wing,right_wing)
        if h_size > max_h_size:
            # print("Hazard 1 : Max found :", h_size, "Left Wing:", left_wing,"Center Wing: ", center_wing,"Right Wing: ", right_wing)
            max_h_size = h_size
            return
    else:
        # print("Final Left wing is : ", left_wing)
        # print("Final Right wing is:", right_wing)
        # print("Final Center wing is:", center_wing)
        #we need to make new copys of the wings
        center_final = center_wing

        #if greater than one we need to pop the vertical wings again.
        #the part that I have not really thought about...
        #We need to approach this from certain places.

        #If the center has a hazard we must reduce the vertical wings such that they have no hazards.
        if center_final[3] > 0:
            left_final = copy.deepcopy(left_wing)
            right_final = copy.deepcopy(right_wing)
            #print("In center checker.... ")
            #print("Final Left wing is : ", left_final)
            #print("Final Right wing is:", right_final)
            #we will trim the vertival wings based of the hazard postiion
            # and the position of the center wing. if it is start -> center wing -> Hazard -> end
            # then hazard -1 will become our new end so : start -> center wing -> Harazard-1

            #if it is start -> hazard ->center wing ->end .... then harzard+1 will become our new start
            #so hazard+1 ->center wing -> end.

            #when this happens the hazard is automatically removed....

            #if left wing has a hazard
            if left_final[3] > 0:
                #print("Left Wing has a Hazard...")
                # we will start with the left wing by calling harazard traim and pass it the left wing...
                left_final = hazard_trim(left_final,center_final[2])

                #print("Left wing trimmed ... result:", left_final)
                    #we then call the vertical trim function to trim the right wing to the same length as the left wing.
                left_final, right_final = vertical_trim(left_final, right_final, center_final[2])
                #print("Vertical trim complete... left:",left_final,"Right: ", right_final)
                #we will then check is v trim retuned an errror if yes we jsut return...
                if left_final[0] == -1 or right_final[0] == -1:
                    # print("Error occured... h no longer valid...")
                    #not valid.
                    return

            #if no errors we will check if the right wing has a hazard....
            if right_final[3] > 0:
                #print("Right Wing has a Hazard...")
                # if there is a hazard we will call the hazard trim
                #print("Right wing before trim ... result:", right_final)
                right_final = hazard_trim(right_final,center_wing[2])

                #print("Right wing trimmed ... result:", right_final)
                #we will then call vertical trim again
                left_final, right_final = vertical_trim(left_final, right_final, center_final[2])
                #print("Vertical trim complete... left:", left_final, "Right: ", right_final)
                #we will check for errors
                if left_final[0] == - 1 or right_final[0] == -1:
                    # print("Error occured... h no longer valid...")
                    # not valid.
                    return

            #if there are no errors or no hazards in the right wing
            #we then calculate the size and compare and then return....
            h_size = get_H_size(left_final,right_final)
            if h_size > max_h_size:
                # print("Center 1: Max found :", h_size, "Left Wing:", left_final,"Center Wing: ", center_final,"Right Wing: ", right_final)
                max_h_size = h_size

        else:


            #if theree are no hazards in the center we need to check both sides ...

            #if there is a hazard in the left
            if left_wing[3] > 0:
                #print("Going Left ... doing deep copy... ")
                left_final = copy.deepcopy(left_wing)
                right_final = copy.deepcopy(right_wing)
                #we will call hazard_trim on the left wing
                #print("---------------Doing left trim .. before: ", left_final)
                left_final = hazard_trim(left_final,center_final[2])


                #print("---------------Doneleft trim .. after: ", left_final)
                #we will then call vertical wing trim
                #print("---------------Doing Vertical Trim... left before:",left_final," .. right before: ", right_final)
                left_final,right_final = vertical_trim(left_final,right_final,center_final[2])
                #print("---------------Done Vertical Trim... left after:", left_final, " .. right after: ", right_final)
                #we will then check if there are no errors
                if left_final[0] != -1 and right_final[0] != -1:
                    #print("---------------Vertical trim was ok .... checking sizes ... ")
                    #no errors so we will check the size...
                    h_size = get_H_size(left_final, right_final)
                    if h_size > max_h_size:
                        # print("Left 1: Max found :", h_size, "Left Wing:", left_final,"Center Wing: ", center_final,"Right Wing: ", right_final)
                        max_h_size = h_size
                        #we dont return because we still need to check the right side...

            # if there is a hazard in the right side
            if right_wing[3] > 0:
                #print("Going Right ... doing deep copy... ")
                left_final = copy.deepcopy(left_wing)
                right_final = copy.deepcopy(right_wing)
                #we will call the hazard_trim for the right side
                #print("---------------Doing right trim .. before: ", right_final)
                right_final = hazard_trim(right_final,center_final[2])

                #print("---------------Done right trim .. after: ", right_final)
                #we will then call the vertical trim
                #print("---------------Doing Vertical Trim... left before:", left_final, " .. right before: ", right_final)
                left_final, right_final = vertical_trim(left_final, right_final, center_final[2])
                #print("---------------Done Vertical Trim... left after:", left_final, " .. right after: ", right_final)
                # we will then check if there are no errors
                if left_final[0] != -1 and right_final[0] != -1:
                    #print("---------------Vertical trim was ok .... checking sizes ... ")
                    # no errors so we will check the size...
                    h_size = get_H_size(left_final, right_final)
                    if h_size > max_h_size:
                        # print("Right 1: Max found :", h_size, "Left Wing:", left_final,"Center Wing: ", center_final,"Right Wing: ", right_final)
                        max_h_size = h_size
                        # we dont return because we still need to check the right side...
            #final reutrn here

def center_trim(start_c, c_wing, end_c):
    #print("Center Trim Running .... Starting C_wing:", c_wing)
    # start_c will be the column where left wing is located
    # end_c will be the column where the righ wing is located
    # c_wing will be the center wing array from H_finder. Will will modify this and return it to H_finder.

    # first we check if c_wing start is less than or equal to the start_c value.
    if c_wing[0] <= start_c:
        # if yes. c_wing start = start_c+1 ... plus one because it should be nexto the column.
        c_wing[0] = start_c + 1
    # now we check if the c_sing end is greater than or equal to the end_c value.
    if c_wing[1] >= end_c:
        # if yes. c_wing end = end_c-1 .. minus one because it should be nexto the column...
        c_wing[1] = end_c - 1

        # now we should check if we have not removed a hazard from the center wing...
        # we first check if there are any hazards....
        if c_wing[3] > 0:
            # is hazard poistion is less than c_wing start or hazard position is greater than c_wing end.
            if c_wing[4] < c_wing[0] or c_wing[4] > c_wing[1]:
                # the hazard is now out of the trimmed wing.
                # now we set the hazard counter = 0
                c_wing[3] = 0
    #print("Center Trim complete reutrning...: ", c_wing)
    return c_wing

def inline_harzard_detect(left_wing,center_wing,right_wing):
    #print("Inline Haz Detect Running ....")
    if center_wing[3] == 0:
        #if the center wing has no hazards then we are good
        return False
    else:
        if(left_wing[3]>0 and left_wing[4] == center_wing[2]):
            #The left wing has a hazard and it is inline with the center wings hazard...
            return True
        if(right_wing[3]>0 and right_wing[4] == center_wing[2]):
            #The right wing has a hazard and it is inline iwth the cinter wings hazard...
            return True
        else:
            #Nothing was found therefor no inline hazard...
            return False

def vertical_trim(lw,rw,center_pos):
    #In this function we need to make the vertical wings the same length.

    #we first need to see which wing has the largest starting value
        #we then take the opposite wing and make that wings starting value the same.
    if lw[0] > rw[0]:
        rw[0] = lw[0]
    elif rw[0] > lw[0]:
        lw[0] = rw[0]

    #we the find which wing has the smallest ending value.
        #we then take the opposite wing and make that wings ending vlaue the same.
    if lw[1] < rw[1]:
        rw[1] = lw[1]
    elif rw[1] < lw[1]:
        lw[1] = rw[1]

    #We then need to see if these wings still have a valid size... >2
    if (lw[1]-lw[0])+1 < 3 or (rw[1]-rw[0])+1 < 3:
        lw[0] = -1
        rw[0] = -1
        #The wings are to small set the first element to -1 and exit.
        #H_finder will check if it is -1 and also return since it is now invalue
        return lw,rw

    # We now need to check if the center wing is still inbetween the newly trimmed vertrical wings...
    if center_pos <=lw[0] or center_pos>=lw[1]:
        lw[0] = -1
        rw[0] = -1
        #the center wing is on the border or passed the board of the vertical wings...
        #this wing is now no longer valid.
        return lw, rw

    #The center wing is still in a valid spot...
    #We then also need to check if we removed any hazards during the trimming proccess for both wings...
    if lw[3] > 0:
        if lw[4] < lw[0] or lw[4] > lw[1]:
            lw[3] = 0
    if rw[3] > 0:
        if rw[4] < rw[0] or rw[4] > rw[1]:
            rw[3] = 0
    #Any redunant hazards have been removed

    #We will then return the altered wings...
    return lw,rw

def get_H_size(left,right):
    #Get the size of both veritcal wings
    v_size = ((left[1] - left[0]) +1) *2
    #get the size of the horizontal wings

    h_size = (right[2]-left[2])-1
    return v_size+h_size

def hazard_trim(wing,center_pos):
    #Here we will give a wing and the position where the center wing starts.
    #the job is the trim the wing either between the start pos and the hazard or the hazard and the ending pos
    #depedning where the center wing is will determine which side of trim we do.
    if wing[0] < center_pos and wing[4] > center_pos:
        #the hazard pos -1 will be our new end.
        wing[1] = wing[4]-1
        wing[3] = 0
        return wing
    if wing[4] < center_pos and wing[1] > center_pos:
        #hazard pos +1 will be our new begin
        wing[0] = wing[4]+1
        wing[3] = 0
        return wing
    if wing[4] == center_pos:
        # return an invalid wing
        wing[1] = center_pos - 1
        return wing

def get_inputs():
    global matrix
    global column_size
    global row_size
    row_size, column_size  = input().split()
    row_size = int(row_size)
    column_size = int(column_size)
    generate_ref_matrix()
    for i in range(row_size):
        row = list(input())
        # print(row)
        matrix.append(row)

def copy_vertical_wings_and_sort():
    global vertical_wing_container_sorted
    global vertical_wing_container
    global number_of_vertical_wings
    for i in range(number_of_vertical_wings):
        vertical_wing_container_sorted.append([vertical_wing_container[i].start_pos,i])
    print(vertical_wing_container_sorted)
    vertical_wing_container_sorted.sort()
    print(vertical_wing_container_sorted)

def display_matrix(select):
    global matrix
    global H_ref_matrix
    global V_ref_matrix
    global column_size
    global row_size
    print('----------------------------')
    if select == 'main':
        print('Main matrix')
        for row in range(row_size):
            print(matrix[row])

    elif select == 'vref':
        print('V ref matrix')
        for row in range(row_size):
            print(V_ref_matrix[row])

    elif select == 'href':
        print('H ref matrix')
        for row in range(row_size):
            print(H_ref_matrix[row])
    print('----------------------------')

def generate_ref_matrix():
    #Here we generate the reference matrices
    global V_ref_matrix
    global H_ref_matrix
    global column_size
    global row_size

    for i in range(row_size):
        V = []
        H = []
        for k in range(column_size):
            V.append(-1)
            H.append(-1)
        V_ref_matrix.append(V)
        H_ref_matrix.append(H)

# -------Testing Functions------------

def get_inputs_from_file(dir):
    global matrix
    global column_size
    global row_size

    line_number = 0

    file = open(dir,'r')

    for line in file:
        if line_number ==0:
            row_size, column_size = line.split()
            row_size = int(row_size)
            column_size = int(column_size)
            generate_ref_matrix()
        else:
            stripped_row = line.strip()
            row_list = list(stripped_row)
            # print(row_list)
            matrix.append(row_list)
        line_number+=1
    file.close()

def get_reference_result(dir):
    file = open(dir)
    for line in file:
        awnser = line.strip("\n")

    file.close()
    return int(awnser)

def reset_all_data():
    global matrix
    global column_size
    global row_size
    global horizontal_wing_container
    global number_of_horizontal_wings
    global vertical_wing_container_sorted
    global vertical_wing_container
    global number_of_vertical_wings
    global temp_wing_container
    global max_h_size
    global V_ref_matrix
    global H_ref_matrix

    matrix = []
    column_size = 0
    row_size =0

    horizontal_wing_container = []

    number_of_horizontal_wings = 0

    vertical_wing_container_sorted = []
    vertical_wing_container = []
    number_of_vertical_wings = 0

    temp_wing_container = []

    max_h_size = 0

    V_ref_matrix = []
    H_ref_matrix = []

def test_all(type):
    if (type > 10 or type <1) and type != -1:
        print("Type must be between 1 and 10")
        return ValueError
    if type != -1:
        #Here are are only testing one case
        correct_counter = 0

        string = './pubdata/'

        for i in range(type, type+1):

            reset_all_data()
            if i < 10:
                end = 'pub0' + str(i)
            else:
                end = 'pub' + str(i)
            file = string + end
            file_out = file + '.out'
            file_in = file + '.in'
            print("--------------------------------")
            print("Testing: ", file)
            main_start = time.time()
            get_inputs_from_file(file_in)
            display_matrix('vref')
            display_matrix('href')
            display_matrix('main')

            find_horizontal_wing()
            find_vertical_wing()
            print_vertical_wings()
            print_horizontal_wings()
            # wing_connector()
            wing_connector_with_ref()
            main_end = time.time()
            print("Time:", main_end - main_start)
            print("Reference Awnser: ", get_reference_result(file_out))
            if get_reference_result(file_out) == max_h_size:
                print("{} --- Good ! :)".format(max_h_size))
                correct_counter += 1
            else:
                print("{} --- Bad :( ".format(max_h_size))
            print("--------------------------------")

            display_matrix('vref')
            display_matrix('href')

    else:
        #We are testing all cases...
        correct_counter = 0

        string = '../../pubdata/'

        for i in range(1, 11):

            reset_all_data()
            if i < 10:
                end = 'pub0' + str(i)
            else:
                end = 'pub' + str(i)
            file = string + end
            file_out = file + '.out'
            file_in = file + '.in'
            print("--------------------------------")
            print("Testing: ", file)
            main_start = time.time()
            get_inputs_from_file(file_in)
            find_horizontal_wing()
            find_vertical_wing()


            # wing_connector()

            wing_connector_with_ref()
            main_end = time.time()
            print("Time:", main_end - main_start)
            print("Reference Awnser: ", get_reference_result(file_out))
            if get_reference_result(file_out) == max_h_size:
                print("{} --- Good ! :)".format(max_h_size))
                correct_counter += 1
            else:
                print("{} --- Bad :( ".format(max_h_size))
            print("--------------------------------")

        print("{}/10 Correct".format(correct_counter))

# -------Testing Functions END---------


# test_all(-1)
# test_all(1)
# test_all(-1)




# get_inputs_from_file('./pubdata/pub04.in')

#
get_inputs()
find_horizontal_wing()
find_vertical_wing()
wing_connector_with_ref()
print(max_h_size)

# print_vertical_wings()
# print_horizontal_wings()
# copy_vertical_wings_and_sort()


# start_time = time.time()
# wing_connector()
# print("--- %s seconds ---" % (time.time() - start_time))
# print(max_h_size)





