from board import Board
import sys
from car import Car
from helper import load_json

POSSIBLE_NAMES = ['Y', 'B', 'O', 'W', 'G', 'R']
VALID_DIRECTIONS = ['r', 'l', 'u', 'd']
LEGAL_LENGTH = [2, 3, 4]
HORIZONTAL = 0
VERTICAL = 1


class Game:
    """
    The game class, got turn func and the play fun,
    through this class you can play the game
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.working_board = board

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is not mandatory
        to implement it.

        The function runs one round of the game :
            1.print the game board,
             get user's input of: what color car to move, and what
             direction to move it.
            2. Check if the input is valid through checking_game_input func
            3. Try moving car according to user's input.

        """
        print(self.working_board.__str__())
        game_input = input("Car and direction please\n")
        while not (self.checking_game_input(game_input)):
            game_input = input("Valid car and direction please\n")
        car_name, car_dirc = game_input.split(',')
        self.working_board.move_car(car_name, car_dirc)
        # implement your code here (and then delete the next line - 'pass')

    def checking_game_input(self, game_input):
        """
        checking input inserted,
        return True if it valid False otherwise
        :param game_input:
        :return:
        """
        game_options = self.working_board.possible_moves()
        if len(game_input) != 3:
            return False
        if game_input[0] not in POSSIBLE_NAMES:
            print("Please choose valid names")
            print(game_board.possible_moves())
            return False
        if game_input[1] != ',':
            print("Wrong format arg")
            return False
        if game_input[2] not in VALID_DIRECTIONS:
            print("Please choose valid directions")
            return False
        if len(game_options)>0:
            for i in range(len(game_options)):
                if game_input[0]==game_options[i][0]:
                    if game_input[2]==game_options[i][1]:
                        return True
            print("Name and direction doesnt match")
            print(game_options)
            return False
        return True

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        end_game_co = game_board.target_location()
        while (game_board.working_board[end_game_co[0]][end_game_co[1]]
                                                                      == 'E'):
            Game.__single_turn(self)
        print(self.working_board.__str__())
        print("Game Won, life of programmer gone")
        return


def adding_valid_cars(dict_of_json, game_board):
    """
    Getting the Json file data, check if it valid
    if so adding the cars in it, while a car isn't valid
     prints the problem it got
    :param dict_of_json:
    :param game_board:
    :return:
    """
    for key, value in dict_of_json.items():
        if key in POSSIBLE_NAMES:
            if (len(value) != 3):
                print(key + " got not valid numbers of args")
            elif not (value[0] in LEGAL_LENGTH):
                print(key + " has no valid length")
            elif (len(value[1]) != 2):
                print(key + " location is wrong")
            elif (tuple([value[1][0], value[1][1]]) not
                                                 in game_board.cell_list()):
                print(key + " has no valid location")
            elif value[2] not in [HORIZONTAL, VERTICAL]:
                print(key + " has no valid direction")
            else:
                game_board.add_car(Car(key, value[0], tuple([value[1][0],
                                                 value[1][1]]), value[2]))
        else:
            print(key + " not a valid color")


if __name__ == "__main__":
    """
    main, load Json file, 
    creat board, add cars from
    json file to board and run the game
    """
    car_dict = load_json(sys.argv[1])
    game_board = Board()
    adding_valid_cars(car_dict, game_board)
    Game(game_board).play()
