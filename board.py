POSSIBLE_DIRECTIONS = ['r', 'l', 'u', 'd']


class Board:
    """
    Board of the game,
    this case board is 7*7 and exit is on (3,7)co.
    gets orders from Game and command on Car class
    """

    def __init__(self):
        """
        Initialize a new Board object.
        """
        self.car_lst = []
        self.working_board = []
        for i in range(7):  # create a list with nested lists
            self.working_board.append([])
            for n in range(7):
                self.working_board[i].append("_")
                if (i == 3 and n == 6):
                    self.working_board[i].append("E")

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        copy_board = self.working_board[:]
        copy_board = '\n'.join(str(v) for v in copy_board)
        return copy_board

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        # In this board, returns a list containing the cells in the square
        # from (0,0) to (6,6) and the target cell (3,7)
        lst = []
        for i in range(len(self.working_board)):
            for j in range(len(self.working_board[i])):
                lst.append(tuple([i, j]))
        return lst

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description)
                 representing legal moves
        """
        cell_lst = self.cell_list()
        lst = []
        for i in range(len(self.car_lst)):
            car_name = self.car_lst[i].get_name()
            for j in range(len(POSSIBLE_DIRECTIONS)):
                move_req = self.car_lst[i].movement_requirements(
                                            POSSIBLE_DIRECTIONS[j])
                if (len(move_req)>0 and
                    move_req[0] in cell_lst and
                    self.cell_content(move_req[0])==None):
                        lst.append(tuple([car_name, POSSIBLE_DIRECTIONS[j],
                                        self.car_lst[i].possible_moves()]))
        return lst

    def target_location(self):
        """
        This function returns the coordinates of the location
         which is to be filled for victory.
        :return: (row,col) of goal location
        """
        # In this board, returns (3,7)
        return (3, 7)

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        if (self.working_board[coordinate[0]][coordinate[1]] == '_' or
                self.working_board[coordinate[0]][coordinate[1]] == 'E'):
            return None
        return self.working_board[coordinate[0]][coordinate[1]]

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        co_of_car = car.car_coordinates()
        cell_lst = self.cell_list()
        endgame_co = Board.target_location(self)
        for i in range(len(co_of_car)):
            if (co_of_car[i] not in cell_lst):
                return False
            for j in range(len(self.car_lst)):
                if (not car.get_name() == self.car_lst[j].get_name()):
                    if (co_of_car[i] in
                                        self.car_lst[j].car_coordinates()):
                        return False
                else:
                    if (car != self.car_lst[j]):
                        return False
        if (endgame_co in co_of_car):
            self.working_board[endgame_co[0]][endgame_co[1]] = car.get_name()
        for i in range(len(self.working_board)): #cleaning the board from name
            for j in range(len(self.working_board[i])):
                if self.working_board[i][j] == car.get_name():
                    self.working_board[i][j] = '_'
        for i in range(car.length):  ##moving the car
            self.working_board[co_of_car[i][0]][co_of_car[i][1]] \
                                                    = car.get_name()
        self.car_lst.append(car)
        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        for i in range(len(self.car_lst)):
            if self.car_lst[i].get_name() == name:
                coordinats = self.car_lst[i].movement_requirements(movekey)
                if (len(coordinats) > 0 and coordinats[0] in
                                                        self.cell_list()):
                    if (self.working_board[coordinats[0][0]][coordinats[0][1]]
                                                                        == '_'
                        or self.working_board[coordinats[0][0]]
                                                    [coordinats[0][1]] == 'E'):
                        if self.car_lst[i].move(movekey):
                            Board.add_car(self, self.car_lst[i])
                            return True
        return False
