import time  # (16.03.2026)
import random
from turtle import *
import tkinter as tkr


def Enter():  # (13.03.2026)
    global VipAccess, PassGuess, Login, VN
    Vips = ["voice659", "vhba", "vipuser", 'hbaofficial', "vvoice", "voice", "v", "vip1"]
    VN = "0.0.2.0.03"
    VipAccess = "F"
    PassGuess = 0
    print("--- HubBase " + VN + " (plus, June 09 2026, 17:22:17) ---")
    Login = input("Login (If <vip level then press enter): ").lower()
    if Login in Vips:
        Password = str(5280)
        while PassGuess != Password:
            PassGuess = input("Password for " + Login + ": ")
            if PassGuess != Password:
                print("Incorrect")
        VipAccess = "T"
    if Login == "":
        Login = "usr"
    print("Login successful!")
    if VipAccess == "T":
        PassGuess = str(5280)


def Programm1():  # (15.03.2026)
    print("Hello world")


def Programm2():  # (15.03.2026)
    Num = input("Number = ")
    Num2 = input("Number2 = ")
    num = int(Num)
    num2 = int(Num2)
    print(num + num2)
    print(num - num2)
    print(num * num2)
    print(num ** num2)
    print(num / num2)
    print(num // num2)
    print(num % num2)


def Programm3():  # (15.03.2026)
    Bananas = input("Bananas = ")
    BananasEaten = input("Bananas Eaten = ")
    print(int(Bananas) - int(BananasEaten))


def Programm4():  # (15.03.2026)
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
    print('"' + "Thanks for creating me,", Uname + '"', "- says", Cname)


def Programm5():  # (15.03.2026)
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


def Programm6():  # (16.03.2026)
    print("You are in a castle of a dragon.")
    DoorChoice = input("There are four doors. Which one do you enter? -- ")
    if DoorChoice == "1":
        print("You found a treasure")
        VipTreasure = random.randint(1, 100)
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
    elif DoorChoice == "4":
        print("You see a sphinx.")
        SPass = str(random.randint(1, 10))
        SGuess = input("Can you guess my number.It is inbetween 1 to 10 -- ")
        if SGuess == SPass:
            print("You are freed.")
            print("You win!")
        else:
            print("The sphinx traps you.")
            print("You lose!")


def Programm7():  # (17.03.2026)
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
        print("Password =", APass)
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


def Programm8():  # (18.03.2026)
    GNum = str(random.randint(1, 20))
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


def Programm9():  # (18.03.2026)
    Num = input("Number = ")
    Num2 = input("Number2 = ")
    num = int(Num)
    num2 = int(Num2)
    for Cyc1 in range(num, num2):
        print(Cyc1)


def Programm10():  # (18.03.2026)
    TTMN = int(input("What number to muitiply by -- "))
    TTEN = int(input("The final number -- ")) + 1
    for Cyc2 in range(1, TTEN):
        print(Cyc2, "x", TTMN, "=", Cyc2 * TTMN)


def Programm11():  # (18.03.2026)
    for Cyc3 in range(1, 5):
        print("Bleep")
        for Cyc4 in range(1, 5):
            print("Bloop")
        print("Bzzzt")


def Programm12():  # (24.03.2026)
    print("Create a list with 4 elements")
    print("")
    El1 = input("Element 1 -- ")
    El2 = input("Element 2 -- ")
    El3 = input("Element 3 -- ")
    El4 = input("Element 4 -- ")
    print("")
    print("The list will now change")
    List1 = [El1, El2, El3, El4]
    List1E = [El1, El2, El3, El4]
    print(List1)
    List1[0] = "Change?"
    print(List1)
    del List1[0]
    print(List1)
    List1.append("Change!")
    print(List1)
    Num = random.randint(0, 3)
    Num2 = random.randint(1, 3)
    Num3 = random.randint(0, 2)
    List2 = [List1E[Num], List1E[Num3], List1E[Num2]]
    List1 = List2 + List1
    print(List1)
    print('')
    for Cyc5 in List1:
        print(Cyc5)


def Programm13():  # (11.04.2026)
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


def Programm14():  # (12.04.2026)
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


def Programm15():  # (13.04.2026)
    color("blue")
    shape("turtle")
    speed(10)
    pensize(4)
    NoA = int(input("How many sides do you want? -- "))
    Angle = 360 / NoA
    for Cyc7 in range(NoA):
        forward(50)
        right(Angle)


def Programm16():  # (15.04.2026)

    def VShape(size):
        right(25)
        forward(size)
        backward(size)
        left(50)
        forward(size)
        backward(size)
        right(25)

    def SnowflakeArm(size):
        for Cyc8 in range(4):
            forward(size)
            VShape(size)
        backward(size * 4)

    def Snowflake(size):
        color(random.choice(colors))
        for Cyc7 in range(NoA):
            SnowflakeArm(size)
            right(Angle)

    colors = ["white", "blue", "cyan", "purple", "green", "white", "white"]
    goto(0, 0)
    shape("turtle")
    speed(10)
    pensize(6)
    Screen().bgcolor("turquoise")
    clear()
    NoA = int(input("How many arms do you want? -- "))
    NoS = int(input("How many snowflakes do you want? -- "))
    Angle = 360 / NoA
    for Cyc9 in range(NoS):
        size = random.randint(5, 30)
        x = random.randint(-400, 400)
        y = random.randint(-400, 400)
        penup()
        goto(x, y)
        pendown()
        Snowflake(size)


def Programm17():  # (24.04.2026)
    window1 = tkr.Tk()
    button1 = tkr.Button(window1, text="Do not press this button", width=40)
    button1.pack(padx=10, pady=10)
    global clicks1
    clicks1 = 0

    def onClick(event):
        global clicks1
        clicks1 = clicks1 + 1
        if clicks1 == 1:
            button1.configure(text="Seriously? Do. Not. Press. It.")
        elif clicks1 == 2:
            button1.configure(text="Gah! Next next time no-no-no more butt-utt-on-on")
        elif clicks1 == 3:
            time.sleep(1.0)
            button1.configure(text="Opps. I said 'Next next time'")
        else:
            button1.pack_forget()

    button1.bind("<ButtonRelease-1>", onClick)
    window1.mainloop()


def Programm18():  # (27.04.2026)
    print("To draw, use LMB.")
    window2 = tkr.Tk()
    canvas1 = tkr.Canvas(window2, bg="white", width=750, height=500)
    canvas1.pack()
    global lastX, lastY
    lastX, lastY = 0, 0
    global Scolor
    Scolor = "black"
    width = int(input("How wide do you want your pencil? -- "))
    red_id = canvas1.create_rectangle(10, 10, 30, 30, fill="red")
    blue_id = canvas1.create_rectangle(10, 35, 30, 55, fill="blue")
    black_id = canvas1.create_rectangle(10, 60, 30, 80, fill="black")
    white_id = canvas1.create_rectangle(10, 85, 30, 105, fill="white")

    def StoreNewPos(event):
        global lastX, lastY
        lastX = event.x
        lastY = event.y

    def onClick(event):
        StoreNewPos(event)

    def onDrag(event):
        global Scolor
        canvas1.create_line(lastX, lastY, event.x, event.y, fill=Scolor, width=width)
        StoreNewPos(event)

    def CCTR(event):
        global Scolor
        Scolor = "red"

    def CCTB(event):
        global Scolor
        Scolor = "blue"

    def CCTb(event):
        global Scolor
        Scolor = "black"

    def CCTW(event):
        global Scolor
        Scolor = "white"

    canvas1.bind("<Button-1>", onClick)
    canvas1.bind("<B1-Motion>", onDrag)
    canvas1.tag_bind(red_id, "<Button-1>", CCTR)
    canvas1.tag_bind(blue_id, "<Button-1>", CCTB)
    canvas1.tag_bind(black_id, "<Button-1>", CCTb)
    canvas1.tag_bind(white_id, "<Button-1>", CCTW)
    window2.mainloop()


def Programm19():  # (29.04.2026)
    def Setup_minesweeper():
        global gameOver, score, squaresLeft, minefield
        gameOver = False
        score = 0
        squaresLeft = 0
        minefield = []

    def printfield(minefield):
        for rowList in minefield:
            print(rowList)

    def create_minefield(minefield, window):

        def generate_minefield(minefield):
            global squaresLeft
            for row in range(10):
                rowList = []
                for column in range(10):
                    BombRN = random.randint(1, 100)
                    if BombRN <= 20:
                        rowList.append(1)
                    else:
                        rowList.append(0)
                        squaresLeft = squaresLeft + 1
                minefield.append(rowList)

        def set_Flag(event):
            global score, squaresLeft, gameOver, minefield, PFQ
            square = event.widget
            currentText = square.cget("text")
            if currentText == "    ":
                square.config(bg="yellow", text="" + "B" + "")
            if currentText == "B":
                square.config(bg="green", text="    ")

        def check_Bombs(event):
            global score, squaresLeft, gameOver, minefield, PFQ
            square = event.widget
            row = int(square.grid_info()["row"])
            column = int(square.grid_info()["column"])
            currentText = square.cget("text")
            if gameOver == False:
                if minefield[row][column] == 1:
                    gameOver = True
                    square.config(bg="red")
                    print("Game over! You hit a bomb!")
                    if VipAccess == "T":
                        if PFQ == "Y":
                            print("**Even with a cheat!!!**")
                    print("Your score was:", score)
                elif currentText == "    ":
                    square.config(bg="brown")
                    totalBombs = 0
                    if row < 9:
                        if minefield[row + 1][column] == 1:
                            totalBombs = totalBombs + 1
                    if row > 0:
                        if minefield[row - 1][column] == 1:
                            totalBombs = totalBombs + 1
                    if column > 0:
                        if minefield[row][column - 1] == 1:
                            totalBombs = totalBombs + 1
                    if column < 9:
                        if minefield[row][column + 1] == 1:
                            totalBombs = totalBombs + 1
                    if row > 0 and column > 0:
                        if minefield[row - 1][column - 1] == 1:
                            totalBombs = totalBombs + 1
                    if row < 9 and column < 9:
                        if minefield[row + 1][column + 1] == 1:
                            totalBombs = totalBombs + 1
                    if row > 0 and column < 9:
                        if minefield[row - 1][column + 1] == 1:
                            totalBombs = totalBombs + 1
                    if row < 9 and column > 0:
                        if minefield[row + 1][column - 1] == 1:
                            totalBombs = totalBombs + 1
                    square.config(text=" " + str(totalBombs) + " ")
                    score += 1
                    squaresLeft -= 1
                    if squaresLeft == 0:
                        gameOver = True
                        print("Well done!")
                        print("Your score was:", score)

        def layout_minefield(window, minefield):
            global VipAccess
            for rowNumber, rowList in enumerate(minefield):
                for columnNumber, columnEntry in enumerate(rowList):
                    RSC = random.randint(1, 100)
                    if RSC < 25:
                        square = tkr.Label(window, text="    ", bg="darkgreen")
                    elif RSC > 75:
                        square = tkr.Label(window, text="    ", bg="seagreen")
                    else:
                        square = tkr.Label(window, text="    ", bg="green")
                    square.grid(row=rowNumber, column=columnNumber)
                    square.bind("<Button-1>", check_Bombs)
                    square.bind("<Button-3>", set_Flag)

        generate_minefield(minefield)
        layout_minefield(window, minefield)

    def Play_minesweeper():
        global VipAccess, minefield, PFQ
        window3 = tkr.Tk()
        create_minefield(minefield, window3)
        if VipAccess == "T":
            PFQ = input("Do you want a cheat?[Y/N] -- ").upper()
            if PFQ == "Y":
                printfield(minefield)
        window3.mainloop()

    Setup_minesweeper()
    Play_minesweeper()


def Programm20():
    def move_tennisObject(object):
        global batSpeed, bat, rightPressed, leftPressed, ball, canvas2, canvasWidth, ballMoveX, ballMoveY, setBatBottom, setBatTop, score, bounceCount
        if object == "bat":
            batMove = batSpeed * rightPressed - batSpeed * leftPressed
            (batLeft, batTop, batRight, batBottom) = canvas2.coords(bat)
            if (batLeft > 0 or batMove > 0) and (batRight < canvasWidth or batMove < 0):
                canvas2.move(bat, batMove, 0)
        elif object == "ball":
            (batLeft, batTop, batRight, batBottom) = canvas2.coords(bat)
            (ballLeft, ballTop, ballRight, ballBottom) = canvas2.coords(ball)
            if ballMoveX > 0 and ballRight > canvasWidth:
                ballMoveX = -ballMoveX
            if ballMoveX < 0 and ballLeft < 0:
                ballMoveX = -ballMoveX
            if ballMoveY < 0 and ballTop < 0:
                ballMoveY = -ballMoveY
            if ballMoveY > 0 and ballBottom > setBatTop and ballBottom < setBatBottom:
                (batLeft, batTop, batRight, batBottom) = canvas2.coords(bat)
                if (ballMoveX > 0 and (ballRight + ballMoveX > batLeft and ballLeft < batRight) or ballMoveX < 0 and (
                        ballRight > batLeft and ballLeft + ballMoveX < batRight)):
                    ballMoveY = -ballMoveY
                    score += 1
                    bounceCount += 1
                    if bounceCount == 4:
                        bounceCount = 0
                        batSpeed += 1
                        if ballMoveX > 0:
                            ballMoveX += 1
                        else:
                            ballMoveX -= 1
                        ballMoveY -= 1
            canvas2.move(ball, ballMoveX, ballMoveY)
        else:
            print("Such object does not exist")

    def close():
        global windowOpen, window4
        windowOpen = False
        window4.destroy()

    def check_game_over():
        global canvasHeight
        (ballLeft, ballTop, ballRight, ballBottom) = canvas2.coords(ball)
        if ballTop > canvasHeight:
            PlayAgain = tkr.messagebox.askyesno(message="Play again?")
            if PlayAgain == True:
                reset()
            else:
                close()

    def on_key_press(event):
        global rightPressed, leftPressed
        if event.keysym == "Left":
            leftPressed = 1
        if event.keysym == "Right":
            rightPressed = 1

    def on_key_release(event):
        global rightPressed, leftPressed
        if event.keysym == "Left":
            leftPressed = 0
        if event.keysym == "Right":
            rightPressed = 0

    def setup_Tennis():
        global bat, ball, windowOpen, batSpeed, rightPressed, leftPressed, canvas2, canvasWidth, canvasHeight, ballMoveX, ballMoveY, setBatBottom, setBatTop, window4
        canvasWidth = 750
        canvasHeight = 500
        window4 = tkr.Tk()
        canvas2 = tkr.Canvas(window4, width=canvasWidth, height=canvasHeight, bg="dodgerblue4")
        canvas2.pack()
        bat = canvas2.create_rectangle(0, 0, 40, 10, fill="dark turquoise")
        ball = canvas2.create_oval(0, 0, 10, 10, fill="deep pink")
        windowOpen = True
        batSpeed = 6
        rightPressed = 0
        leftPressed = 0
        ballMoveX = 4
        ballMoveY = -4
        setBatTop = canvasHeight - 40
        setBatBottom = canvasHeight - 30
        window4.protocol("WM_DELETE_WINDOW", close)
        window4.bind("<KeyPress>", on_key_press)
        window4.bind("<KeyRelease>", on_key_release)
        canvas2.coords(bat, 10, setBatTop, 50, setBatBottom)
        canvas2.coords(ball, 20, setBatTop - 10, 30, setBatTop)

    def reset():
        global bat, ball, windowOpen, batSpeed, rightPressed, leftPressed, canvas2, canvasWidth, ballMoveX, ballMoveY, setBatBottom, setBatTop, window4
        leftPressed = 0
        rightPressed = 0
        ballMoveX = 4
        ballMoveY = -4
        canvas2.coords(bat, 10, setBatTop, 50, setBatBottom)
        canvas2.coords(ball, 20, setBatTop - 10, 30, setBatTop)

    def play_Tennis():
        global windowOpen, window4
        while windowOpen == True:
            move_tennisObject("bat")
            move_tennisObject("ball")
            window4.update()
            time.sleep(0.02)
            if windowOpen == True:
                check_game_over()

    setup_Tennis()
    play_Tennis()


def ProgrammP1():  # T1

    def Drift():  # (19.03.2026)
        global x, y, z, a
        a = max((y - y * 2) * 2, z)
        y = random.randint(min(a, y * 2), max(a, y * 2))
        if y == 0:
            y = 1
        x = x + y

    def Drift2():  # (19.03.2026)
        global i, o, r, p
        p = max((o - o * 2) * 2, r)
        o = random.randint(min(p, o * 2), max(p, o * 2))
        if o == 0:
            o = 1
        i = i + o

    def ProgrammP1E1():  # (19.03.2026)
        global x, y, i, o, z, r
        Goal = float(input("Set a goal -- "))
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
                    z = -random.randint(1, max(1, y))
                if i > Goal:
                    r = -random.randint(1, max(1, o))
            if x < Goal or i < Goal:
                if x < Goal:
                    z = random.randint(1, max(1, y))
                if i < Goal:
                    r = random.randint(1, max(1, o))
            if x == Goal or i == Goal:  # (20.03.2026)
                if x == Goal:
                    print("First D reached the goal")
                if i == Goal:
                    print("Second D reached the goal")
                break
            Opr = Opr + 1
            if Opr >= 10000:
                print("Fail")
                break

    ProgrammP1E1()  # (19.03.2026)


def ProgrammP2():  # T3
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


def ProgrammP3():  # T4
    window = tkr.Tk()
    button1 = tkr.Button(window, text="Do not press this button", width=40)
    button1.pack(padx=50, pady=20)
    global clicks1
    clicks1 = 0
    print("Please do not close the window before the turtle finishes!")
    print("It may cause bugs.")

    def VShape(size):
        right(25)
        forward(size)
        backward(size)
        left(50)
        forward(size)
        backward(size)
        right(25)

    def SnowflakeArm(size):
        for Cyc8 in range(4):
            forward(size)
            VShape(size)
        backward(size * 4)

    def Snowflake(size):
        color('white')
        for Cyc7 in range(4):
            SnowflakeArm(size)
            right(90)

    def onClick(event):
        global clicks1
        clicks1 = clicks1 + 1
        shape("turtle")
        speed(10)
        pensize(6)
        Screen().bgcolor("turquoise")
        if clicks1 < 20:
            Snowflake(20)
            if clicks1 < 20:
                button1.pack_forget()
                print("Fail")
                Terminator()
        else:
            button1.configure(text="You outsmarted me!")
            print("Success")
            speed(100000)
            Terminator()
            time.sleep(1)
            button1.pack_forget()
            Terminator()

    button1.bind("<ButtonRelease-1>", onClick)
    window.mainloop()


def ProgrammP4():
    print("HB-JS python port 0.0.1.0.00")
    time.sleep(1)

    def JSProgramm1(repeats):
        for i in range(repeats):
            print(str(i) + ". =^.^=")

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
        print(HighFives + 1)
        print(HighFives + 1)
        print(HighFives - 1)
        print("Delayed:")
        print(HighFives)
        print(HighFives + 1)
        print(HighFives + 1)
        print(HighFives - 1)

    print("Programm1:")
    JSProgramm1(10)
    time.sleep(1)
    print("Programm2:")
    JSProgramm2()
    time.sleep(1)
    print("Programm3:")
    JSProgramm3()
    time.sleep(1)


def ProgrammP5():
    def Ttt(sys, n):
        if sys == "tw":
            t = 0
            r = 0
            for i in n:
                o = int(i) * (2 ** r)
                t += o
                r += 1
            print(t)
        elif sys == "te":
            u = int(n)
            x = 0
            while 2 ** x < int(n):
                x += 1
            t = ""
            r = 0
            for i in range(x):
                o = str(int(u) % 2)
                t = t + o
                r += 1
                u = u / 2
            if int(n) == 2 ** x:
                t = t + "1"
            RL = []
            u = str(t)
            t = ""
            for i in u:
                RL.append(i)
            RL.reverse()
            for element in RL:
                t = t + element
            print(t)

    n = input("Number -- ")
    Ttt("te", n)


def CTNP():  # Mainline
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


def Advance():  # Mainline
    Adv = 1
    global Stop
    Stop = 0


def PStop():  # Mainline
    global Stop
    Stop = 1


def Start():
    ProgrammP1()
    CTNP()
    if Stop == 1:
        pass
    else:
        ProgrammP2()
        CTNP()
        if Stop == 1:
            pass
        else:
            ProgrammP3()
            CTNP()
            if Stop == 1:
                pass
            else:
                ProgrammP4()
                CTNP()
                if Stop == 1:
                    pass
                else:
                    ProgrammP5()


def Code():
    global Stop, VipAccess
    print("PE programms are enabled on default!")
    TAEstate = "N"  # (15.03.2026)
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
                        if Stop == 1:  # (16.03.2026)
                            pass
                        else:
                            Programm6()
                            CTNP()
                            if Stop == 1:  # (17.03.2026)
                                pass
                            else:
                                Programm7()
                                CTNP()
                                if Stop == 1:  # (18.03.2026)
                                    pass
                                else:
                                    Programm8()
                                    if VipAccess == "T":  # (20.03.2026)
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
                                    CTNP()  # (24.03.2026)
                                    if Stop == 1:
                                        pass
                                    else:
                                        Programm12()
                                        CTNP()  # (11.04.2026)
                                        if Stop == 1:
                                            pass
                                        else:
                                            Programm13()
                                            CTNP()  # (12.04.2026)
                                            if Stop == 1:
                                                pass
                                            else:
                                                Programm14()
                                                CTNP()  # (15.04.2026)
                                                if Stop == 1:
                                                    pass
                                                else:
                                                    Programm15()
                                                    CTNP()
                                                    if Stop == 1:
                                                        pass
                                                    else:
                                                        Programm16()
                                                        CTNP()
                                                        if Stop == 1:
                                                            pass
                                                        else:
                                                            Programm17()
                                                            CTNP()
                                                            if Stop == 1:
                                                                pass
                                                            else:
                                                                Programm18()
                                                                CTNP()
                                                                if Stop == 1:
                                                                    pass
                                                                else:
                                                                    Programm19()
                                                                    CTNP()
                                                                    if Stop == 1:
                                                                        pass
                                                                    else:
                                                                        Programm20()
                                                                        CTNP()
                                                                        if Stop == 1:
                                                                            pass
                                                                        else:
                                                                            ProgrammP1()
                                                                            CTNP()
                                                                            if Stop == 1:
                                                                                pass
                                                                            else:
                                                                                ProgrammP2()
                                                                                CTNP()
                                                                                if Stop == 1:
                                                                                    pass
                                                                                else:
                                                                                    ProgrammP3()
                                                                                    CTNP()
                                                                                    if Stop == 1:
                                                                                        pass
                                                                                    else:
                                                                                        ProgrammP4()
                                                                                        CTNP()
                                                                                        if Stop == 1:
                                                                                            pass
                                                                                        else:
                                                                                            ProgrammP5()
    else:
        pass
    print("")  # (16.03.2026)
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
        global RA
        RestartAttempt = RestAtt = RA = int(RA) + 1
        print("Restart №" + str(RA), "initialaizing")
        Restart()


def Restart():  # (16.03.2026)
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
            elif PrStart == "17":
                Programm17()
                Restart()
            elif PrStart == "18":
                Programm18()
                Restart()
            elif PrStart == "19":
                Programm19()
                Restart()
            elif PrStart == "20":
                Programm20()
                Restart()
            elif PrStart == "P1":
                ProgrammP1()
                Restart()
            elif PrStart == "P2":
                ProgrammP2()
                Restart()
            elif PrStart == "P3":
                ProgrammP3()
                Restart()
            elif PrStart == "P4":
                ProgrammP4()
                Restart()
            elif PrStart == "P5":
                ProgrammP5()
                Restart()
            else:
                Code()
        else:
            pass


def dev_console():
    global RA, VipAccess, Login, VN
    SpCm = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
            "P1", "P2", "P3", "P4", "P5"]
    if VipAccess == "T":
        print("Developer console for " + VN)
        line = ""
        while line != "stop":
            line = input(Login + " >>> ").lower()
            if line in SpCm:
                PrStart = line
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
                elif PrStart == "17":
                    Programm17()
                    Restart()
                elif PrStart == "18":
                    Programm18()
                    Restart()
                elif PrStart == "19":
                    Programm19()
                    Restart()
                elif PrStart == "20":
                    Programm20()
                    Restart()
                elif PrStart == "P1":
                    ProgrammP1()
                    Restart()
                elif PrStart == "P2":
                    ProgrammP2()
                    Restart()
                elif PrStart == "P3":
                    ProgrammP3()
                    Restart()
                elif PrStart == "P4":
                    ProgrammP4()
                    Restart()
                elif PrStart == "P5":
                    ProgrammP5()
                    Restart()
                else:
                    Code()
            elif line != "stop":
                try:
                    print(eval(line))
                except SyntaxError:
                    print("Error: The syntax is not correct.")
