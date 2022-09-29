import re

# sentances = [
#     'That year winter weather lasted till early May.',  # 1
#     'Jill left in February, she spent 8 days in Berlin.',  # 2
#     'The newly planted trees were held up by wooden frames.',  # 3
#     'There were only seventeen players in the club in August.',  # 4
#     'She said it happened on 23.12. and others supported her view.',  # 5
#     'Tom, Pat and Sue had no time in November, however.',  # 6
#     'April and May were her favourite names and 27 was her favourite number.',  # 7
#     'In August it was possible to collect 23, 24, and 25 specimens, respectively.',  # 8
#     'They intended to arrive on 23.8. or on 27.8.',  # 9
#     'We could not find any documents in the 4th drawer.',  # 10
#     'Sand was blown on the beach on 1.1. in Perth.',  # 11
#     'Numbers 11, 12 or 14 may be brought in focus in April this year.',  # 12
#     'Another example is 5 and 10 of February.',  # 13
#     'And finally, check 1 2 3 in July against 5 6 7 in other months.'  # 14
# ]
# numberofsentances = 14
# flag_reg_invalid = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# flag_reg_months = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# flag_reg_days = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# flag_reg_DM = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


sentances = []

numberofsentances = 0

flag_reg_invalid = []
flag_reg_months = []
flag_reg_days = []
flag_reg_DM = []

month_reference = [31,28,31,30,31,30,31,31,30,31,30,31]



pattern = re.compile(r'(\bJanuary(\.|\,|\s))|(\bFebruary(\.|\,|\s))|(\bMarch(\.|\,|\s))|(\bApril(\.|\,|\s))|(\bMay(\.|\,|\s))|(\bJune(\.|\,|\s))|(\bJuly(\.|\,|\s))|(\bAugust(\.|\,|\s))|(\bSeptember(\.|\,|\s))|(\bOctober(\.|\,|\s))|(\bNovember(\.|\,|\s))|(\bDecember(\.|\,|\s))|(\b\d{1,2}[.]\d{1,2}[.])|(\b(\d{1,2})(\s|\.|\,))')

extracted_data = []

def get_inputs():
    global numberofsentances
    numberofsentances = input()

    numberofsentances = int(numberofsentances)

    for i in range(int(numberofsentances)):
        temp = input()
        sentances.append(temp)

def DM_to_test(date):
    x = date.split(".")
    day = x[0]
    if x[1] == '1':
        month = 'January'
    elif x[1] == '2':
        month = 'February'
    elif x[1] == '3':
        month = 'March'
    elif x[1] == '4':
        month = 'April'
    elif x[1] == '5':
        month = 'May'
    elif x[1] == '6':
        month = 'June'
    elif x[1] == '7':
        month = 'July'
    elif x[1] == '8':
        month = 'August'
    elif x[1] == '9':
        month = 'September'
    elif x[1] == '10':
        month = 'October'
    elif x[1] == '11':
        month = 'November'
    elif x[1] == '12':
        month = 'December'
    return month,day

def DM_extractor(line,date):
        if flag_reg_invalid[line] != 1:
            if flag_reg_DM[line] == 1:
                output = []
                output.append(line+1)
                output.append(DM_to_test(date[0][2])[0])
                output.append(DM_to_test(date[0][2])[1])
                extracted_data.append(output)
                return 1
        return 0

def months_without_days_checker(line):
    if flag_reg_months[line] >=1 and flag_reg_days[line] == 0:
        return 1
    else:
        return 0

def multiple_occurance_checker(line):
    if flag_reg_DM[line] > 1 or flag_reg_months[line] > 1:
        return 1

    if flag_reg_DM[line] >= 1 and flag_reg_months[line] >= 1:
        return 1
    return 0

def date_checker(day,month):
    day = day.replace(",", "")
    day = day.replace(".", "")

    day = int(day)
    month = int(month)
    #We check if the given month exists

    if month > 12:
        return 0
    if day > 31:
        return 0

    #Month Reference looks at each month in the year 2019
    #[0]=>January  to [11}=>Decmeber with their number of days

    if(month_reference[month-1]>=day):
        return 1
    else:
        return 0

def extracted_data_check(line,data):
    if data[0].isalpha():
        flag_reg_months[line] +=1

        return 1
    else:
        if len(data) > 3:
            #check validity of DM
            date_test_temp = data.split(".")
            if date_checker(date_test_temp[0], date_test_temp[1]):
                flag_reg_DM[line]+=1
                return 1
            else:

                return 0
        if len(data) <= 3:

            flag_reg_days[line] += 1
            return 1

def month_name_to_number(month):
    if month.find("January") != -1:
        return 1
    elif month.find("February") != -1:
        return 2
    elif month.find("March") != -1:
        return 3
    elif month.find("April") != -1:
        return 4
    elif month.find("May") != -1:
        return 5
    elif month.find("June") != -1:
        return 6
    elif month.find("July") != -1:
        return 7
    elif month.find("August") != -1:
        return 8
    elif month.find("September") != -1:
        return 9
    elif month.find("October") != -1:
        return 10
    elif month.find("November") != -1:
        return 11
    elif month.find("December") != -1:
        return 12

def month_day_extractor(data,m_position):
    month_number = month_name_to_number(data[m_position][2])
    best_distance = -1
    best_day_position = 0
    left = 1
    for i in range(len(data)):

        if i == m_position:
            left = 0
            continue
        if left:
            current_ditance = data[m_position][0] - data[i][1]
            if best_distance > current_ditance or best_distance ==-1:
                if date_checker(data[i][2],month_number):
                    best_distance = current_ditance
                    best_day_position = i
        else:
            current_ditance = data[i][0] - data[m_position][1]
            if best_distance > current_ditance or best_distance ==-1:
                if date_checker(data[i][2], month_number):
                    best_distance = current_ditance
                    best_day_position = i


    if best_distance == -1:
        return -1
    else:
        return best_day_position

def setup_flag_regs(l):
    # global flag_reg_months
    # global flag_reg_days
    # global flag_reg_DM
    for i in range(l):
        flag_reg_months.append(0)
        flag_reg_days.append(0)
        flag_reg_DM.append(0)
        flag_reg_invalid.append(0)

def extract_data(data):
    for i in range(len(data)):
        line_miss = -1
        month_position = 0
        counter = 0

        line_information = []
        for match in pattern.finditer(data[i]):
            line_miss = 0

            if extracted_data_check(i,match.group()):

                counter +=1
                temp =[]
                #temp.append(i)
                temp.append(match.start())
                temp.append(match.end())
                temp.append(match.group())
                line_information.append(temp)
                if(match.group()[0].isalpha()):
                    #If a month is detected store the poistion in the temp arrary if multiple month exsist then this variable will not matter since the line will be dropped anyway

                    month_position = counter


            if multiple_occurance_checker(i):
                #Setting Respective line as invalid, Either Multiple Months or Multiple DMs or Valid DM and Valid Month in same line

                flag_reg_invalid[i] = 1 #We dont need to save this. If the break occours the information will not be saved in its final place
                break

        if line_miss == -1:

            continue


        if flag_reg_invalid[i] == 1:

            continue
        #Here we should find DMs and store them, we did not need to wory about multiple DMs or Months since it has already been filterd

        if DM_extractor(i,line_information):

            continue

        if flag_reg_months[i] != 1:

            continue

        #If No DMs are found we need to look for Months and Days
        if months_without_days_checker(i):
            #If we have a line without a DM and with a month but no days for that month we say the line is invalid
            flag_reg_invalid[i] = 1
            continue

        #If There is one Month and only one day then we just add them to the results
        if flag_reg_days[i] == 1 and flag_reg_months[i] == 1:

            temp = []
            temp.append(i+1)
            #The month will always be where month_position is pointing
            temp.append(line_information[month_position-1][2])
            month_number = month_name_to_number(line_information[month_position-1][2])

            #If the month position is the first element than the day will be to the left
            if month_position == 1:
                val = line_information[month_position][2]
                if date_checker(val,month_number):
                    temp.append(val)
                else:
                    continue
            #if the month poition is not 1 than the day position will be to the right
            else:
                val = line_information[month_position-2][2]
                if date_checker(val,month_number):
                    temp.append(val)
                else:
                    continue

            extracted_data.append(temp)
            continue
        # If we are here that means no DMs were found and there is a valid number of days
        # We should not find the Month in our Line information


        bestday = month_day_extractor(line_information,month_position-1)
        #If we do not find a day that is satisfiable we return -1
        if bestday == -1:
            continue
        else:
            temp =[]
            temp.append(i+1)
            temp.append(line_information[month_position-1][2])
            temp.append(line_information[bestday][2])
            extracted_data.append(temp)



def outputs_print():
    for i in range(len(extracted_data)):
        line = extracted_data[i][0]
        line = str(line)
        month = extracted_data[i][1]
        month = month.replace(",", "")
        month = month.replace(".", "")
        month = month.replace(" ", "")
        day = extracted_data[i][2]
        day = day.replace(".", "")
        day = day.replace(",", "")
        day = day.replace("", "")
        print(line +". "+ month+" "+day)


get_inputs()
setup_flag_regs(numberofsentances)
extract_data(sentances)
outputs_print()

