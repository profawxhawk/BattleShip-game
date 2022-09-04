import math
import random
from models.Ship import Ship
class BattleField():
    def __init__(self,size):
        if size<=1:
            raise Exception("Size must be greater than 1")

        self.size = size
        self.grid = [[None for x in range(size+1)] for y in range(size+1)]
        self.shipSet = set()
        self.hitGridSet = set()

        self.playerShipCountMap = {
            1: 0,
            2: 0
        }

    def generate_random_cord(self,startx,starty,endx,endy):

        xcord = random.randint(startx, endx)
        ycord = random.randint(starty, endy)

        while((xcord,ycord) in self.hitGridSet):
            xcord = random.randint(startx, endx)
            ycord = random.randint(starty, endy)
        
        return xcord, ycord
    
    def fire_missile(self,player):
        if player==1:
            xcord, ycord = self.generate_random_cord(1,math.ceil(self.size/2),self.size,self.size)
        if player==2:
            xcord, ycord = self.generate_random_cord(1,1,self.size,math.floor(self.size/2))

        self.hitGridSet.add((xcord, ycord))

        return (xcord, ycord)

        

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

        ShipA =  Ship("A-" + code,size,playerAX,playerAY)
        
        for i in range(squareStartX,squareEndX):
            for j in range(squareStartY,squareEndY):
                self.grid[i][j] =ShipA

        (squareStartX,squareStartY,squareEndX,squareEndY) = self.get_start_and_end_cords(size,playerBX,playerBY)

        ShipB =  Ship("B-" + code,size,playerBX,playerBY)

        for i in range(squareStartX,squareEndX):
            for j in range(squareStartY,squareEndY):
                self.grid[i][j] = ShipB
        
        self.playerShipCountMap[1]+=1
        self.playerShipCountMap[2]+=1

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

    def start_game(self):
        playerTurn = 1
        while(self.playerShipCountMap[1]!=0 and self.playerShipCountMap[2]!=0):
            if playerTurn == 1:
                playerString = "Player A"
            else:
                playerString = "Player B"

            (xcord,ycord) = self.fire_missile(playerTurn)
            displayString = playerString+"\'s turn: Missile fired at ("+str(xcord)+","+str(ycord)+") : "
            hitAction = "Miss"
            shipName = ""
            if self.grid[xcord][ycord] !=  None:
                hitAction = "Hit"
                self.playerShipCountMap[3-playerTurn]-=1
                shipName = self.grid[xcord][ycord].name
                self.remove_ship(self.grid[xcord][ycord])

            if hitAction=="Miss":
                displayString += hitAction
            else:
                displayString += hitAction+" : " + shipName +" destroyed"

            displayString += " : Ships Remaining - PlayerA: "+  str(self.playerShipCountMap[1])+", PlayerB: "+  str(self.playerShipCountMap[2])
            print(displayString)
        
            playerTurn = 3 - playerTurn

        winner = "Player A"

        if(self.playerShipCountMap[1]==0):
            winner = "Player B"

        print("Game over."+winner+" wins")

    def remove_ship(self,ship):
        if not isinstance(ship,Ship):
            raise Exception("Provided object is not of type ship")

        (squareStartX,squareStartY,squareEndX,squareEndY) = self.get_start_and_end_cords(ship.size,ship.xcord,ship.ycord)
        for i in range(squareStartX,squareEndX):
            for j in range(squareStartY,squareEndY):
                self.grid[i][j]=None

