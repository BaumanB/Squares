class Screen:
    def __new__(cls, height, width):
        if (height < 1 or width < 1):
            return None
        return super().__new__(cls)

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.iteration_long_side = max(self.height, self.width)
        self.iteration_short_side = min(self.height, self.width)
        self.squares = {}
        self.num_of_squares = 0

    def find_next_square(self):
        if self.iteration_long_side < self.iteration_short_side : self.iteration_long_side, self.iteration_short_side = self.iteration_short_side, self.iteration_long_side

        if self.iteration_short_side == 0:
            return False

        if self.iteration_short_side in self.squares:
            self.squares[self.iteration_short_side] = self.squares[self.iteration_short_side] + 1
        else:
            self.squares[self.iteration_short_side] = 1
        self.iteration_long_side -= self.iteration_short_side

        return True

    def find_all_squares(self):
        while self.find_next_square():
            pass
        self.num_of_squares = sum(self.squares.values())

if __name__ == '__main__':
    pass
