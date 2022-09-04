from controller import Controller

stopGame = False

gameController = Controller()
print("Welcome to the game of BattleShip! Please enter your choice")

while(not stopGame):
    gameController.display_menu()
    handler = input()
    stopGame = gameController.handle_user_input(handler)