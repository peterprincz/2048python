class square:
    def __init__(self):
        self.value = 0
        self.changed_this_turn = False

    def string_value(self):
        if self.value == 0:
            return "     "
        else:
            return "{:^5s}".format(str(self.value))

    def multiply(self):
        self.value *= 2
