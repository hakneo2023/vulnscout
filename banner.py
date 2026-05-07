import os
import time
import random

HACK_NEO_ASCII = r"""
██╗  ██╗ █████╗  ██████╗██╗  ██╗    ███╗   ██╗███████╗ ██████╗ 
██║  ██║██╔══██╗██╔════╝██║ ██╔╝    ████╗  ██║██╔════╝██╔═══██╗
███████║███████║██║     █████╔╝     ██╔██╗ ██║█████╗  ██║   ██║
██╔══██║██╔══██║██║     ██╔═██╗     ██║╚██╗██║██╔══╝  ██║   ██║
██║  ██║██║  ██║╚██████╗██║  ██╗    ██║ ╚████║███████╗╚██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═╝  ╚═══╝╚══════╝ ╚═════╝ 
                     >>> HACK-NEO <<<
"""

def matrix_banner(text):
    os.system("cls" if os.name == "nt" else "clear")
    lines = text.split("\n")
    max_len = max(len(line) for line in lines)

    # Effetto Matrix iniziale
    for _ in range(20):
        os.system("cls" if os.name == "nt" else "clear")
        for _ in range(len(lines)):
            row = "".join(random.choice("01") for _ in range(max_len))
            print(f"\033[32m{row}\033[0m")
        time.sleep(0.05)

    # Reveal del banner
    os.system("cls" if os.name == "nt" else "clear")
    for line in lines:
        reveal = ""
        for char in line:
            reveal += char
            print(f"\033[32m{reveal}\033[0m", end="\r")
            time.sleep(0.002)
        print(f"\033[32m{reveal}\033[0m")
        time.sleep(0.02)

    print("\n\033[92mby_dany\033[0m\n")


def matrix_end_animation():
    os.system("cls" if os.name == "nt" else "clear")
    print("\n")

    for _ in range(15):
        row = "".join(random.choice("01") for _ in range(80))
        print(f"\033[32m{row}\033[0m")
        time.sleep(0.03)

    print("\n\033[92mSCAN COMPLETED — by_dany\033[0m\n")
    time.sleep(1)
