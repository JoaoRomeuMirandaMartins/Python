from tkinter import*
import os
def Substituidor(OName,OPart,NPart):
    cont = len(OName) - 1
    while (OName[cont] != "." or cont > 0):
        cont = cont - 1
    NName = OName[0:cont].replace(OPart,NPart) + OName[cont:len(OName)]
    return NName
def Navegador():
    Path = "."
    while Path != "":
        os.chdir(Path)
        print("\n" + os.getcwd() + "\n")
        Path = os.listdir(".")
        Path.append("..")
        Path.sort()
        for file in Path:
            print(file)
        Path = input()
Command = "."
while Command != "":
    print("Command:",end = "")
    Command = input()
    if Command == "N":
        Navegador()
    else:
        if Command == "R":
            print("Encontrar:", end = "")
            OPart = input()
            print("Substituir:", end = "")
            NPart = input()
            Folder = os.listdir(".")
            for file in Folder:
                if not os.path.isdir(file):
                    os.rename(file, Substituidor(file, OPart, NPart))
                    print(file + " ==> " + Substituidor(file, OPart, NPart))
