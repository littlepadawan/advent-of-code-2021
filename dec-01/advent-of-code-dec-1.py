report_file = open("input.txt")
report_raw = report_file.read()
report_file.close()

def toInt(lst):
    new_list = []
    for x in lst:
        new_list.append(int(x))
    return new_list

report = toInt(report_raw.split("\n"))

def countIncrease(lst):
    increases = 0
    len_lst = len(lst)
    for i in range(len_lst):
        if i < (len_lst-1):
            if lst[i] < lst[i+1]:
                increases = increases + 1
    return increases

def countIncrease3(lst):
    increases = 0
    len_lst = len(lst)
    for i in range(len_lst):
        if i < (len_lst-3):
            fst_window = lst[i] + lst[i+1] + lst[i+2]
            scnd_window = lst[i+1] + lst[i+2] + lst[i+3]
            if fst_window < scnd_window:
                increases = increases + 1
    return increases
