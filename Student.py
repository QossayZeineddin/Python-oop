class student:
    studentCount = 0
    def __init__(self, id, name ):
        self.id = id
        self.name = name

        student.studentCount += 1

    def displayCount(self):
        print("Total student  %d" % student.studentCount)

    def toString(self):
        print(" student ID  : ", self.id, ", Student name: ", self.name)
        