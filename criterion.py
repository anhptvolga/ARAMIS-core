__author__ = 'anton'

# from scale import *
from collections import OrderedDict


class Criterion:
    """
        Criterion
    """
    def __init__(self, name, scales, weight=0,):
        self.name = name
        self.weight = weight
        self.scales = OrderedDict(zip(scales, [0]*len(scales)))

    def set_weight(self, value):
        self.weight = value

    def get_weight(self):
        return self.weight

    def add_scale(self, scale):
        self.scales[scale] = 0

    def get_scales(self):
        return self.scales

    def estimate(self, scale, value=1):
        try:
            if isinstance(scale, str):
                scale = eval(scale)
        except Exception:
            pass
        if scale in self.scales:
            self.scales[scale] += value

    def size(self):
        return len(self.scales)

    def first_scale(self):
        return list(self.scales.keys())[0]

    def last_scale(self):
        return list(self.scales.keys())[-1]
