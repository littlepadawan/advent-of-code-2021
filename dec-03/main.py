gamma_bin = None
gamma_dec = None

epsilon_bin = None
epsilon_dec = None

oxygen_bin = None
oxygen_dec = None

CO2_bin = None
CO2_dec = None

power_consumption = None
life_support = None

# Get puzzle input
report_file = open('input.txt')
report_raw = report_file.read()
report_file.close()

def toInt(lst):
    new_list = []
    for x in lst:
        new_list.append(int(x))
    return new_list

report = report_raw.split('\n')


# Find the most common bit in given position
def mostCommonBit(lst, position):
    one = 0
    zero = 0
    for element in range(len(lst)):
        if lst[element][position] == '1':
            one = one + 1
        elif lst[element][position] == '0':
            zero = zero + 1
    if one > zero or one == zero:
         return '1'
    else:
        return '0'
    
# Determine a specific rate according to given report and
# rate = 'gamma' or 'epsilon'
def generateRate(lst, rate):
    position = 0
    rate_binary= ''
    if rate == 'gamma':
        for element in range(len(lst[0])):
            rate_binary = rate_binary + mostCommonBit(lst, position)
            position = position + 1
        return rate_binary
    elif rate == 'epsilon':
        for element in range(len(lst[0])):
            least_common = ''
            if mostCommonBit(lst, position) == '1':
                least_common = '0'
            else:
                least_common = '1'
            rate_binary = rate_binary + least_common
            position = position + 1
        return rate_binary

# Helper function to filterReport 
def filterReportAux(lst, position, filtr):
    filtered_lst = []
    for x in range(len(lst)):
        if lst[x][position] == filtr:
            filtered_lst.append(lst[x])
    return filtered_lst


def filterReport(lst, rating):
    if rating == 'oxygen':
        # Filter given list based upon most common number in first position
        filtered_lst = filterReportAux(lst, 0, generateRate(lst, 'gamma')[0])
        for x in range(1, len(lst[0])):
            if len(filtered_lst) > 1:
                filtered_lst = filterReportAux(filtered_lst, x, generateRate(filtered_lst, 'gamma')[x])
            else:
                return filtered_lst[0]
        return filtered_lst[0]
        
    elif rating == 'CO2':
        # Filter given list based upon most common number in first position
        filtered_lst = filterReportAux(lst, 0, generateRate(lst, 'epsilon')[0])
        for x in range(1, len(lst[0])):
            if len(filtered_lst) > 1:
                filtered_lst = filterReportAux(filtered_lst, x, generateRate(filtered_lst, 'epsilon')[x])
            else:
                return filtered_lst[0]
        return filtered_lst[0]

# Determine gamma rate as binary and decimal number
gamma_bin = generateRate(report, 'gamma')
gamma_dec = int(gamma_bin, 2)

# Determine epsilon rate as binary and decimal number
epsilon_bin = generateRate(report, 'epsilon')
epsilon_dec = int(epsilon_bin, 2)

# Determine oxygen generator rating
oxygen_bin = filterReport(report, 'oxygen')
oxygen_dec = int(oxygen_bin, 2)

# Determine CO2 scrubber rating
CO2_bin = filterReport(report, 'CO2')
CO2__dec = int(CO2_bin, 2)

# Calculate power consumtion
power_consumption = gamma_dec * epsilon_dec

# Calculate life support rating
life_support = oxygen_dec * CO2_dec