import time  # (16.03.2026)
import random
from turtle import *
import tkinter as tkr
from tkinter import messagebox
import subprocess
import sys
import importlib
import inspect

__version__ = "0.0.2.1.01"
__version2__ = "0.0.2.1.0.0"
__parameters__ = "(default, Sep 11 2026, 19:15:51)"

PlPr = False
RA = 0
progs = 21
VipAccess = False


class User:
    def __init__(self, login: str):
        self.VipAccess = False
        self.username = login

    def log_in(self):
        self.VipAccess = input("VIP password -- ") == "5280"
        if not self.VipAccess:
            print("Incorrect.")
        else:
            print("Correct.")
        global VipAccess
        VipAccess = self.VipAccess


def Enter():  # (13.03.2026)
    print(f"--- HubBase {__version__} {__parameters__} ---")
    User_obj = User(input("Login: ").lower())
    User_obj.log_in()
    return User_obj


def ProgramCycle(programmList: dict, TransitionMethod, TransitionMethodargs: list):
    try:
        automate_deps("HubBaseUtility")["HubBaseUtility"].ProgramCycle(programmList, TransitionMethod, TransitionMethodargs)
    except (ImportError, AttributeError):
        for programm in range(1, 1000000000000000):
            print(f"Programm №{programm} launching")
            try:
                programmList[programm]()
                success = TransitionMethod(*TransitionMethodargs)
                if success:
                    continue
                else:
                    break
            except KeyError:
                break
            except Exception as e:
                print(e)
                break


def automate_deps(which: str | list[str] = "_all"):
    def load_deps() -> list[str]:
        deps = []
        with open("requirements.txt", "r", encoding="utf-8") as f:
            for line in f.readlines():
                deps.append(line.replace(" =", "STOP").replace(" ~", "STOP").split("STOP")[0])
        return deps

    global PlPr
    modules = {}
    not_installed = []
    if which == "_all":
        try:
            deps = load_deps()
        except OSError:
            raise OSError("File requirements.txt not found.")
    elif isinstance(which, list):
        deps = which
    else:
        deps = [which]
    for dep in deps:
        try:
            modules[dep] = importlib.import_module(dep + ".Main")
        except ImportError:
            not_installed.append(dep)
    if not_installed:
        print(f"Error: module{'s' if len(not_installed) > 1 else ''} {', '.join(not_installed)} not installed")
        install_prompt = input("Install them?[Y/N] -- ").upper()
        if install_prompt == "Y":
            try:
                _ = subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True,
                                   capture_output=True)
                print("Modules installed.")
                modules = automate_deps()
            except subprocess.CalledProcessError:
                print("Install failed.")
                sys.exit(1)
    return modules


def extend_prList(prList: dict[int, object], modules: dict[str, object]):
    for module in modules.values():
        if "HubBase" in str(module.__name__):
            suffix = str(module.__name__).removesuffix(".Main").removeprefix("HubBase")[0].upper()
            modulefuncs = inspect.getmembers(module, predicate=inspect.isfunction)
            for func_name, func_obj in modulefuncs:
                if f"Programm{suffix}" in func_name:
                    prList[len(prList) + 1] = func_obj
    return prList


def Setup_HubBase():  # (11.06.2026)
    modules = automate_deps()
    prList = extend_prList(
        {1: Programm1, 2: Programm2, 3: Programm3, 4: Programm4, 5: Programm5, 6: Programm6, 7: Programm7,
         8: Programm8, 9: Programm9, 10: Programm10, 11: Programm11, 12: Programm12, 13: Programm13,
         14: Programm14, 15: Programm15, 16: Programm16, 17: Programm17, 18: Programm18, 19: Programm19,
         20: Programm20, 21: Programm21}, modules)
    return prList, modules


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
        if VipAccess:
            print("--Vip level access taken--")
        VipAccess = False
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
    time.sleep(1)
    if VipAccess:
        print("VipAccess = True")
        print("--Access granted--")
        print("Password =", APass)
    else:
        print("VipAccess = False")
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
    if VipAccess:
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
                    print("Your score was: ", score)
                    if VipAccess:
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
                        print("Your score was: ", score)

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
        if VipAccess:
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
            print("Your score was: ", str(score))
            PlayAgain = tkr.messagebox.askyesno(message="Play again?")
            if PlayAgain:
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
        global bat, ball, windowOpen, batSpeed, rightPressed, leftPressed, canvas2, canvasWidth, canvasHeight, ballMoveX, ballMoveY, setBatBottom, setBatTop, window4, score, bounceCount
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
        score = 0
        bounceCount = 0
        window4.protocol("WM_DELETE_WINDOW", close)
        window4.bind("<KeyPress>", on_key_press)
        window4.bind("<KeyRelease>", on_key_release)
        canvas2.coords(bat, 10, setBatTop, 50, setBatBottom)
        canvas2.coords(ball, 20, setBatTop - 10, 30, setBatTop)

    def reset():
        global bat, ball, windowOpen, batSpeed, rightPressed, leftPressed, canvas2, canvasWidth, ballMoveX, ballMoveY, setBatBottom, setBatTop, window4, score, bounceCount
        leftPressed = 0
        rightPressed = 0
        ballMoveX = 4
        ballMoveY = -4
        score = 0
        bounceCount = 0
        canvas2.coords(bat, 10, setBatTop, 50, setBatBottom)
        canvas2.coords(ball, 20, setBatTop - 10, 30, setBatTop)

    def play_Tennis():
        global windowOpen, window4
        while windowOpen:
            move_tennisObject("bat")
            move_tennisObject("ball")
            window4.update()
            time.sleep(0.02)
            if windowOpen:
                check_game_over()

    setup_Tennis()
    play_Tennis()


def Programm21():
    global game_list, move
    move = 0
    game_list = {1: [0, [0, 0, 100, 100]], 2: [0, [110, 0, 210, 100]], 3: [0, [220, 0, 320, 100]],
                 4: [0, [0, 110, 100, 210]], 5: [0, [110, 110, 210, 210]], 6: [0, [220, 110, 320, 210]],
                 7: [0, [0, 220, 100, 320]], 8: [0, [110, 220, 210, 320]], 9: [0, [220, 220, 320, 320]]}
    x = []
    o = []
    tttwindow = tkr.Tk()
    tttcanvas = tkr.Canvas(tttwindow, bg="white", width=320, height=320)
    tttcanvas.pack()
    S1_id = tttcanvas.create_rectangle(*game_list[1][1], fill="black")
    S4_id = tttcanvas.create_rectangle(*game_list[4][1], fill="black")
    S7_id = tttcanvas.create_rectangle(*game_list[7][1], fill="black")
    S2_id = tttcanvas.create_rectangle(*game_list[2][1], fill="black")
    S5_id = tttcanvas.create_rectangle(*game_list[5][1], fill="black")
    S8_id = tttcanvas.create_rectangle(*game_list[8][1], fill="black")
    S3_id = tttcanvas.create_rectangle(*game_list[3][1], fill="black")
    S6_id = tttcanvas.create_rectangle(*game_list[6][1], fill="black")
    S9_id = tttcanvas.create_rectangle(*game_list[9][1], fill="black")

    def Render(game_list: dict, move: int):
        for square in game_list:
            square_data = game_list[square]
            if square_data[0] == 0:
                pass
            elif square_data[0] == 1:
                new_square_data = [square_data[1][2], square_data[1][1], square_data[1][0], square_data[1][3]]
                tttcanvas.create_line(*square_data[1], fill="red", width=3)
                tttcanvas.create_line(*new_square_data, fill="red", width=3)
                if not square in x:
                    x.append(square)
            elif square_data[0] == 2:
                tttcanvas.create_oval(*square_data[1], outline="blue", width=3)
                if not square in o:
                    o.append(square)
        if (((1 in x and 4 in x and 7 in x) or (1 in x and 2 in x and 3 in x) or (2 in x and 5 in x and 8 in x) or
             (4 in x and 5 in x and 6 in x) or (3 in x and 6 in x and 9 in x) or (7 in x and 8 in x and 9 in x)) or
            (1 in x and 5 in x and 9 in x)) or (3 in x and 5 in x and 7 in x):
            print("X`es have won!")
            tttwindow.destroy()
        elif (((1 in o and 4 in o and 7 in o) or (1 in o and 2 in o and 3 in o) or (2 in o and 5 in o and 8 in o) or
               (4 in o and 5 in o and 6 in o) or (3 in o and 6 in o and 9 in o) or (7 in o and 8 in o and 9 in o)) or
              (1 in o and 5 in o and 9 in o)) or (3 in o and 5 in o and 7 in o):
            print("Circles have won!")
            tttwindow.destroy()
        elif move == 9:
            print("Draw.")
            tttwindow.destroy()

    def Move(event):
        global move, game_list
        for key, x in game_list.items():
            if x[1][0] <= event.x <= x[1][2] and x[1][1] <= event.y <= x[1][3]:
                square = key
                break
        else:
            raise Exception("Click location not found")
        if move % 2 == 0:
            side = 1
        else:
            side = 2
        if game_list[square][0] == 0:
            game_list[square][0] = side
            move += 1
            Render(game_list, move)

    tttcanvas.tag_bind(S1_id, "<Button-1>", Move)
    tttcanvas.tag_bind(S2_id, "<Button-1>", Move)
    tttcanvas.tag_bind(S3_id, "<Button-1>", Move)
    tttcanvas.tag_bind(S4_id, "<Button-1>", Move)
    tttcanvas.tag_bind(S5_id, "<Button-1>", Move)
    tttcanvas.tag_bind(S6_id, "<Button-1>", Move)
    tttcanvas.tag_bind(S7_id, "<Button-1>", Move)
    tttcanvas.tag_bind(S8_id, "<Button-1>", Move)
    tttcanvas.tag_bind(S9_id, "<Button-1>", Move)
    Render(game_list, move)
    tttwindow.mainloop()


def CTNP():  # (15.03.2026)
    Cstate = input("Continue?[Y/N] -- ").upper()
    if Cstate == "Y":
        return True
    else:
        return False


# CodeBase
def Code(prList: dict, User: User):
    TAEstate = "N"  # (15.03.2026)
    if User.VipAccess:
        TAEstate = input("Skip procedure[Y/N] -- ").upper()
    if TAEstate != "Y":
        ProgramCycle(prList, CTNP, [])
    else:
        pass
    print("")  # (16.03.2026)
    print("------------------")
    print("Checking VipAccess")
    print("------------------")
    print("")
    time.sleep(1.5)
    if User.VipAccess:
        print("VipAccess = 'T'")
        Restart(prList, User)
    else:
        print("VipAccess = 'F'")
        print("Goodbye!")
        sys.exit(0)


def Restart(prList: dict, User: User):  # (16.03.2026)
    if not User.VipAccess:
        Code(prList, User)
    else:
        E_C = input("Do you want to exit the programm?[Y/N] -- ").upper()
        if E_C == "N":
            PrStart = input("What programm to launch? -- ")
            if "P" in PrStart:
                PrStart = int(PrStart.replace("P", "")) + int(progs)
            PrStart = int(PrStart)
            try:
                prList[PrStart]()
                Restart(prList, User)
            except KeyError:
                print(f"Programm {PrStart} does not exist")
                sys.exit(1)
        else:
            pass


# (16.03.2026)
if __name__ == '__main__':
    prList, modules = Setup_HubBase()
    User = Enter()
    Code(prList, User)
