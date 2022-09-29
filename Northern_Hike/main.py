checkpoints = []

minE = 0
maxE = 0

minT = 0
maxT = 0

minD = 0
maxD = 0

hike_min_distance = 0
hike_max_distance = 0
hike_min_elevation = 0
hike_max_elevation = 0

number_of_check_points = 0

# sections =[
#     [2, 6, 300, 14, 33],
#     [3, 6, 300, 10, 25],
#     [5, 9, 400, 15, 31],
#     [6, 9, 400, 12, 24],
#     [8, 14, 500, 17, 38],
#     [9, 14, 500, 16, 36]
# ]




# minD = 10
# maxD = 40
# minT = 10
# maxT = 40
# minE = 100
# maxE = 500
#
# hike_min_distance = 10
# hike_max_distance = 50
# hike_min_elevation = 100
# hike_max_elevation = 800
#
#
# number_of_check_points = 16
#
# checkpoints = [
#     [0, 200, 10, 3],
#     [1, 400, 8, 4],
#     [1, 200, 12, 5],
#     [0, 500, 6, 2],
#     [1, 400, 7, 3],
#     [1, 100, 10, 6],
#     [0, 300, 12, 5],
#     [1, 500, 2, 1],
#     [1, 400, 8, 3],
#     [0, 600, 8, 5],
#     [0, 900, 12, 5],
#     [1, 500, 4, 1],
#     [0, 400, 4, 2],
#     [1, 200, 15, 7],
#     [0, 300, 10, 3],
#     [0, 200, 0, 0]
# ]

elevations = []
prefix_sum_array_time = []
prefix_sum_array_distance = []
prefix_sum_array_elevation = []

prefix_sum2_elevations = []
prefix_sum2_times = []
prefix_sum2_distances = []

camp_sites = []
camp_connections = []

sections = []

hikes = []


def print_inputs():
    print(minD, " ", maxD, " ", minT, " ",maxT, " ",minE, " ", maxE)
    print(type(minD), ' ',type(maxD), ' ',type(minT), ' ',type(maxT), ' ',type(minE), ' ',type(maxE))
    print(hike_min_distance, " ",hike_max_distance, " ",hike_min_elevation, "", hike_max_elevation)
    print(type(hike_min_distance), ' ', type(hike_max_distance), ' ', type(hike_min_elevation), ' ', type(hike_max_elevation))
    print(number_of_check_points)
    print(checkpoints)

def get_inputs():
    global minE
    global maxE

    global minT
    global maxT

    global minD
    global maxD

    global hike_min_distance
    global hike_max_distance
    global hike_min_elevation
    global hike_max_elevation

    global number_of_check_points

    number_of_check_points = 0
    # print("Data for section Limits")
    # print("Enter min distance, max distance, min time, max time, min elevation, max elevation")
    minD, maxD, minT, maxT, minE, maxE = input().split()
    minD = int(minD)
    maxD = int(maxD)
    minT = int(minT)
    maxT = int(maxT)
    minE = int(minE)
    maxE = int(maxE)
    # print("Input Hike Limits")
    # print("Enter min distance, max distance, min time, max time, min elevation, max elevation")
    hike_min_distance, hike_max_distance, hike_min_elevation, hike_max_elevation = input().split()

    hike_min_distance = int(hike_min_distance)
    hike_max_distance = int(hike_max_distance)
    hike_min_elevation = int(hike_min_elevation)
    hike_max_elevation = int(hike_max_elevation)


    # print("Number of Check points")
    number_of_check_points = input()

    for i in range(int(number_of_check_points)):
        temp = input().split()
        data = list(map(int,temp))
        checkpoints.append(data)

def elevation_detect(array):
    #print("Elevation Detect Called: ")
    output_array = []

    for i in range(len(array)):
        if (i == 0):
            i+=1
        else:
            temp = array[i][1] - array[i-1][1]
            #print("[", i, " ", i+1, "] ==> ", temp)
            if temp > 0:
                output_array.append(temp)
            else:
                output_array.append(0)
    return output_array

def extract_data(array,data):
    #print("Extra Data Called: ")
    output_array = []
    for i in range(len(array)):
        output_array.append(array[i][data])
    #print("Result: ")
    #print(output_array)
    return output_array

def generate_prefix_array(data_array):
    #print("Generate Prefix Sum Array Called: ")
    output_array = []
    for i in range(len(data_array)):
        if i == 0:
            output_array.append(0)
            output_array.append(data_array[0])
        else:
            output_array.append(output_array[i] + data_array[i])
    #print("Result: ")
    #print(output_array)
    return output_array

def prefix_sum_array_extract(array, start, end):
    #print("[",start, " ", end, "] ==>", array[end-1], '-',  array[start-1], "= " , array[end-1] - array[start-1] )
    return array[end - 1] - array[start - 1]

def camp_to_camp_data_extract():
    global camp_sites
    global camp_connections
    for i in range(len(camp_sites)-1):
        data = []
        time = prefix_sum_array_extract(prefix_sum_array_time, camp_sites[i], camp_sites[i + 1])
        distance = prefix_sum_array_extract(prefix_sum_array_distance, camp_sites[i], camp_sites[i + 1])
        elevation = prefix_sum_array_extract(prefix_sum_array_elevation, camp_sites[i], camp_sites[i + 1])

        data.append(camp_sites[i])
        data.append(camp_sites[i + 1])
        data.append(elevation)
        data.append(time)
        data.append(distance)
        camp_connections.append(data)

def campsite_detect(array):
    #print("Camp Site Detect Called: ")
    output_array = []

    for i in range(len(array)):
        if(array[i][0] == 1):
            output_array.append(i+1)
    #print("Result: ")
    #print(output_array)
    return output_array


def max_limit_check_sections(elevation,time,distance):

    global maxE
    global maxT
    global maxD
    # print(type(distance))
    # print(type(maxD))
    # print(type(time))
    # print(type(maxT))
    # print(type(elevation))
    # print(type(maxE))
    if distance <= maxD and time <= maxT and elevation <= maxE:
        return 1
    else:
        return 0

def min_limit_check_sections(elevation,time,distance):

    global minE
    global minT
    global minD
    if distance>=minD and time>=minT and elevation>=minE:
        return 1
    else:
        return 0

def print_sections(array):
    global camp_sites
    print("")
    print("###########################")
    print("Print Sections called")
    for i in range(len(array)):
        print("Section: [", camp_sites[array[i][0]], " ", camp_sites[array[i][0]+array[i][4]], "]")
        print("     => Campsite: ", camp_sites[array[i][0]])
        print("     => Elevation: ", array[i][1])
        print("     => Time: ",array[i][2] )
        print("     => Distance: ", array[i][3])
        print("     => Counter/Hops: ", array[i][4])
    print("###########################")
    print("")




def sliding_window_sections(array):

    #print("Sliding Window Called")


    for i in range(len(array)):
        global sections
        begin = i
        end = i
        counter = 1
        currentElevation = array[i][2]
        currentTime = array[i][3]
        currentDistance = array[i][4]
        bestBegin = -1
        bestEnd = -1
        bestElevation = -1
        bestTime = -1
        bestDistance = -1
        while end < len(array):

            #print("sum from", begin, "to", end, " Distance: ", currentDistance, " Elevation: ",currentElevation, " Time: ", currentTime)

            if limit_check_max_sections(currentDistance,currentElevation,currentTime) and end - begin > bestEnd - bestBegin:
                bestBegin = begin
                bestEnd = end
                bestElevation = currentElevation
                bestDistance = currentDistance
                bestTime = currentTime
            if limit_check_max_sections(currentDistance,currentElevation,currentTime):
                end += 1
                if end < len(array):
                    currentElevation += array[end][2]
                    currentTime += array[end][3]
                    currentDistance += array[end][4]
                    counter +=1

            else:
                currentElevation -= array[begin][2]
                currentTime -= array[begin][3]
                currentDistance -= array[begin][4]
                counter -= 1
                break
        if limit_check_min_sections(bestDistance,bestElevation,bestTime):
            #print("Best Found: Start: ", bestBegin, "End: ", bestEnd)
            data = []
            data.append(bestBegin)
            data.append(bestElevation)
            data.append(bestTime)
            data.append(bestDistance)
            data.append(counter)
            sections.append(data)
        if bestBegin == -1 and bestEnd == -1:
            bestBegin = i
            counter = 1
            bestElevation = currentElevation
            bestDistance = currentDistance
            bestTime = currentTime
            if limit_check_min_sections(bestDistance, bestElevation, bestTime):
                data = []
                data.append(bestBegin)
                data.append(bestElevation)
                data.append(bestTime)
                data.append(bestDistance)
                data.append(counter)
                sections.append(data)



def print_hikes():
    global hikes
    for i in range(len(hikes)):
        print("###########################################")
        print("Start: ", hikes[i][0], " End: ", hikes[i][1])
        print("Elevation: ", hikes[i][2])
        print("Distance: ", hikes[i][3])
        print("Sections: ", hikes[i][4])
        print("###########################################")

def find_best_hike():
    global hikes
    maxd = 0
    dcount = 0
    dpos = []
    maxe = 0
    ecount = 0
    epos = []

    maxseccount = 0
    secpos = 0

    for i in range(0,len(hikes)):
        if maxd < hikes[i][1]:
            maxd = hikes[i][1]
    for i in range(len(hikes)):
        if maxd == hikes[i][1]:
            dcount +=1
            dpos.append(i)
    if dcount == 1:
        position = dpos[0]
        return [hikes[position][1], hikes[position][0], hikes[position][2]]
    if dcount > 1:
        for i in range(len(dpos)):
            position = dpos[i]
            if maxe < hikes[position][0]:
                maxe = hikes[position][0]

        for i in range(len(dpos)):
            position = dpos[i]
            if maxe == hikes[position][0]:
                ecount += 1
                epos.append(position)
    if ecount == 1:
        position = epos[0]
        return [hikes[position][1], hikes[position][0], hikes[position][2]]

    if ecount > 1:
        maxseccount = hikes[epos[0]][2]
        secpos = epos[0]
        for i in range(len(epos)):
            position = epos[i]

            if maxseccount > hikes[position][2]:
                maxseccount = hikes[position][2]
                secpos=position

    position = secpos
    return [hikes[position][1], hikes[position][0], hikes[position][2]]



def limit_check_max_sections(D,E,T):
    global maxE
    global maxT
    global maxD

    if D<= maxD and E<=maxE and T<=maxT:
        return 1
    else:
        return 0

def limit_check_min_sections(D,E,T):
    global minE
    global minT
    global minD

    if D>=minD and E>=minE and T>=minT:
        return 1
    else:
        return 0

def hike_finder(array):
    global hikes
    global camp_sites
    for i in range(len(array)):
        counter = 1
        begin = i
        end = i
        currentDistance = array[end][3]
        currentElevation = array[end][1]
        bestBegin = -1
        bestEnd = -1
        bestDistance = -1
        bestElevation = -1

        while end < len(array):

            #print("sum from", camp_sites[begin], "to", camp_sites[end], " Distance: ", currentDistance, " Elevation: ", currentElevation)

            if limit_check_max_hikes(currentDistance,currentElevation) and end - begin > bestEnd - bestBegin:
                #print("in 1st if")
                bestBegin = begin
                bestEnd = end
                bestElevation = currentElevation
                bestDistance = currentDistance

            if limit_check_max_hikes(currentDistance,currentElevation):
                end += array[end][4]
                if end < len(array):
                    currentElevation += array[end][1]
                    currentDistance += array[end][3]
                    counter +=1
            else:
                currentElevation -= array[end][1]
                currentDistance -= array[end][3]
                counter -=1

                break
        if limit_check_min_hikes(bestDistance,bestElevation):
            #print("Best Found: Start: ", camp_sites[bestBegin], "End: ", camp_sites[bestEnd])
            data = []
            data.append(bestElevation)
            data.append(bestDistance)
            data.append(counter)
            hikes.append(data)
        if bestBegin == -1 and bestEnd == -1:
            bestBegin = i
            counter = 1
            bestElevation = currentElevation
            bestDistance = currentDistance
            if limit_check_min_hikes(bestDistance,bestElevation):
                data = []
                data.append(bestElevation)
                data.append(bestDistance)
                data.append(counter)
                hikes.append(data)

def limit_check_max_hikes(D,E):
    global hike_max_elevation
    global hike_max_distance

    if D<= hike_max_distance and E<=hike_max_elevation :
        return 1
    else:
        return 0

def limit_check_min_hikes(D,E):
    global hike_min_elevation
    global hike_min_distance

    if D>=hike_min_distance and E>=hike_min_elevation:
        return 1
    else:
        return 0


get_inputs()
#print_inputs()

elevations = elevation_detect(checkpoints)

prefix_sum_array_distance = generate_prefix_array(extract_data(checkpoints,2))

prefix_sum_array_time = generate_prefix_array(extract_data(checkpoints,3))

prefix_sum_array_elevation = generate_prefix_array(elevations)

camp_sites = campsite_detect(checkpoints)

camp_to_camp_data_extract()

#print(camp_connections)

sliding_window_sections(camp_connections)
#print(sections)
#print_sections(sections)

hike_finder(sections)

#print("#printing Hikes")
#print(hikes)

best_hike = find_best_hike()

print(best_hike[0],best_hike[1],best_hike[2])