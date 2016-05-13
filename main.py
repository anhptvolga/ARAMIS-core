import sys
import copy
from criterion import *
from option import *


__author__ = 'anton'

criterions = list()
amount_experts = 0
options = list()


def read_file_input(filename, type = 1):
    with open(filename, "r") as file:
        # criterions = list()
        sum_weight = 0
        # read each criterion
        for i in range(0, int(file.readline())):
            name = file.readline().strip()
            weight = eval(file.readline())
            sum_weight += weight
            scales = list()
            line = file.readline().strip()
            if line[0] != '[' or line[-1] != ']':
                while line:
                    scales.append(line)
                    line = file.readline().strip()
            else:   # integer range benmark
                line = eval(line)
                scales = [i for i in range(line[1], line[0]-1, -1)]
                file.readline()  # read empty line
            criterions.append(Criterion(name, scales, weight))
        # recalculate weight of each criterion (sum = 1)
        tmp = 0
        for crt in criterions[:-1]:
            tmp += crt.get_weight() / sum_weight
            crt.set_weight(crt.get_weight() / sum_weight)
        criterions[-1].set_weight(1-tmp)
        if type == '1':
            read_benmark1(file)
        else:
            read_benmark2(file)


def read_benmark1(file):
        # read objects
        global amount_experts
        amount_experts = int(file.readline())
        # read options = list()
        for i in range(0, int(file.readline().strip())):
            name = file.readline().strip()
            options.append(Option(name, copy.deepcopy(criterions)))
            # read point for each option
            line = file.readline().strip()
            while line:
                line = line.split('.')
                options[-1].estimate(line[0].strip(), line[1].strip(), int(line[2].strip()))
                line = file.readline().strip()
    # print('read done')
    # return (criterions, amount_experts, options)


def read_benmark2(file):
    # number of expert
    global amount_experts
    amount_experts = int(file.readline())

    # options's names
    line = file.readline().split('.')
    for op in line:
        options.append(Option(op.strip(), copy.deepcopy(criterions)))
    # read each expert's benmark table (for each options)
    amount_options = len(line)
    for i in range(amount_experts):
        file.readline()
        for j in range(amount_options):
            line = list(map(lambda x: x.strip(), file.readline().split('.')))
            options[j].estimate_all(line)


def cal_the_best():
    # create the best option
    the_best = Option('The Best', copy.deepcopy(criterions))
    for i in range(the_best.sizeof_criterions()):
        the_best.estimate_i(i, criterions[i].first_scale(), amount_experts)
    return the_best


def cal_the_worst():
    # create the worst option
    the_worst = Option('The Wordst', copy.deepcopy(criterions))
    for i in range(the_worst.sizeof_criterions()):
        the_worst.estimate_i(i, criterions[i].last_scale(), amount_experts)
    return the_worst


if __name__ == '__main__':
    if len(sys.argv) == 3:
        # criterions, amount_experts, options = read_file_input('input.txt')
        read_file_input(sys.argv[1], sys.argv[2])
        the_best = cal_the_best()
        the_worst = cal_the_worst()

        res_option = options[0]
        for opt in options:
            opt.set_distance_to_best(the_best)
            opt.set_distance_to_worst(the_worst)
            opt.cal_relative_index()
            if opt.get_relative_index() < res_option.get_relative_index():
                res_option = opt
            # print(opt.name, " --- %0.3f\t%0.3f\t%0.3f"%(opt.distance_to_best, opt.distance_to_worst, opt.get_relative_index()))
        options.sort(key = lambda k: k.get_relative_index())
        print('------ sorted -----')
        for opt in options:
            print(opt.get_name(), '\t--\t%0.3f'%opt.get_relative_index())
        print(' --------- the best option:', res_option.get_name(), '-----------')
    else:
        print('Call main.py file_input input_way(1 or 2)')
