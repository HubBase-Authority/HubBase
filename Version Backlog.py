print("--- Version Backlog a8-a8.2.1 (default, Apr 11 2026) ---")
print("V`s available are a8.0.0 - a8.2.1")
print("Newest - a8, start - a8")
D1 = input("The Main part -- ").lower()
print("1,2,3 and so on")
D2 = input("The addition -- ")
print("1,2,3 and so on")
D3 = input("The fix -- ")
print("B - for betas, R - for releases")
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
    else:
        print("Such release does not exist or isn`t documented")
else:
    print("Such release does not exist or isn`t documented")
s = input("")
