__author__ = 'anton'


class Option:
    """
        Option
    """
    def __init__(self, name, criterions):
        self.name = name
        self.criterions = criterions
        self.distance_to_best = float('inf')
        self.distance_to_worst = 0
        self.relative_index = float('inf')

    def get_name(self):
        return self.name

    def sizeof_criterions(self):
        return len(self.criterions)

    def estimate(self, criterion, value, num=1):
        for crt in self.criterions:
            if crt.name == criterion:
                crt.estimate(value, num)

    def estimate_i(self, pos, value, num):
        if 0 <= pos < len(self.criterions):
            self.criterions[pos].estimate(value, num)

    def estimate_all(self, points):
        if len(points) == len(self.criterions):
            for i in range(0, len(points)):
                self.criterions[i].estimate(points[i])

    def distance_to_best(self):
        return self.distance_to_best

    def set_distance_to_best(self, best):
        self.distance_to_best = self.calc_distance_to(best)

    def distance_to_worst(self):
        return self.distance_to_worst

    def set_distance_to_worst(self, worst):
        self.distance_to_worst = self.calc_distance_to(worst)

    def get_criterions(self):
        return self.criterions

    def calc_distance_to(self, other):
        res = 0
        for (a, b) in zip(self.criterions, other.get_criterions()):
            tmp = 0
            for key in a.get_scales().keys():
                tmp += abs(a.get_scales()[key] - b.get_scales()[key])
            res += a.get_weight() * tmp;
        return res

    def cal_relative_index(self):
        self.relative_index = self.distance_to_best / (self.distance_to_best + self.distance_to_worst)

    def get_relative_index(self):
        return self.relative_index