import pyautogui
import time
import os
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text

# simple "write" function for writing txt to the screen
def write(msg):
    pyautogui.write(msg)

# configuration file for organising the modules into a dictionary
# [very messy]
def configuration():
    with open("settings.cfg","r") as s:
        settings = s.readlines()
        drone_modules = {
            str(settings[0].split("=")[0]): eval(settings[0].split("=")[1]),
            str(settings[1].split("=")[0]): eval(settings[1].split("=")[1]),
            str(settings[2].split("=")[0]): eval(settings[2].split("=")[1]),
            str(settings[3].split("=")[0]): eval(settings[3].split("=")[1]),
            str(settings[4].split("=")[0]): eval(settings[4].split("=")[1]),
            str(settings[5].split("=")[0]): eval(settings[5].split("=")[1]),
            str(settings[6].split("=")[0]): eval(settings[6].split("=")[1]),
            str(settings[7].split("=")[0]): eval(settings[7].split("=")[1]),
            str(settings[8].split("=")[0]): eval(settings[8].split("=")[1]),
            str(settings[9].split("=")[0]): eval(settings[9].split("=")[1]),
            str(settings[10].split("=")[0]): eval(settings[10].split("=")[1]),
            str(settings[11].split("=")[0]): eval(settings[11].split("=")[1]),
            str(settings[12].split("=")[0]): eval(settings[12].split("=")[1]),
            str(settings[13].split("=")[0]): eval(settings[13].split("=")[1]),
            str(settings[14].split("=")[0]): eval(settings[14].split("=")[1]),
            str(settings[15].split("=")[0]): eval(settings[15].split("=")[1]),
            str(settings[16].split("=")[0]): eval(settings[16].split("=")[1]),
            str(settings[17].split("=")[0]): eval(settings[17].split("=")[1]),
            str(settings[18].split("=")[0]): eval(settings[18].split("=")[1]),
            str(settings[19].split("=")[0]): eval(settings[19].split("=")[1]),
            str(settings[20].split("=")[0]): eval(settings[20].split("=")[1]),
            str(settings[21].split("=")[0]): eval(settings[21].split("=")[1]),
            str(settings[22].split("=")[0]): eval(settings[22].split("=")[1]),
            str(settings[23].split("=")[0]): eval(settings[23].split("=")[1]),
            str(settings[24].split("=")[0]): eval(settings[24].split("=")[1])
        }
        return drone_modules

# simple function for making a new console and clearing the screen
def new_console():
    os.system("title Drones Rewrite Macro - Made by: Pyco VR#5264")
    os.system("cls")
    return Console()


def main():
    settings = configuration()

    console = new_console()
    title1 = Text("Drones Rewrite",justify="center")
    title1.stylize("cyan")
    main = Text("Macro made by: Pyco VR#5264")
    main.stylize("red")
    console.print(Panel(f"{title1}\n{main}",expand=False))
    Prompt.prompt_suffix = ""
    drone_id = Prompt.ask("[cyan]Enter your drone ID: [/cyan]")
    time.sleep(1)

    for m in settings:
        if settings[m] == True:
            pyautogui.write(f"addmodule {drone_id} {m}")
            time.sleep(0.1)
            pyautogui.press("enter")

if __name__ == "__main__":
    main()