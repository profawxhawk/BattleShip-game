class Ship():
    def __init__(self, code,size,xcord,ycord):
        self.name =  code
        self.size = size
        self.xcord = xcord
        self.ycord = ycord
    def __str__(self):
        print(self.name)