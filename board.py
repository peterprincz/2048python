import square
import random

class board:
    def __init__(self):
        self.squares = [square.square() for x in range(16)]
        self.table = [
                        self.squares[0:4],
                        self.squares[4:8],
                        self.squares[8:12],
                        self.squares[12:16]
                     ]

    def print_table(self):
        print('\n' * 4)
        for line in self.table:
            for square in line:
                print("|" + square.string_value() + "|", end="")
            print("")
            print("_" * 12)

    def increase_random_square(self):
        empty_squares = [x for x in self.squares if x.value == 0]
        if len(empty_squares) == 0:
            raise Exception("GAME OVER")
        choosen_square = empty_squares[random.randrange(len(empty_squares))]
        choosen_square.value = 2

    def move_squares_horizontically(self, direction):
        moves = 0
        if direction not in ["left", "right"]:
            raise Exception("Invalid argument")
        if direction == "right":
            self.reverse_horizontally()
        for line in self.table:
            for x in range(1, 4):
                for y in range(x, 0, -1):
                    moving_square = line[y]
                    squate_to_the_left = line[y - 1]
                    if squate_to_the_left.value == 0:
                        squate_to_the_left.value = moving_square.value
                        moving_square.value = 0
                        moves += 1
                        continue
                    if squate_to_the_left.value == moving_square.value and \
                    squate_to_the_left.changed_this_turn is False and \
                    moving_square.changed_this_turn is False:
                        squate_to_the_left.multiply()
                        squate_to_the_left.changed_this_turn = True
                        moving_square.value = 0
                        moves += 1
                        continue
        if direction == "right":
            self.reverse_horizontally()
        if moves == 0:
            raise ValueError("Invalid move")


    def move_squares_vertically(self, direction):
        moves = 0
        if direction not in ["up", "down"]:
            raise Exception("Invalid parameteter")
        if direction == "up":
            rows = [
                [self.table[x][0] for x in range(4)],
                [self.table[x][1] for x in range(4)],
                [self.table[x][2] for x in range(4)],
                [self.table[x][3] for x in range(4)]
            ]
        else:
            rows = [
                [self.table[x][0] for x in range(3, -1, -1)],
                [self.table[x][1] for x in range(3, -1, -1)],
                [self.table[x][2] for x in range(3, -1, -1)],
                [self.table[x][3] for x in range(3, -1, -1)]
            ]
        for row in rows:
            for x in range(1, 4):
                for y in range(x, 0, -1):
                    moving_square = row[y]
                    squate_to_the_left = row[y - 1]
                    if squate_to_the_left.value == 0:
                        squate_to_the_left.value = moving_square.value
                        moving_square.value = 0
                        moves += 1
                        continue
                    if squate_to_the_left.value == moving_square.value and \
                    squate_to_the_left.changed_this_turn is False and \
                    moving_square.changed_this_turn is False:
                        squate_to_the_left.multiply()
                        squate_to_the_left.changed_this_turn = True
                        moving_square.value = 0
                        moves += 1
                        continue
        if moves == 0:
            raise ValueError("Invalid move")

    
    def reverse_horizontally(self):
        for line in self.table:
            line.reverse()

