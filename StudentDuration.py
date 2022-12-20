class studentDuration:

    studentduration = 0

    def __init__(self, id, name, d1,d2,d3,d4,d5,d6):
        self.id = id
        self.name = name
        self.d1=d1
        self.d2 = d2
        self.d3 = d3
        self.d4 = d4
        self.d5 = d5
        self.d6 = d6
        studentDuration.studentduration += 1

    def displayCount(self):
        print("Total student  %d" % studentDuration.studentDuration)

    def toString(self):
        print(" student ID  : ", self.id, ", Student name: ", self.name)
