print("--- Version Backlog a8-a9.0.2 (default, Apr 19 2026) ---")
print("V`s available are a8.0.0 - a9.0.2")
print("Exceptions:")
print("a0.1.0, a0.1.1")
print("Newest - a9, start - a8")
D1 = input("The Main part -- ").lower()
print("1,2,3 and so on")
D2 = input("The addition -- ")
print("1,2,3 and so on")
D3 = input("The fix -- ")
print("B - for betas, PR - for prereleases, R - for releases")
D4 = input("Access to Version -- ").upper()
print("")
if D1 == "a8":
    if D2 == "0":
        if D3 == "0":
            if D4 == "R":
                print("--- HubBase a8.0.0 (default, Apr 10 2026) ---")
                print("Official release!")
                print("Featuring:")
                print("    - 12 programms!")
                print("    - Looped showcase!")
                print("    - Vip`s!")
            else:
                print("Such release does not exist or isn`t documented")
        elif D3 == "1":
            if D4 == "R":
                print("--- HubBase a8.0.1 (default, Apr 10 2026) ---")
                print("First bugfix!")
                print("Changes:")
                print("    - Fixed Version Number Bug!")
            else:
                print("Such release does not exist or isn`t documented")
        elif D3 == "2":
            if D4 == "R":
                print("--- HubBase a8.0.2 (default, Apr 10 2026) ---")
                print("Second bugfix!")
                print("Changes:")
                print("    - Fixed Password not integer bug")
            else:
                print("Such release does not exist or isn`t documented")
        else:
            print("Such release does not exist or isn`t documented")
    elif D2 == "1":
        if D3 == "0":
            if D4 == "R":
                print("--- HubBase a8.1.0 (default, Apr 10 2026) ---")
                print("Addition №1!")
                print("Changes:")
                print("    - Added Admin level access")
            else:
                print("Such release does not exist or isn`t documented")
        else:
            print("Such release does not exist or isn`t documented")
    elif D2 == "2":
        if D3 == "0":
            if D4 == "B":
                print("--- HubBase a8.2.0B (default, Apr 11 2026, 14:40:24) ---")
                print("Addition №2!(not complete)")
                print("Changes:")
                print("    - Added 'Programm13()' as a launchable programm!")
            elif D4 == "R":
                print("--- HubBase a8.2.0 (default, Apr 11 2026, 18:16:51) ---")
                print("Addition №2!")
                print("Changes:")
                print("    - Added 'Programm13()' fully")
            else:
                print("Such release does not exist or isn`t documented")
        elif D3 == "1":
            if D4 == "R":
                print("--- HubBase a8.2.1 (default, Apr 11 2026, 19:33:34) ---")
                print("Bugfix №3!")
                print("Changes:")
                print("    - Fixed 'Programm13()' not working for not Vip users")
            else:
                print("Such release does not exist or isn`t documented")
        else:
            print("Such release does not exist or isn`t documented")
    elif D2 == "3":
        if D3 == "0":
            if D4 == "B":
                print("--- HubBase a8.3.0B (default, Apr 12 2026, 9:30:29) ---")
                print("Addition №3!(in beta)")
                print("Changes:")
                print("    - Added 'Programm14()'(with bugs)")
            elif D4 == "R":
                print("--- HubBase a8.3.0 (default, Apr 12 2026, 10:00:36) ---")
                print("Addition №3!")
                print("Changes:")
                print("    - Added 'Programm14()' fully")
            else:
                print("Such release does not exist or isn`t documented")
        elif D3 == "1":
            print("--- HubBase a8.3.1 (default, Apr 12 2026, 10:42:57) ---")
            print("Bugfix №3!")
            print("Changes:")
            print("    - Fixed 'Programm14()' not working for Decrypt mode")
        else:
            print("Such release does not exist or isn`t documented")
    else:
        print("Such release does not exist or isn`t documented")
elif D1 == "a9":
    if D2 == "0":
        if D3 == "0":
            if D4 == "B":
                print("--- HubBase a9.0.0B (default, Apr 12 2026, 21:17:18) ---")
                print("The first big update!!(Beta!)")
                print("Addition:")
                print("    - Added 'Turtle' programm №1(Pr15)!")
            elif D4 == "PR":
                print("--- HubBase a9.0.0PR (default, Apr 15 2026, 19:49:17) ---")
                print("The first big update!!(Not done!)")
                print("Addition:")
                print("    - Added 'Turtle' programm №2(Pr16)(Pt1)!")
            elif D4 == "R":
                print("--- HubBase a9.0.0 (default, Apr 15 2026, 21:09:07) ---")
                print("The first big update!!")
                print("Addition:")
                print("    - Added 'Turtle' programm №2(Pr16)(Pt2)!")
            else:
                print("Such release does not exist or isn`t documented")
        if D3 == "1":
            if D4 == "R":
                print("--- HubBase a9.0.1 (default, Apr 19 2026, 10:31:44) ---")
                print("Bugfix №4!")
                print("Changes:")
                print("    - Fixed 'Programm16()' funky snowflakes bug")
            else:
                print("Such release does not exist or isn`t documented")
        if D3 == "2":
            if D4 == "R":
                print("--- HubBase a9.0.2 (default, Apr 19 2026, 18:41:07) ---")
                print("Bugfix №5!")
                print("Changes:")
                print("    - Fixed 'Pr-start' tracking only 2 and 14-16")
            else:
                print("Such release does not exist or isn`t documented")
        else:
            print("Such release does not exist or isn`t documented")
    else:
        print("Such release does not exist or isn`t documented")
elif D1 == "a0":
    if D2 == "1":
        if D3 == "0":
            if D4 == "R":
                print("The code:")
                print("Num = input('Number = ')")
                print("Num2 = input('Number2 = ')")
                print("print(Num + Num2)")
            else:
                print("Such release does not exist or isn`t documented")
        elif D3 == "1":
            if D4 == "R":
                print("The code:")
                print("Num = input('Number = ')")
                print("Num2 = input('Number2 = ')")
                print("num = int(Num)")
                print("num2 = int(Num2)")
                print("print(num + num2)")
            else:
                print("Such release does not exist or isn`t documented")
        else:
            print("Such release does not exist or isn`t documented")
    else:
        print("Such release does not exist or isn`t documented")
else:
    print("Such release does not exist or isn`t documented")
s = input("")
