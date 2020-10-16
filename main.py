from Calendar import Calendar
k = 0
self = Calendar(2021, 'F')

calOrdinary = self.createAll()
calReversed = self.createDate1(calOrdinary)

print(calOrdinary)
print(calReversed)

'''dataRev = []
dates1 = createDate1(data)

def createDate2(L):
    for date in L:
        L.append(str(date[0]) + str(date[1]+1) + str(date[2]) + str(date[3]))
    return L
createDate2(dates1)
for date in dates1:
    dataFormat.append(str(date[0]) + str(date[1]+1) + str(date[2]) + str(date[3]))

def printD(L, M):
    b = self.day
    for j in b:
        S = range(j)
        for i in S:
            print(L[i])
    print(M)

printD(dates1, data)'''