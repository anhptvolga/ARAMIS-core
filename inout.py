__author__ = 'anton'

from criterion import *

def read_file_input(file_name):
    file = open(file_name, "r")
    
    num_criterion = eval(file.readline())
    print('num of criterion = ', num_criterion)
    criterions = list()
    # read each criterion
    for i in range(0, num_criterion):
        name = file.readline()
        weight = eval(file.readliine())
        num_scales = eval(file.readline())
        scales = list()
        for j in range(0, num_scales):
            scales.append(file.readline())
        criterions.append(Criterion(name, weight, scales))

    # read objects
    num_object, num_expert = map(eval, file.readline().split())
    for i in range(0, num_object):
        pass
    file.close()
