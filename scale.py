__author__ = 'anton'


class Scale:
    """
        Scale for each criterion
    """

    def __int__(self, size):
        self.values = []

    def add(self, value):
        self.values.append(value)
