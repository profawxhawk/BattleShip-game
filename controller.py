from models.BattleField import BattleField
import utils

class Controller():
    def __init__(self):
        self.menuMap = {
            '1' :   self.init_game_handler,
            '2' :   self.add_ship_handler,
            '3' :   self.view_battle_field_handler,
            '4' :   self.start_game_handler
        }

    def check_if_game_initialized(self):
        if not hasattr(self, 'battleship'):
            print("Game is not initialized")
            return False
        return True

    def display_menu(self):
        if not hasattr(self, 'battleship'):
            print("1) Initialize game")
        else:
            print("1) Re-initialize game")
            print("2) Add ship")
            print("3) View battle field")
            print("4) Start game")

    def handle_user_input(self, handlerString):
        if handlerString not in self.menuMap.keys():
            raise Exception("Unknown functionality provided")
        
        if not callable(self.menuMap[handlerString]):
            raise Exception("No handler found for the given function")
        
        self.menuMap[handlerString]()

        return self.end_game_decider(handlerString)


    def end_game_decider(self,handlerString):
        return handlerString=='4'

    def init_game_handler(self):

        print("Please enter the size of the battleship grid")
        size = utils.get_integer_input()

        self.battleship =  BattleField(size)
        print('BattleShip game started successfully')

    def add_ship_handler(self):
        gameInitCheck = self.check_if_game_initialized()
        if not gameInitCheck:
            return

        print("Please enter the code for the ship")
        code = input()

        if code in self.battleship.shipSet:
            print("Ship code already exists")
        
        print("Please enter the size of the ship")
        size = utils.get_integer_input()

        print("Please enter the x cordinate for player A")
        playerAX = utils.get_integer_input()

        print("Please enter the y cordinate for player A")
        playerAY = utils.get_integer_input()

        print("Please enter the x cordinate for player B")
        playerBX = utils.get_integer_input()

        print("Please enter the y cordinate for player B")
        playerBY = utils.get_integer_input()

        ok = self.battleship.placeShip(code,size,playerAX,playerAY,playerBX,playerBY)
        if not ok:
            print("Ship creation failed")

        print("Ship added successfully")

    def view_battle_field_handler(self):
        gameInitCheck = self.check_if_game_initialized()
        if not gameInitCheck:
            return

        self.battleship.display_grid()

    def start_game_handler(self):
        pass
