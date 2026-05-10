import tkinter as tkr
import time

def ProgrammP4():
    global Num, Num2
    Num = 0
    Num2 = 0
    window = tkr.Tk()

    def NumDZero(event):
        global Num
        Num = (Num * 10)

    def NumDOne(event):
        global Num
        Num = (Num * 10) + 1

    def NumDTwo(event):
        global Num
        Num = (Num * 10) + 2

    def NumDThree(event):
        global Num
        Num = (Num * 10) + 3

    def NumDFour(event):
        global Num
        Num = (Num * 10) + 4

    def NumDFive(event):
        global Num
        Num = (Num * 10) + 5

    def NumDSix(event):
        global Num
        Num = (Num * 10) + 6

    def NumDSeven(event):
        global Num
        Num = (Num * 10) + 7

    def NumDEight(event):
        global Num
        Num = (Num * 10) + 8

    def NumDNine(event):
        global Num
        Num = (Num * 10) + 9

    Zero_id = tkr.Button(window, width=20, text="0")
    Zero_id.pack(padx=10,pady=10)
    One_id = tkr.Button(window, width=2, text="1")
    One_id.pack(padx=10, pady=10)
    Two_id = tkr.Button(window, width=2, text="2")
    Two_id.pack(padx=10, pady=10)
    Three_id = tkr.Button(window, width=2, text="3")
    Three_id.pack(padx=10, pady=10)
    Four_id = tkr.Button(window, width=2, text="4")
    Four_id.pack(padx=10, pady=10)
    Five_id = tkr.Button(window, width=2, text="5")
    Five_id.pack(padx=10, pady=10)
    Six_id = tkr.Button(window, width=2, text="6")
    Six_id.pack(padx=10, pady=10)
    Seven_id = tkr.Button(window, width=2, text="7")
    Seven_id.pack(padx=10, pady=10)
    Eight_id = tkr.Button(window, width=2, text="8")
    Eight_id.pack(padx=10, pady=10)
    Nine_id = tkr.Button(window, width=2, text="9")
    Nine_id.pack(padx=10, pady=10)
    Zero_id.bind("<Button-1>", NumDZero)
    One_id.bind("<Button-1>", NumDOne)
    Two_id.bind("<Button-1>", NumDTwo)
    Three_id.bind("<Button-1>", NumDThree)
    Four_id.bind("<Button-1>", NumDFour)
    Five_id.bind("<Button-1>", NumDFive)
    Six_id.bind("<Button-1>", NumDSix)
    Seven_id.bind("<Button-1>", NumDSeven)
    Eight_id.bind("<Button-1>", NumDEight)
    Nine_id.bind("<Button-1>", NumDNine)
    window.mainloop()
    print(Num)
    print("Canceled")

ProgrammP4()