class Calendar:
    def __init__(self, year, firstDay):
        self.year = year
        self.first = firstDay
        self.day = self.createDays()

        self.data = self.createAll()
        self.dataReversed = self.createDate1(self.data)
        self.dayName = ['Mo', 'Tu', 'W', 'Th', 'F', 'S', 'Su']
        self.months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    def createDays(self):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            days[1] = 29
        self.day = days
        return self.day
    def createDate(self, i, j, L):
        self.data = L
        if i<9:
            if j<9:
                date = str(0) + str(j+1) + str(0) + str(i+1) + str(self.year)
                #[13, 1, 2021]
                L.append(date)
            else:
                date = str(j+1) + str(0) + str(i+1) + str(self.year)
                L.append(date)
        elif i>=9:
            if j<9:
                date = str(0) + str(j+1) + str(i+1) + str(self.year)
                L.append(date)
            else:
                date = str(j+1) + str(i+1) + str(self.year)
                L.append(date)
        self.data = L
        return self
    def createAll(self):
        data = []
        for i in range(12):
            for j in range(self.day[i]):
                self.createDate(i, j, data)
        return self.data
    def createDate1(self, L):
        self.dataRev = []
        for date in L:
            day = date[0] + date[1]
            month = date[2] + date[3]
            year = date[4] + date[5] + date[6] + date[7]
            dateR = str(year) + str(month) + str(day)
            ## dataRev is th matrix [2020113, , ...]
            self.dataRev.append(dateR)
            ## dataFormat is the matrix [Wed1Jan2020, Thi2Jan]
        return self