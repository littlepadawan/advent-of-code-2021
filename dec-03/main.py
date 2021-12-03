gamma_bin = None
gamma_dec = None

epsilon_bin = None
gamma_dec = None

power_consumption = None

report_file = open('input.txt')
report_raw = report_file.read()
report_file.close()

def toInt(lst):
    new_list = []
    for x in lst:
        new_list.append(int(x))
    return new_list

report = report_raw.split('\n')


# Finds the most common bit in given position
def mostCommonBit(lst, position):
    one = 0
    zero = 0
    for element in range(len(lst)):
        if lst[element][position] == '1':
            one = one + 1
        elif lst[element][position] == '0':
            zero = zero + 1
    if one > zero:
         return '1'
    else:
        return '0'


# Finds the least common bit in given position
def leastCommonBit(lst, position):
    one = 0
    zero = 0
    for element in range(len(lst)):
        if lst[element][position] == '1':
            one = one + 1
        elif lst[element][position] == '0':
            zero = zero + 1
    if one < zero:
        return '1'
    else:
        return '0'
    

# Determine a specific rate according to given report and
# rate = specific rate to determine as a string ('gamma' or 'epsilon')
def generateRate(lst, rate):
    position = 0
    new_binary= ''
    if rate == 'gamma':
        for element in range(len(lst[0])):
            new_binary = new_binary + mostCommonBit(lst, position)
            position = position + 1
        return new_binary
    elif rate == 'epsilon':
        for element in range(len(lst[0])):
            new_binary = new_binary + leastCommonBit(lst, position)
            position = position + 1
        return new_binary


                  


# Determine gamma rate as binary and decimal number
gamma_bin = generateRate(report, 'gamma')
gamma_dec = int(gamma_bin, 2)

# Determine epsilon rate as binary and decimal number
epsilon_bin = generateRate(report, 'epsilon')
epsilon_dec = int(epsilon_bin, 2)

# Calculate power consumtion
power_consumption = gamma_dec * epsilon_dec
