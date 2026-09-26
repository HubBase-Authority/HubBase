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



    
