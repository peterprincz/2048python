import board as b 

class game:
    def __init__(self):
        self.game_board = b.board()

    def start_game(self):
        print("Welcome User, have fun")
        print("Controls:W,A,S,D")
        print("Endgame is not implemented yet!!!")
        self.game_board.increase_random_square()
        self.game_board.increase_random_square()
        self.game_board.print_table()
        while(True):
            for line in self.game_board.table:
                for square in line:
                    square.changed_this_turn = False
            try:
                direction = input("Give me input")
                if direction not in ["w", "s", "a", "d"]:
                    print("Invalid input")
                    continue
                if direction == "w":
                    self.game_board.move_squares_vertically("up")
                if direction == "s":
                    self.game_board.move_squares_vertically("down")
                if direction == "a":
                    self.game_board.move_squares_horizontically("left")
                if direction == "d":
                    self.game_board.move_squares_horizontically("right")
                self.game_board.increase_random_square()
            except ValueError:
                print("You cant move that direction now")
            self.game_board.print_table()