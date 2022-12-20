class resenceReport:
    def __init__(self, id, name , x1,x2,x3,x4,x5,x6):
        self.id = id
        self.name = name
        self.x1 =x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.x5 = x5
        self.x6 = x6



    def toString(self):
        print(" student ID  : ", self.id, ", Student name: ", self.name)