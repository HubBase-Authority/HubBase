import time  #(16.03.2026)
import random
from turtle import *

def Enter():  #(13.03.2026)
    VN = "a9.0.2"
    global VipAccess, PassGuess, AdminAccess
    VipAccess = "F"
    Password = str(1041)
    PassGuess = 0
    print("--- HubBase "+VN+" (default, Apr 19 2026, 18:41:07) ---")
    while PassGuess != Password:
        Num = input("Number = ")
        Num2 = input("Number2 = ")
        PassGuess = Num + Num2
        if PassGuess == str(5280):
            print("--Vip level access awarded--")
            print("Pass = 1041")
            VipAccess = "T"
            PassGuess = str(1041)
        if PassGuess == "A52-80A":
            print("--Welcome, Mark--")
            VipAccess = "T"
            AdminAccess = "T"
            PassGuess = str(1041)
        if PassGuess != Password:
            print("Incorrect")
    print("Correct")
    if VipAccess == "T":
        PassGuess = str(5280)

def Programm1():  #(15.03.2026)
    print("Hello world")

def Programm2():  #(15.03.2026)
    Num = input("Number = ")
    Num2 = input("Number2 = ")
    num = int(Num)
    num2 = int(Num2)
    print(num+num2)
    print(num-num2)
    print(num*num2)
    print(num**num2)
    print(num/num2)
    print(num//num2)
    print(num%num2)

def Programm3():  #(15.03.2026)
    Bananas = input("Bananas = ")
    BananasEaten = input("Bananas Eaten = ")
    print(int(Bananas)-int(BananasEaten))

def Programm4():  #(15.03.2026)
    Uname = input("What is your name? -- ")
    print("Create a character")
    Cname = input("What is his name? -- ")
    Cage = input("What is his age? -- ")
    Cpower = input("What are his powers? -- ")
    Cweak = input("What are his weaknesses? -- ")
    print("His name is", Cname)
    print("He is", Cage, "years old")
    print("Powers:", Cpower)
    print("Weaknesses:", Cweak)
    print('"'+"Thanks for creating me,", Uname+'"',"- says", Cname)

def Programm5():  #(15.03.2026)
    User_reply = input("Do you like robots? -- ").upper()
    if User_reply == "YES":
        User_reply = "Y"
    elif User_reply == "NO":
        User_reply = "N"
    elif User_reply == "MAYBE":
        User_reply = "M"
    if User_reply == "Y":
        print("Beep Boop!")
    elif User_reply == "N":
        print("Well, robots don't like you either")
        global VipAccess
        if VipAccess == "T":
            print("--Vip level access taken--")
        VipAccess = "F"
    elif User_reply == "M":
        print("Make up your mind, human")
    else:
        print("Print('input(something sensible)')")

def Programm6():  #(16.03.2026)
    print("You are in a castle of a dragon.")
    DoorChoice = input("There are four doors. Which one do you enter? -- ")
    if DoorChoice == "1":
        print("You found a treasure")
        VipTreasure = random.randint(1,100)
        if VipTreasure > 95:
            print("A Vip password was in it")
            print("It is 5-2-8-0")
        print("You win!")
    elif DoorChoice == "2":
        print("You are quickly attacked by an angry ogre.")
        print("You lose!")
    elif DoorChoice == "3":
        print("You see a sleeping dragon.")
        print("You can...")
        print("...1)Try to steal gold")
        print("...2)Try to escape")
        DragonChoice = input("1 or 2 -- ")
        if DragonChoice == "2":
            print("You were able to escape!")
            print("You win!")
        else:
            print("The dragon wakes up and eats you.")
            print("You lose!")
    if DoorChoice == "4":
        print("You see a sphinx.")
        SPass = str(random.randint(1,10))
        SGuess = input("Can you guess my number.It is inbetween 1 to 10 -- ")
        if SGuess == SPass:
            print("You are freed.")
            print("You win!")
        else:
            print("The sphinx traps you.")
            print("You lose!")

def Programm7():  #(17.03.2026)
    aliens = 2
    APass = "ALIENS"
    print("Aliens are invading the earth!")
    print("Activate the defence platform!")
    print("")
    print("------------------------------------------")
    print("           The defence platform           ")
    print("------------------------------------------")
    time.sleep(1)
    print("")
    print("------------------------------------------")
    print("            Checking VipAccess            ")
    print("------------------------------------------")
    global VipAccess
    time.sleep(1)
    if VipAccess == "T":
        print("VipAccess = 'T'")
        print("--Access granted--")
        print("Password =",APass)
    else:
        print("VipAccess = 'F'")
        APassGuess = input("Please enter the password -- ").upper()
        while APassGuess != APass:
            print("")
            print("INCORRECT PASSWORD")
            print("")
            aliens = aliens ** 2
            print("There are", aliens, "aliens now on earth")
            if aliens > 8000000000:
                break
            print("")
            print("Hint: The thing is attacking us.")
            print("")
            APassGuess = input("Please enter the password -- ").upper()
        if APassGuess == APass:
            print("We won! Hooray!")
        else:
            print("No! The aliens have out numbered us!")

def Programm8():  #(18.03.2026)
    GNum = str(random.randint(1,20))
    if VipAccess == "T":
        GPstate = input("Learn correct answer(skips programm)[Y/N] -- ").upper()
        if GPstate != "Y":
            GGuess = input("Can you guess my number. It is inbetween 1 to 20 -- ")
            while GGuess != GNum:
                if int(GGuess) < int(GNum):
                    print("Too low")
                else:
                    print("Too high")
                GGuess = input("Can you guess my number. It is inbetween 1 to 20 -- ")
            print("Correct!")
        else:
            print("The number is", GNum)
    else:
        GGuess = input("Can you guess my number. It is inbetween 1 to 20 -- ")
        while GGuess != GNum:
            if int(GGuess) < int(GNum):
                print("Too low")
            else:
                print("Too high")
            GGuess = input("Can you guess my number. It is inbetween 1 to 20 -- ")
        print("Correct!")

def Programm9():  #(18.03.2026)
    Num = input("Number = ")
    Num2 = input("Number2 = ")
    num = int(Num)
    num2 = int(Num2)
    for Cyc1 in range(num,num2):
        print(Cyc1)

def Programm10():  #(18.03.2026)
    TTMN = int(input("What number to muitiply by -- "))
    TTEN = int(input("The final number -- ")) + 1
    for Cyc2 in range(1,TTEN):
        print(Cyc2, "x", TTMN, "=", Cyc2*TTMN)

def Programm11():  #(18.03.2026)
    for Cyc3 in range(1,5):
        print("Bleep")
        for Cyc4 in range(1,5):
            print("Bloop")
        print("Bzzzt")

def Programm12():  #(24.03.2026)
    print("Create a list with 4 elements")
    print("")
    El1 = input("Element 1 -- ")
    El2 = input("Element 2 -- ")
    El3 = input("Element 3 -- ")
    El4 = input("Element 4 -- ")
    print("")
    print("The list will now change")
    List1 = [El1,El2,El3,El4]
    List1E = [El1,El2,El3,El4]
    print(List1)
    List1[0] = "Change?"
    print(List1)
    del List1[0]
    print(List1)
    List1.append("Change!")
    print(List1)
    Num = random.randint(0,3)
    Num2 = random.randint(1,3)
    Num3 = random.randint(0,2)
    List2 = [List1E[Num],List1E[Num3],List1E[Num2]]
    List1 = List2 + List1
    print(List1)
    print('')
    for Cyc5 in List1:
        print(Cyc5)

def Programm13():  #(11.04.2026)
    print("Create a list with 2 elements and 2 keys")
    print("")
    El1 = input("Element 1 -- ")
    El2 = input("Element 2 -- ")
    Key1 = input("Key 1 -- ")
    Key2 = input("Key 2 -- ")
    print("")
    print("The list will now change")
    List1 = {Key1: El1, Key2: El2}
    List1E = {Key1: El1, Key2: El2}
    print(List1)
    List1["Change?"] = "Change!"
    print(List1)
    del List1[Key1]
    print(List1)
    List1[Key2] = "Changeful!"
    print(List1)
    print('')
    for Cyc6 in List1:
        print(Cyc6)

def Programm14():  #(12.04.2026)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet = alphabet * 2
    STE = input("The string that you want to encrypt -- ").upper()
    Key = int(input("Enter a number between -25 and 25 -- "))
    ES = ""
    for x in STE:
        pos = alphabet.find(x)
        NewPos = pos + Key
        if x in alphabet:
            ES = ES + alphabet[NewPos]
        else:
            ES = ES + x
    print("The message is:", ES)

def Programm15():  #(13.04.2026)
    color("blue")
    shape("turtle")
    speed(10)
    pensize(4)
    NoA = int(input("How many sides do you want? -- "))
    Angle = 360 / NoA
    for Cyc7 in range(NoA):
        forward(50)
        right(Angle)

def Programm16():  #(15.04.2026)

    def VShape(size):
        right(25)
        forward(size)
        backward(size)
        left(50)
        forward(size)
        backward(size)
        right(25)

    def SnowflakeArm(size):
        for Cyc8 in  range(4):
            forward(size)
            VShape(size)
        backward(size*4)

    def Snowflake(size):
        color(random.choice(colors))
        for Cyc7 in range(NoA):
            SnowflakeArm(size)
            right(Angle)

    colors = ["white","blue","cyan","purple","green","white","white"]
    goto(0,0)
    shape("turtle")
    speed(10)
    pensize(6)
    Screen().bgcolor("turquoise")
    clear()
    NoA = int(input("How many arms do you want? -- "))
    NoS = int(input("How many snowflakes do you want? -- "))
    Angle = 360 / NoA
    for Cyc9 in range(NoS):
        size = random.randint(5,30)
        x = random.randint(-400, 400)
        y = random.randint(-400, 400)
        penup()
        goto(x,y)
        pendown()
        Snowflake(size)

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

def Code():
    global Stop, VipAccess
    TAEstate = "N"  #(15.03.2026)
    EPstate = "N"
    if VipAccess == "T":
        TAEstate = input("Skip procedure[Y/N] -- ").upper()
    if TAEstate != "Y":
        Programm1()
        CTNP()
        if Stop == 1:
            pass
        else:
            Programm2()
            CTNP()
            if Stop == 1:
                pass
            else:
                Programm3()
                CTNP()
                if Stop == 1:
                    pass
                else:
                    Programm4()
                    CTNP()
                    if Stop == 1:
                        pass
                    else:
                        Programm5()
                        CTNP()
                        if Stop == 1:  #(16.03.2026)
                            pass
                        else:
                            Programm6()
                            CTNP()
                            if Stop == 1:  #(17.03.2026)
                                pass
                            else:
                                Programm7()
                                CTNP()
                                if Stop == 1:  #(18.03.2026)
                                    pass
                                else:
                                    Programm8()
                                    if VipAccess == "T":  #(20.03.2026)
                                        EPstate = input("Skip programms 9-11[Y/N] -- ").upper()
                                    if EPstate != "Y":
                                        CTNP()
                                        if Stop == 1:
                                            pass
                                        else:
                                            Programm9()
                                            CTNP()
                                            if Stop == 1:
                                                pass
                                            else:
                                                Programm10()
                                                CTNP()
                                                if Stop == 1:
                                                    pass
                                                else:
                                                    Programm11()
                                    else:
                                        pass
                                    CTNP()  #(24.03.2026)
                                    if Stop == 1:
                                        pass
                                    else:
                                        Programm12()
                                        CTNP()  #(11.04.2026)
                                        if Stop == 1:
                                            pass
                                        else:
                                            Programm13()
                                            CTNP()  #(12.04.2026)
                                            if Stop == 1:
                                                pass
                                            else:
                                                Programm14()
                                                CTNP()  #(15.04.2026)
                                                if Stop == 1:
                                                    pass
                                                else:
                                                    Programm15()
                                                    CTNP()
                                                    if Stop == 1:
                                                        pass
                                                    else:
                                                        Programm16()
        ProgrammP1()
        CTNP()
        if Stop == 1:
            pass
        else:
            ProgrammP2()
    else:
        pass
    print("")  #(16.03.2026)
    print("Stop!")
    print("")
    print("------------------")
    print("Checking VipAccess")
    print("------------------")
    print("")
    time.sleep(1.5)
    if VipAccess == "T":
        print("VipAccess = 'T'")
        Restart()
    else:
        print("VipAccess = 'F'")
        print("You shall not pass")
        Pass = random.randint(1,20)
        if Pass <= 19:
            global RA
            RestartAttempt = RestAtt = RA = int(RA) + 1
            print("Restart №"+str(RA),"initialaizing")
            Restart()
        else:
            print("A bug has occured!")

def Restart():  #(16.03.2026)
    global E_C
    if VipAccess == "F":
        Code()
    else:
        Exit_Chioce = E_C = input("Do you want to exit the programm?[Y/N] -- ").upper()
        if E_C == "N":
            PrStart = input("What programm to launch? -- ")
            if PrStart == "2":
                Programm2()
                Restart()
            elif PrStart == "3":
                Programm3()
                Restart()
            elif PrStart == "4":
                Programm4()
                Restart()
            elif PrStart == "5":
                Programm5()
                Restart()
            elif PrStart == "6":
                Programm6()
                Restart()
            elif PrStart == "7":
                Programm7()
                Restart()
            elif PrStart == "8":
                Programm8()
                Restart()
            elif PrStart == "9":
                Programm9()
                Restart()
            elif PrStart == "10":
                Programm10()
                Restart()
            elif PrStart == "11":
                Programm11()
                Restart()
            elif PrStart == "12":
                Programm12()
                Restart()
            elif PrStart == "13":
                Programm13()
                Restart()
            elif PrStart == "14":
                Programm14()
                Restart()
            elif PrStart == "15":
                Programm15()
                Restart()
            elif PrStart == "16":
                Programm16()
                Restart()
            else:
                Code()
        else:
            pass