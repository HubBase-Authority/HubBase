import time
print("Log v0 - Core")
print("Available: v1, v1.5, v2")
LogVersion = input("Which version(formula) to use? -- ")
if LogVersion == "1":
    print("Log v1 loading!")
    time.sleep(1)
    print("Complete")
    time.sleep(0.1)
    print("--- Version Backlog a8-a10.0.2 (default, Apr 30 2026) ---")
    print("V`s available are a8.0.0 - a10.0.2")
    print("Exceptions:")
    print("a0.1.0, a0.1.1, a2.7.19")
    print("Newest - a10, start - a8")
    D1 = input("The Main part -- ").lower()
    print("1,2,3 and so on")
    D2 = input("The addition -- ")
    print("1,2,3 and so on")
    D3 = input("The fix -- ")
    print("B - for betas, PR - for prereleases, R - for releases")
    D4 = input("Access to Version -- ").upper()
    print("The security updates are exclusive to the wiki!")
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
            elif D3 == "1":
                if D4 == "R":
                    print("--- HubBase a9.0.1 (default, Apr 19 2026, 10:31:44) ---")
                    print("Bugfix №4!")
                    print("Changes:")
                    print("    - Fixed 'Programm16()' funky snowflakes bug")
                else:
                    print("Such release does not exist or isn`t documented")
            elif D3 == "2":
                if D4 == "R":
                    print("--- HubBase a9.0.2 (default, Apr 19 2026, 18:41:07) ---")
                    print("Bugfix №5!")
                    print("Changes:")
                    print("    - Fixed 'Pr-start' tracking only 2 and 14-16")
                else:
                    print("Such release does not exist or isn`t documented")
            else:
                print("Such release does not exist or isn`t documented")
        if D2 == "1":
            if D3 == "0":
                if D4 == "R":
                    print("--- HubBase a9.1.0 (default, Apr 22 2026, 18:29:45) ---")
                    print("Addition №4!")
                    print("Changes:")
                    print("    - Added HubBasePE integration")
                else:
                    print("Such release does not exist or isn`t documented")
            elif D3 == "1":
                if D4 == "R":
                    print("--- HubBase a9.1.1 (default, Apr 22 2026, 19:35:59) ---")
                    print("Bugfix №6!")
                    print("Changes:")
                    print("    - Fixed HubBasePE integration not working")
                else:
                    print("Such release does not exist or isn`t documented")
            elif D3 == "2":
                if D4 == "R":
                    print("--- HubBase a9.1.2 (default, Apr 22 2026, 20:07:09) ---")
                    print("Bugfix №7!")
                    print("Changes:")
                    print("    - Fixed PE programm order!")
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
    elif D1 == "a2":
        if D2 == "7":
            if D3 == "19":
                if D4 == "R":
                    print("Release №1 with version number")
                    print("Featuring:")
                    print("    - 4 programms! (and the 5`th as a launchable)")
                    print("    - The name - №2!")
                    print("    - Vip`s!")
                else:
                    print("Such release does not exist or isn`t documented")
            else:
                print("Such release does not exist or isn`t documented")
        else:
            print("Such release does not exist or isn`t documented")
    elif D1 == "a10":
        if D2 == "0":
            if D3 == "0":
                if D4 == "B":
                    print("--- HubBase a10.0.0B (base - a9.1.2) (default, Apr 24 2026, 12:11:14) ---")
                    print("The second big update!!(Beta!)")
                    print("Addition:")
                    print("    - Added 'Tkinter' programm №1(Pr17)!")
                elif D4 == "PR":
                    print("--- HubBase a10.0.0PR (default, Apr 25 2026, 13:24:32) ---")
                    print("The second big update!!(Not done!)")
                    print("Addition:")
                    print("    - Added HubBasePE v0.0.1rc1.post1 support!")
                elif D4 == "R":
                    print("--- HubBase a10.0.0 (default, Apr 26 2026, 11:51:41) ---")
                    print("The second big update!!")
                    print("Addition:")
                    print("    - Added 'Tkinter' programm №2(Pr18)!")
                else:
                    print("Such release does not exist or isn`t documented")
            if D3 == "1":
                if D4 == "R":
                    print("--- HubBase a10.0.1 (default, Apr 29 2026, 20:26:45) ---")
                    print("Bugfix №8!")
                    print("Changes:")
                    print("    - Added HubBasePE v0.0.1rc2.post2 support!")
                else:
                    print("Such release does not exist or isn`t documented")
            if D3 == "2":
                if D4 == "R":
                    print("--- HubBase a10.0.2 (default, Apr 30 2026, 19:41:54) ---")
                    print("Bugfix №9!")
                    print("Changes:")
                    print("    - Updated V-B to a new formula, - v1.5")
                    print("    - Added 'Programm19()' as a launchable to HB")
                    print("This is the last documented release in Log v1")
                    print("The 1.0 log will not include >a10.0.2")
                else:
                    print("Such release does not exist or isn`t documented")
            else:
                print("Such release does not exist or isn`t documented")
        else:
            print("Such release does not exist or isn`t documented")
    else:
        print("Such release does not exist or isn`t documented")
elif LogVersion == "1.5":
    print("Log v1.5 loading!")
    time.sleep(0.8)
    print("Complete")
    time.sleep(0.2)
    print("--- Version Backlog a8-b1.0.0 (default, May 01 2026) ---")
    print("V`s available are a8.0.0 - b1.0.0")
    print("Exceptions:")
    print("a0.1.0, a0.1.1, a2.7.19")
    print("Newest - 0, start - a8")
    D1 = input("The Main part -- ").lower()
    print("0,1,2,3 and so on")
    D2 = input("The addition -- ")
    print("0,1,2,3 and so on")
    D3 = input("The fix -- ")
    print("b(n) - for betas, rc(n) - for prereleases, r - for releases")
    D4 = input("Access to Version -- ").lower()
    print("The security updates are exclusive to the wiki!")
    print("")
    if D1 == "a8":
        if D2 == "0":
            if D3 == "0":
                if D4 == "r":
                    print("--- HubBase a8.0.0 (default, Apr 10 2026) ---")
                    print("Official release!")
                    print("Featuring:")
                    print("    - 12 programms!")
                    print("    - Looped showcase!")
                    print("    - Vip`s!")
                else:
                    print("Such release does not exist or isn`t documented")
            elif D3 == "1":
                if D4 == "r":
                    print("--- HubBase a8.0.1 (default, Apr 10 2026) ---")
                    print("First bugfix!")
                    print("Changes:")
                    print("    - Fixed Version Number Bug!")
                else:
                    print("Such release does not exist or isn`t documented")
            elif D3 == "2":
                if D4 == "r":
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
                if D4 == "r":
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
                if D4 == "b1":
                    print("--- HubBase a8.2.0B (default, Apr 11 2026, 14:40:24) ---")
                    print("Addition №2!(not complete)")
                    print("Changes:")
                    print("    - Added 'Programm13()' as a launchable programm!")
                elif D4 == "r":
                    print("--- HubBase a8.2.0 (default, Apr 11 2026, 18:16:51) ---")
                    print("Addition №2!")
                    print("Changes:")
                    print("    - Added 'Programm13()' fully")
                else:
                    print("Such release does not exist or isn`t documented")
            elif D3 == "1":
                if D4 == "r":
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
                if D4 == "b1":
                    print("--- HubBase a8.3.0B (default, Apr 12 2026, 9:30:29) ---")
                    print("Addition №3!(in beta)")
                    print("Changes:")
                    print("    - Added 'Programm14()'(with bugs)")
                elif D4 == "r":
                    print("--- HubBase a8.3.0 (default, Apr 12 2026, 10:00:36) ---")
                    print("Addition №3!")
                    print("Changes:")
                    print("    - Added 'Programm14()' fully")
                else:
                    print("Such release does not exist or isn`t documented")
            elif D3 == "1":
                if D4 == "r":
                    print("--- HubBase a8.3.1 (default, Apr 12 2026, 10:42:57) ---")
                    print("Bugfix №3!")
                    print("Changes:")
                    print("    - Fixed 'Programm14()' not working for Decrypt mode")
                else:
                    print("Such release does not exist or isn`t documented")
            else:
                print("Such release does not exist or isn`t documented")
        else:
            print("Such release does not exist or isn`t documented")
    elif D1 == "a9":
        if D2 == "0":
            if D3 == "0":
                if D4 == "b1":
                    print("--- HubBase a9.0.0B (default, Apr 12 2026, 21:17:18) ---")
                    print("The first big update!!(Beta!)")
                    print("Addition:")
                    print("    - Added 'Turtle' programm №1(Pr15)!")
                elif D4 == "rc1":
                    print("--- HubBase a9.0.0PR (default, Apr 15 2026, 19:49:17) ---")
                    print("The first big update!!(Not done!)")
                    print("Addition:")
                    print("    - Added 'Turtle' programm №2(Pr16)(Pt1)!")
                elif D4 == "r":
                    print("--- HubBase a9.0.0 (default, Apr 15 2026, 21:09:07) ---")
                    print("The first big update!!")
                    print("Addition:")
                    print("    - Added 'Turtle' programm №2(Pr16)(Pt2)!")
                else:
                    print("Such release does not exist or isn`t documented")
            elif D3 == "1":
                if D4 == "r":
                    print("--- HubBase a9.0.1 (default, Apr 19 2026, 10:31:44) ---")
                    print("Bugfix №4!")
                    print("Changes:")
                    print("    - Fixed 'Programm16()' funky snowflakes bug")
                else:
                    print("Such release does not exist or isn`t documented")
            elif D3 == "2":
                if D4 == "r":
                    print("--- HubBase a9.0.2 (default, Apr 19 2026, 18:41:07) ---")
                    print("Bugfix №5!")
                    print("Changes:")
                    print("    - Fixed 'Pr-start' tracking only 2 and 14-16")
                else:
                    print("Such release does not exist or isn`t documented")
            else:
                print("Such release does not exist or isn`t documented")
        if D2 == "1":
            if D3 == "0":
                if D4 == "r":
                    print("--- HubBase a9.1.0 (default, Apr 22 2026, 18:29:45) ---")
                    print("Addition №4!")
                    print("Changes:")
                    print("    - Added HubBasePE integration")
                else:
                    print("Such release does not exist or isn`t documented")
            elif D3 == "1":
                if D4 == "r":
                    print("--- HubBase a9.1.1 (default, Apr 22 2026, 19:35:59) ---")
                    print("Bugfix №6!")
                    print("Changes:")
                    print("    - Fixed HubBasePE integration not working")
                else:
                    print("Such release does not exist or isn`t documented")
            elif D3 == "2":
                if D4 == "r":
                    print("--- HubBase a9.1.2 (default, Apr 22 2026, 20:07:09) ---")
                    print("Bugfix №7!")
                    print("Changes:")
                    print("    - Fixed PE programm order!")
                else:
                    print("Such release does not exist or isn`t documented")
            else:
                print("Such release does not exist or isn`t documented")
        else:
            print("Such release does not exist or isn`t documented")
    elif D1 == "a0":
        if D2 == "1":
            if D3 == "0":
                if D4 == "r":
                    print("The code:")
                    print("Num = input('Number = ')")
                    print("Num2 = input('Number2 = ')")
                    print("print(Num + Num2)")
                else:
                    print("Such release does not exist or isn`t documented")
            elif D3 == "1":
                if D4 == "r":
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
    elif D1 == "a2":
        if D2 == "7":
            if D3 == "19":
                if D4 == "r":
                    print("Release №1 with version number")
                    print("Featuring:")
                    print("    - 4 programms! (and the 5`th as a launchable)")
                    print("    - The name - №2!")
                    print("    - Vip`s!")
                else:
                    print("Such release does not exist or isn`t documented")
            else:
                print("Such release does not exist or isn`t documented")
        else:
            print("Such release does not exist or isn`t documented")
    elif D1 == "a10":
        if D2 == "0":
            if D3 == "0":
                if D4 == "b1":
                    print("--- HubBase a10.0.0B (base - a9.1.2) (default, Apr 24 2026, 12:11:14) ---")
                    print("The second big update!!(Beta!)")
                    print("Addition:")
                    print("    - Added 'Tkinter' programm №1(Pr17)!")
                elif D4 == "rc1":
                    print("--- HubBase a10.0.0PR (default, Apr 25 2026, 13:24:32) ---")
                    print("The second big update!!(Not done!)")
                    print("Addition:")
                    print("    - Added HubBasePE v0.0.1rc1.post1 support!")
                elif D4 == "r":
                    print("--- HubBase a10.0.0 (default, Apr 26 2026, 11:51:41) ---")
                    print("The second big update!!")
                    print("Addition:")
                    print("    - Added 'Tkinter' programm №2(Pr18)!")
                else:
                    print("Such release does not exist or isn`t documented")
            if D3 == "1":
                if D4 == "r":
                    print("--- HubBase a10.0.1 (default, Apr 29 2026, 20:26:45) ---")
                    print("Bugfix №8!")
                    print("Changes:")
                    print("    - Added HubBasePE v0.0.1rc2.post2 support!")
                else:
                    print("Such release does not exist or isn`t documented")
            if D3 == "2":
                if D4 == "r":
                    print("--- HubBase a10.0.2 (default, Apr 30 2026, 19:41:54) ---")
                    print("Bugfix №9!")
                    print("Changes:")
                    print("    - Updated V-B to a new formula, - v1.5")
                    print("    - Added 'Programm19()' as a launchable to HB")
                else:
                    print("Such release does not exist or isn`t documented")
            else:
                print("Such release does not exist or isn`t documented")
        else:
            print("Such release does not exist or isn`t documented")
    elif D1 == "b1":
        if D2 == "0":
            if D3 == "1":
                if D4 == "b1":
                    print("--- HubBase 0.0.1b1 (default, Apr 30 2026, 20:06:58) ---")
                    print("The first GIGANTIC update!!(in beta)")
                    print("Addition:")
                    print("    - Added 'Minesweeper'(Pr19)(Pt1)!")
                elif D4 == "b2":
                    print("--- HubBase 0.0.1b2 (default, Apr 30 2026, 20:29:47) ---")
                    print("The first GIGANTIC update(in beta)!!")
                    print("Addition:")
                    print("    - Added 'Minesweeper'(Pr19)(Pt2)!")
                elif D4 == "b3":
                    print("--- HubBase 0.0.1b3 (default, Apr 30 2026, 20:41:24) ---")
                    print("The first GIGANTIC update(in beta)!!")
                    print("Addition:")
                    print("    - Added 'Minesweeper'(Pr19)(Pt3.1)!")
                elif D4 == "b4":
                    print("--- HubBase 0.0.1b4 (default, Apr 30 2026, 20:46:45) ---")
                    print("The first GIGANTIC update(in beta)!!")
                    print("Addition:")
                    print("    - Fixed 'Minesweeper'(Pr19)(Pt2+3.1)!")
                elif D4 == "b5":
                    print("--- HubBase 0.0.1b5 (default, May 01 2026, 19:29:35) ---")
                    print("The first GIGANTIC update(in beta)!!")
                    print("Addition:")
                    print("    - Fixed 'Minesweeper'(Pr19)(Pt3)!")
                elif D4 == "rc1":
                    print("--- HubBase 0.0.1rc1 (default, May 02 2026, 19:52:54) ---")
                    print("The first GIGANTIC update(not done!)!!")
                    print("Addition:")
                    print("    - Added 'Minesweeper'(Pr19)(Pt4)!")
                elif D4 == "rc2":
                    print("--- HubBase 0.0.1rc2 (default, May 02 2026, 21:04:43) ---")
                    print("The first GIGANTIC update(not done!)!!")
                    print("Addition:")
                    print("    - Fixed 'Minesweeper'(Pr19)(Pt4) CheckBombs bug!")
                elif D4 == "r":
                    print("--- HubBase 0.0.1.0.00 (default, May 10 2026, 19:37:54) ---")
                    print("The first GIGANTIC update!!")
                    print("Addition:")
                    print("    - Added 'Minesweeper'(Pr19) fully!")
                    print("    - Added HubBasePE v0.0.1 support!")
                else:
                    print("Such release does not exist or isn`t documented")
            else:
                print("Such release does not exist or isn`t documented")
        else:
            print("Such release does not exist or isn`t documented")
    else:
        print("Such release does not exist or isn`t documented")
elif LogVersion == "2":
    print("True version number - v2.1.0.0")
    print("Log v2 loading!")
    time.sleep(3)
    print("Complete")
    time.sleep(0.5)
    print("--- Version Backlog 0.0.0.8-0.0.1.0.00 (default, May 10 2026) ---")
    print("V`s available are 0.0.0.8 = a8(I`m lazy so use a(n)) - 0.0.1.0.00")
    print("Exceptions:")
    print("a0.1.0, a0.1.1, a2.7.19")
    print("Newest - 0, start - a8(use a(n)) = 0")
    D1 = input("The Main part -- ").lower()
    print("0,1,2,3 and so on")
    D2 = input("The addition -- ")
    print("0,1,2,3 and so on")
    D3 = input("The fix -- ")
    print("0.00, 0.01, ..., 0.10, 1.00, and so on")
    D5 = input("Extras(Doesn`t matter for 0.0.1<) -- ")
    print("a(n) - for alphas, b(n) - for betas, rc(n) - for prereleases, r - for releases")
    D4 = input("Access to Version -- ").lower()
    print("The security updates are exclusive to the wiki!")
    print("")
    if D1 == "a8":
        if D2 == "0":
            if D3 == "0":
                if D4 == "r":
                    print("--- HubBase a8.0.0 (default, Apr 10 2026) ---")
                    print("Official release!")
                    print("Featuring:")
                    print("    - 12 programms!")
                    print("    - Looped showcase!")
                    print("    - Vip`s!")
                else:
                    print("Such release does not exist or isn`t documented")
            elif D3 == "1":
                if D4 == "r":
                    print("--- HubBase a8.0.1 (default, Apr 10 2026) ---")
                    print("First bugfix!")
                    print("Changes:")
                    print("    - Fixed Version Number Bug!")
                else:
                    print("Such release does not exist or isn`t documented")
            elif D3 == "2":
                if D4 == "r":
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
                if D4 == "r":
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
                if D4 == "b1":
                    print("--- HubBase a8.2.0B (default, Apr 11 2026, 14:40:24) ---")
                    print("Addition №2!(not complete)")
                    print("Changes:")
                    print("    - Added 'Programm13()' as a launchable programm!")
                elif D4 == "r":
                    print("--- HubBase a8.2.0 (default, Apr 11 2026, 18:16:51) ---")
                    print("Addition №2!")
                    print("Changes:")
                    print("    - Added 'Programm13()' fully")
                else:
                    print("Such release does not exist or isn`t documented")
            elif D3 == "1":
                if D4 == "r":
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
                if D4 == "b1":
                    print("--- HubBase a8.3.0B (default, Apr 12 2026, 9:30:29) ---")
                    print("Addition №3!(in beta)")
                    print("Changes:")
                    print("    - Added 'Programm14()'(with bugs)")
                elif D4 == "r":
                    print("--- HubBase a8.3.0 (default, Apr 12 2026, 10:00:36) ---")
                    print("Addition №3!")
                    print("Changes:")
                    print("    - Added 'Programm14()' fully")
                else:
                    print("Such release does not exist or isn`t documented")
            elif D3 == "1":
                if D4 == "r":
                    print("--- HubBase a8.3.1 (default, Apr 12 2026, 10:42:57) ---")
                    print("Bugfix №3!")
                    print("Changes:")
                    print("    - Fixed 'Programm14()' not working for Decrypt mode")
                else:
                    print("Such release does not exist or isn`t documented")
            else:
                print("Such release does not exist or isn`t documented")
        else:
            print("Such release does not exist or isn`t documented")
    elif D1 == "a9":
        if D2 == "0":
            if D3 == "0":
                if D4 == "b1":
                    print("--- HubBase a9.0.0B (default, Apr 12 2026, 21:17:18) ---")
                    print("The first big update!!(Beta!)")
                    print("Addition:")
                    print("    - Added 'Turtle' programm №1(Pr15)!")
                elif D4 == "rc1":
                    print("--- HubBase a9.0.0PR (default, Apr 15 2026, 19:49:17) ---")
                    print("The first big update!!(Not done!)")
                    print("Addition:")
                    print("    - Added 'Turtle' programm №2(Pr16)(Pt1)!")
                elif D4 == "r":
                    print("--- HubBase a9.0.0 (default, Apr 15 2026, 21:09:07) ---")
                    print("The first big update!!")
                    print("Addition:")
                    print("    - Added 'Turtle' programm №2(Pr16)(Pt2)!")
                else:
                    print("Such release does not exist or isn`t documented")
            elif D3 == "1":
                if D4 == "r":
                    print("--- HubBase a9.0.1 (default, Apr 19 2026, 10:31:44) ---")
                    print("Bugfix №4!")
                    print("Changes:")
                    print("    - Fixed 'Programm16()' funky snowflakes bug")
                else:
                    print("Such release does not exist or isn`t documented")
            elif D3 == "2":
                if D4 == "r":
                    print("--- HubBase a9.0.2 (default, Apr 19 2026, 18:41:07) ---")
                    print("Bugfix №5!")
                    print("Changes:")
                    print("    - Fixed 'Pr-start' tracking only 2 and 14-16")
                else:
                    print("Such release does not exist or isn`t documented")
            else:
                print("Such release does not exist or isn`t documented")
        if D2 == "1":
            if D3 == "0":
                if D4 == "r":
                    print("--- HubBase a9.1.0 (default, Apr 22 2026, 18:29:45) ---")
                    print("Addition №4!")
                    print("Changes:")
                    print("    - Added HubBasePE integration")
                else:
                    print("Such release does not exist or isn`t documented")
            elif D3 == "1":
                if D4 == "r":
                    print("--- HubBase a9.1.1 (default, Apr 22 2026, 19:35:59) ---")
                    print("Bugfix №6!")
                    print("Changes:")
                    print("    - Fixed HubBasePE integration not working")
                else:
                    print("Such release does not exist or isn`t documented")
            elif D3 == "2":
                if D4 == "r":
                    print("--- HubBase a9.1.2 (default, Apr 22 2026, 20:07:09) ---")
                    print("Bugfix №7!")
                    print("Changes:")
                    print("    - Fixed PE programm order!")
                else:
                    print("Such release does not exist or isn`t documented")
            else:
                print("Such release does not exist or isn`t documented")
        else:
            print("Such release does not exist or isn`t documented")
    elif D1 == "a0":
        if D2 == "1":
            if D3 == "0":
                if D4 == "r":
                    print("The code:")
                    print("Num = input('Number = ')")
                    print("Num2 = input('Number2 = ')")
                    print("print(Num + Num2)")
                else:
                    print("Such release does not exist or isn`t documented")
            elif D3 == "1":
                if D4 == "r":
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
    elif D1 == "a2":
        if D2 == "7":
            if D3 == "19":
                if D4 == "r":
                    print("Release №1 with version number")
                    print("Featuring:")
                    print("    - 4 programms! (and the 5`th as a launchable)")
                    print("    - The name - №2!")
                    print("    - Vip`s!")
                else:
                    print("Such release does not exist or isn`t documented")
            else:
                print("Such release does not exist or isn`t documented")
        else:
            print("Such release does not exist or isn`t documented")
    elif D1 == "a10":
        if D2 == "0":
            if D3 == "0":
                if D4 == "b1":
                    print("--- HubBase a10.0.0B (base - a9.1.2) (default, Apr 24 2026, 12:11:14) ---")
                    print("The second big update!!(Beta!)")
                    print("Addition:")
                    print("    - Added 'Tkinter' programm №1(Pr17)!")
                elif D4 == "rc1":
                    print("--- HubBase a10.0.0PR (default, Apr 25 2026, 13:24:32) ---")
                    print("The second big update!!(Not done!)")
                    print("Addition:")
                    print("    - Added HubBasePE v0.0.1rc1.post1 support!")
                elif D4 == "r":
                    print("--- HubBase a10.0.0 (default, Apr 26 2026, 11:51:41) ---")
                    print("The second big update!!")
                    print("Addition:")
                    print("    - Added 'Tkinter' programm №2(Pr18)!")
                else:
                    print("Such release does not exist or isn`t documented")
            if D3 == "1":
                if D4 == "r":
                    print("--- HubBase a10.0.1 (default, Apr 29 2026, 20:26:45) ---")
                    print("Bugfix №8!")
                    print("Changes:")
                    print("    - Added HubBasePE v0.0.1rc2.post2 support!")
                else:
                    print("Such release does not exist or isn`t documented")
            if D3 == "2":
                if D4 == "r":
                    print("--- HubBase a10.0.2 (default, Apr 30 2026, 19:41:54) ---")
                    print("Bugfix №9!")
                    print("Changes:")
                    print("    - Updated V-B to a new formula, - v1.5")
                    print("    - Added 'Programm19()' as a launchable to HB")
                else:
                    print("Such release does not exist or isn`t documented")
            else:
                print("Such release does not exist or isn`t documented")
        else:
            print("Such release does not exist or isn`t documented")
    elif D1 == "0":
        if D2 == "0":
            if D3 == "1":
                if D5 == "0.00":
                    if D4 == "b1":
                        print("--- HubBase 0.0.1b1 (default, Apr 30 2026, 20:06:58) ---")
                        print("The first GIGANTIC update(in beta)!!")
                        print("Addition:")
                        print("    - Added 'Minesweeper'(Pr19)(Pt1)!")
                    elif D4 == "b2":
                        print("--- HubBase 0.0.1b2 (default, Apr 30 2026, 20:29:47) ---")
                        print("The first GIGANTIC update(in beta)!!")
                        print("Addition:")
                        print("    - Added 'Minesweeper'(Pr19)(Pt2)!")
                    elif D4 == "b3":
                        print("--- HubBase 0.0.1b3 (default, Apr 30 2026, 20:41:24) ---")
                        print("The first GIGANTIC update(in beta)!!")
                        print("Addition:")
                        print("    - Added 'Minesweeper'(Pr19)(Pt3)!")
                    elif D4 == "b4":
                        print("--- HubBase 0.0.1b4 (default, Apr 30 2026, 20:46:45) ---")
                        print("The first GIGANTIC update(in beta)!!")
                        print("Addition:")
                        print("    - Fixed 'Minesweeper'(Pr19)(Pt2+3)!")
                    elif D4 == "b5":
                        print("--- HubBase 0.0.1b5 (default, May 01 2026, 19:29:35) ---")
                        print("The first GIGANTIC update(in beta)!!")
                        print("Addition:")
                        print("    - Fixed 'Minesweeper'(Pr19)(Pt3)!")
                    elif D4 == "rc1":
                        print("--- HubBase 0.0.1rc1 (default, May 02 2026, 19:52:54) ---")
                        print("The first GIGANTIC update(not done!)!!")
                        print("Addition:")
                        print("    - Added 'Minesweeper'(Pr19)(Pt4)!")
                    elif D4 == "rc2":
                        print("--- HubBase 0.0.1rc2 (default, May 02 2026, 21:04:43) ---")
                        print("The first GIGANTIC update(not done!)!!")
                        print("Addition:")
                        print("    - Fixed 'Minesweeper'(Pr19)(Pt4) CheckBombs bug!")
                    elif D4 == "r":
                        print("--- HubBase 0.0.1.0.00 (default, May 10 2026, 10:56:54) ---")
                        print("The first GIGANTIC update!!")
                        print("Addition:")
                        print("    - Added 'Minesweeper'(Pr19) fully!")
                        print("    - Added HubBasePE v0.0.1.0.00 support!")
                    else:
                        print("Such release does not exist or isn`t documented")
                if D5 == "0.10":
                    if D4 == "r":
                        print("--- HubBase 0.0.1.0.10 (default, May 13 2026, 20:19:52) ---")
                        print("Addition №5!")
                        print("Changes:")
                        print("    - Added HubBasePE v0.0.1.0.10 support!")
                    else:
                        print("Such release does not exist or isn`t documented")
                if D5 == "1.00":
                    if D4 == "r":
                        print("--- HubBase 0.0.1.1.00 (default, May 23 2026, 22:06:12) ---")
                        print("Addition №6!")
                        print("Changes:")
                        print("    - Added advanced login system!")
                    else:
                        print("Such release does not exist or isn`t documented")
                if D5 == "2.00":
                    if D4 == "r":
                        print("--- HubBase 0.0.1.2.00 (default, May 24 2026, 12:56:45) ---")
                        print("Addition №7!")
                        print("Changes:")
                        print("    - Added dev console!")
                    else:
                        print("Such release does not exist or isn`t documented")
                if D5 == "2.01":
                    if D4 == "r":
                        print("--- HubBase 0.0.1.2.01 (default, May 24 2026, 14:03:54) ---")
                        print("Bugfix №10!")
                        print("Changes:")
                        print("    - Fixed dev console!")
                    else:
                        print("Such release does not exist or isn`t documented")
                else:
                    print("Such release does not exist or isn`t documented")
            if D3 == "1":
                if D5 == "0.00":
                    if D4 == "b1":
                        print("--- HubBase 0.0.2.0.00b1 (default, May 24 2026, 22:03:41) ---")
                        print("The second GIGANTIC update(in beta)!!")
                        print("Addition:")
                        print("    - Added 'Tennis'(Pr20)(Pt1)!")
                    elif D4 == "b2":
                        print("--- HubBase 0.0.2.0.00b2 (default, May 25 2026, 22:03:41) ---")
                        print("The second GIGANTIC update(in beta)!!")
                        print("Addition:")
                        print("    - Added 'Tennis'(Pr20)(Pt2)!")
                    else:
                        print("Such release does not exist or isn`t documented")
            else:
                print("Such release does not exist or isn`t documented")
        else:
            print("Such release does not exist or isn`t documented")
    else:
        print("Such release does not exist or isn`t documented")
else:
    print("Such Log does not exist.")
s = input("")
