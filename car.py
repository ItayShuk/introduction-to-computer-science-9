HORIZONTAL = 1
VERTICAL = 0


class Car:
    """
    Car class, get command from Board
    creating cars and changing them
    """

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col)
            location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self.name = name
        self.length = length
        self.location = location
        self.orientation = orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        coordinates = []
        row = self.location[0]
        col = self.location[1]
        if (self.orientation == HORIZONTAL):
            for i in range(self.length):
                coordinates.append(tuple([row, col + i]))
        else:
            for i in range(self.length):
                coordinates.append(tuple([row + i, col]))
        return coordinates[:]

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements
            permitted by this car.
        """
        if self.orientation == HORIZONTAL:
            return {'r': 'Car goes right', 'l': 'Car goes left'}
        return {'u': 'Car goes up', 'd': 'Car goes down'}

    def movement_requirements(self, movekey):
        """
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order
                    for this move to be legal.
        """
        front = self.car_coordinates()[self.length - 1]
        back = self.location
        if self.orientation == HORIZONTAL:
            if movekey == 'r':
                return [(tuple([front[0], front[1] + 1]))]
            if movekey == 'l':
                return [(tuple([back[0], back[1] - 1]))]
        if self.orientation == VERTICAL:
            if movekey == 'd':
                return [(tuple([front[0] + 1, front[1]]))]
            if movekey == 'u':
                return [(tuple([back[0] - 1, back[1]]))]
        return []

    def move(self, movekey):
        """
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        coordinates = list(self.location)

        if (self.orientation == HORIZONTAL):
            if (movekey in ['u', 'd']):
                return False
            if (movekey == 'r'):
                coordinates[1] += 1
                self.location = tuple(coordinates)
                return True
            if (movekey == 'l'):
                coordinates[1] -= 1
                self.location = tuple(coordinates)
                return True

        if (self.orientation == VERTICAL):
            if (movekey in ['r', 'l']):
                return False
            if (movekey == 'd'):
                coordinates[0] += 1
                self.location = tuple(coordinates)
                return True
            if (movekey == 'u'):
                coordinates[0] -= 1
                self.location = tuple(coordinates)
                return True

        return False

    def get_name(self):
        """
        :return: The name of this car.
        """
        # implement your code and erase the "pass"
        name = self.name
        return name
