report_file = open("input.txt")
report_raw = report_file.read()
report_file.close()
report = report_raw.split("\n")

'''
Converts a string containing a command, to a list consisting of
direction (string) and number of steps to take in that direction (integer)
'''
def getCommand(str):
    size = len(str)
    direction = str[:size-2]
    steps = int(str[-1])
    return [direction, steps]

'''
Calculates horizontal position and depth with regards to input
'''
def calculatePosition(lst):
    horizontal = 0
    depth = 0
    for i in range(len(lst)):
        direction = getCommand(lst[i])[0]
        steps = getCommand(lst[i])[1]
        if direction == "forward":
            horizontal = horizontal + steps
        elif direction == "down":
            depth = depth + steps
        elif direction == "up":
            depth = depth - steps
    
    return [horizontal, depth]

'''
Calculates horizontal position, depth and aim with regards to input
'''
def calculatePositionAim(lst):
    horizontal = 0
    depth = 0
    aim = 0
    for i in range(len(lst)):
        direction = getCommand(lst[i])[0]
        steps = getCommand(lst[i])[1]
        if direction == "forward":
            horizontal = horizontal + steps
            depth = depth + (aim * steps)
        elif direction == "down":
            aim = aim + steps
        elif direction == "up":
            aim = aim - steps
    return [horizontal, depth]
