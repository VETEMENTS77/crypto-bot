import os

def system_clear() -> None:
    if os.name == "nt":
       os.system("cls")
    else:
        os.system("clear")