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

def ProgrammP1():  #(19.03.2026)
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

ProgrammP1()  #(19.03.2026)
                
        
        


