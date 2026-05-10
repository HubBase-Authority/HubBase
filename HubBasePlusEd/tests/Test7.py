import time

def ProgrammP4():
    print("HB-JS python port 0.0.1.0.00")
    time.sleep(1)


    def JSProgramm1(repeats):
        for i in range(repeats):
            print(str(i)+". =^.^=")

    def JSProgramm2():
        SecInMin = 60
        MinInHour = 60
        SecInHour = SecInMin * MinInHour
        HourInDay = 24
        SecInDay = SecInHour * HourInDay
        MinInDay = MinInHour * HourInDay
        DayInWeek = 7
        SecInWeek = SecInDay * DayInWeek
        MinInWeek = MinInDay * DayInWeek
        HourInWeek = HourInDay * DayInWeek
        DayInYear = 365
        SecInYear = SecInDay * DayInYear
        MinInYear = MinInDay * DayInYear
        HourInYear = HourInDay * DayInYear
        currentYear = 2026
        print("There are " + str(SecInMin) + " seconds in a minute")
        print("There are " + str(MinInHour) + " minutes in an hour")
        print("There are " + str(SecInHour) + " seconds in an hour")
        print("There are " + str(HourInDay) + " hours in a day")
        print("There are " + str(SecInDay) + " seconds in a day")
        print("There are " + str(MinInDay) + " minutes in a day")
        print("There are " + str(DayInWeek) + " days in a week")
        print("There are " + str(SecInWeek) + " seconds in a week")
        print("There are " + str(MinInWeek) + " minutes in a week")
        print("There are " + str(HourInWeek) + " hours in a week")
        print("There are " + str(DayInYear) + " days in a year")
        print("There are " + str(SecInYear) + " seconds in a year")
        print("There are " + str(MinInYear) + " minutes in a year")
        print("There are " + str(HourInYear) + " hours in a year")
        print("I am aproximately " + str(((currentYear - 2014) * SecInYear)) + " seconds old")

    def JSProgramm3():
        HighFives = 0
        print(HighFives+1)
        print(HighFives+1)
        print(HighFives-1)
        print("Delayed:")
        print(HighFives)
        print(HighFives+1)
        print(HighFives+1)
        print(HighFives-1)

    print("Programm1:")
    JSProgramm1(10)
    time.sleep(1)
    print("Programm2:")
    JSProgramm2()
    time.sleep(1)
    print("Programm3:")
    JSProgramm3()
    time.sleep(1)

ProgrammP4()