class chatReport:
    def __init__(self, id, name , y1,y2,y3,y4,y5,y6):
        self.id = id
        self.name = name
        self.y1 =y1
        self.y2 = y2
        self.y3 = y3
        self.y4 = y4
        self.y5 = y5
        self.y6 = y6



    def toString(self):
        print(" student ID  : ", self.id, ", Student name: ", self.name)