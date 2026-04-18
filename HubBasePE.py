def ProgrammP1():  #T1
    import random  #(19.03.2026)

    def Drift():  #(19.03.2026)
        global x, y, z, a
        a = max((y-y*2)*2,z)
        y = random.randint(min(a,y*2),max(a,y*2))
        if y == 0:
            y = 1
        x = x + y

    def Drift2():  #(19.03.2026)
        global i, o, r, p
        p = max((o-o*2)*2,r)
        o = random.randint(min(p,o*2),max(p,o*2))
        if o == 0:
            o = 1
        i = i + o

    def ProgrammP1E1():  #(19.03.2026)
        global x, y, i, o, z, r
        Goal =  float(input("Set a goal -- "))
        x = int(input("First S.N. -- "))
        y = int(input("First D.N. -- "))
        i = int(input("Second S.N. -- "))
        o = int(input("Second D.N. -- "))
        z = 1
        r = 1
        Opr = 1
        while True:
            Drift()
            Drift2()
            print(x)
            print(i)
            if x > Goal or i > Goal:
                if x > Goal:
                    z = -random.randint(1,max(1,y))
                if i > Goal:
                    r = -random.randint(1,max(1,o))
            if x < Goal or i < Goal:
                if x < Goal:
                    z = random.randint(1,max(1,y))
                if i < Goal:
                    r = random.randint(1,max(1,o))
            if x == Goal or i == Goal:  #(20.03.2026)
                if x == Goal:
                    print("First D reached the goal")
                if i == Goal:
                    print("Second D reached the goal")
                break
            Opr = Opr + 1
            if Opr >= 10000:
                print("Fail")
                break

    ProgrammP1E1()  #(19.03.2026)

def ProgrammP2():  #T3
    WordLib = ["hi"]
    ES = input("The string that you want to encrypt -- ").split()
    if WordLib != []:
        print("Currently the words are:")
        for Cyc2 in WordLib:
            print(Cyc2)
    Do1 = input("Do you want to add new words?[Y/N] -- ").upper()
    if Do1 == "Y":
        Count = input("How many? -- ")
        for Cyc1 in range(int(Count)):
            NewWord = [str(input("The word? -- "))]
            WordLib = WordLib + NewWord
            NewWord = []
    for Cyc3 in ES:
        if Cyc3 in WordLib:
            pass
        else:
            NewESWord = [Cyc3]
            WordLib = WordLib + NewESWord
            NewESWord = []
    WordLibP = WordLib
    WordLib = WordLib * 2
    CES = []
    for Cyc3 in ES:
        Index = WordLib.index(Cyc3)
        Index = [WordLib[Index + 2]]
        CES = CES + Index
    CESP = ""
    for l in CES:
        CESP = CESP + l + " "
    print(CESP)

def CTNP():  #Mainline
    Cstate = input("Continue[Y/N]").upper()
    if Cstate == "Y":
        Cstate = 1
    elif Cstate == "N":
        Cstate = 0
    else:
        print("Choose properly!")
        Cstate = 2
    if Cstate == 1:
        Advance()
    else:
        print("Bye")
        PStop()

def Advance():  #Mainline
    Adv = 1
    global Stop
    Stop = 0

def PStop():  #Mainline
    global Stop
    Stop = 1

def Start():
    ProgrammP1()
    CTNP()
    if Stop == 1:
        pass
    else:
        ProgrammP2()

Start()