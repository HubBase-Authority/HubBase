import time
import tkinter as tkr
from turtle import *
print("Loading!")
time.sleep(1)
print("Loaded!")
window = tkr.Tk()
button1 = tkr.Button(window, text="Do not press this button", width=40)
button1.pack(padx=50, pady=20)
clicks1 = 0
def onClick(event):
    global clicks1
    clicks1 = clicks1 + 1
    shape("turtle")
    speed(10)
    pensize(6)
    Screen().bgcolor("turquoise")
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
        color('white')
        for Cyc7 in range(4):
            SnowflakeArm(size)
            right(90)
    Snowflake(20)
    if clicks1 < 20:
        button1.pack_forget()
        print("Fail")
    else:
        button1.configure(text="You outsmarted me!")
        print("Success")

button1.bind("<ButtonRelease-1>", onClick)
window.mainloop()
