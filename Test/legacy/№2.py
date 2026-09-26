def Enter():  #(13.03.2026)
    VN = "a2.7.19"
    print("--- HubBase "+VN+" (default, Mar 15 2026) ---")
    global VipAccess, PassGuess, ModAccess
    VipAccess = "F"
    Password = str(1041)
    PassGuess = 0
    while PassGuess != Password:
        Num = input("Number = ")
        Num2 = input("Number2 = ")
        num = int(Num)
        num2 = int(Num2)
        PassGuess = Num + Num2
        if PassGuess != Password:
            print("Incorrect")
        if PassGuess == str(5280):
            print("--Vip level access awarded--")
            print("Pass = 1041")
            VipAccess = "T"
            PassGuess = str(1041)
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

def Programm5():
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
        print("--Vip level access taken (if you had it)--")
        VipAccess = "F"
    elif User_reply == "M":
        print("Make up your mind, human")
    else:
        print("Print('input((something sensible))'")

def CTNP():  #(15.03.2026)
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
        Stop()

def Advance():  #(15.03.2026)
    Adv = 1

def Stop():  #(15.03.2026)
    global Stop
    Stop = 1

#CodeBase
Enter()  #(13.03.2026)
TAEstate = "N"
if VipAccess == "T":
    TAEstate = input("Skip procedure[Y/N]").upper()
if TAEstate != "Y":
    Programm1()  #(15.03.2026)
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
else:
    pass
