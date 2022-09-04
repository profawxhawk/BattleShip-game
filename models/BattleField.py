from models.Ship import Ship
import math
class BattleField():
    def __init__(self,size):
        if size<=1:
            raise Exception("Size must be greater than 1")

        self.size = size
        self.grid = [[None for x in range(size+1)] for y in range(size+1)]
        self.shipSet = set()

    def check_grid_boundary(self,x,y,player):
        if player==1:
            return not (x<1 or y<1 or x>self.size or y>self.size/2)
        if player==2:
            return not (x<1 or y<=self.size/2 or x>self.size or y>self.size)

        return True

    def get_start_and_end_cords(self,size,xcord,ycord):
        squareStartX = math.ceil(xcord-(size/2))
        squareStartY = math.ceil(ycord-(size/2))

        squareEndX = squareStartX + size
        squareEndY = squareStartY + size

        return (squareStartX,squareStartY,squareEndX,squareEndY)

    def check_if_ship_can_be_placed(self,size,xcord,ycord,player):
        (squareStartX,squareStartY,squareEndX,squareEndY) = self.get_start_and_end_cords(size,xcord,ycord)
        if not self.check_grid_boundary(squareStartX,squareStartY,player) or not self.check_grid_boundary(squareEndX,squareEndY,player):
            return False
        
        for i in range(squareStartX,squareEndX):
            for j in range(squareStartY,squareEndY):
                if self.grid[i][j]!=None:
                    return False
        
        return True

    def placeShip(self,code,size,playerAX,playerAY,playerBX,playerBY):
        checkACords = self.check_if_ship_can_be_placed(size,playerAX, playerAY,1)
        if not checkACords:
            print("Invalid coordinates for player A")
            return False
        
        checkBCords = self.check_if_ship_can_be_placed(size,playerBX, playerBY,2)
        if not checkBCords:
            print("Invalid coordinates for player B")
            return False

        (squareStartX,squareStartY,squareEndX,squareEndY) = self.get_start_and_end_cords(size,playerAX,playerAY)

        for i in range(squareStartX,squareEndX):
            for j in range(squareStartY,squareEndY):
                self.grid[i][j] = Ship("A-" + code)

        (squareStartX,squareStartY,squareEndX,squareEndY) = self.get_start_and_end_cords(size,playerBX,playerBY)

        for i in range(squareStartX,squareEndX):
            for j in range(squareStartY,squareEndY):
                self.grid[i][j] =  Ship("B-" + code)
        
        self.shipSet.add(code)
        return True
        
    #source: https://stackoverflow.com/questions/60842728/developing-a-function-to-print-a-grid-in-python
    def display_grid(self):
        print(((self.size)*7+7)*"-")
        for i in range(self.size):
            for j in range(self.size):
                value = ' '*5
                if isinstance(self.grid[i][j],Ship):
                    value = self.grid[i][j].name
                print(f"| {value} ", end='')
            print("| ")
            print(((self.size)*7+7)*"-")
