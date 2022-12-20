class presence:
    presencsCount = 0

    def __init__(self,  name , Duration):
        self.name = name
        self.Duration = Duration
        presence.presencsCount += 1

    def displayCount(self):
        print("Total student  %d" % presence.presencsCount)

    def toString(self):
        print( ", Student name: ", self.name, " student Duration  : ", self.Duration)
