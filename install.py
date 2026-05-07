import os
import sys
import time
import random

GREEN = "\033[92m"
CYAN = "\033[96m"
RED = "\033[91m"
RESET = "\033[0m"


# Effetto digitazione
def typewriter(text, delay=0.03, color=GREEN):
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()


# Effetto Matrix
def matrix_line(width=40):
    chars = "abcdefghijklmnopqrstuvwxyz0123456789@#$%&*"
    return "".join(random.choice(chars) for _ in range(width))


def matrix_rain(lines=8, width=40, speed=0.05):
    for _ in range(lines):
        print(GREEN + matrix_line(width) + RESET)
        time.sleep(speed)


def banner():
    print(GREEN + r"""
██╗   ██╗██╗   ██╗██╗     ███╗   ██╗███████╗ ██████╗ ██████╗ ██╗   ██╗
██║   ██║██║   ██║██║     ████╗  ██║██╔════╝██╔════╝ ██╔══██╗╚██╗ ██╔╝
██║   ██║██║   ██║██║     ██╔██╗ ██║█████╗  ██║  ███╗██████╔╝ ╚████╔╝ 
╚██╗ ██╔╝██║   ██║██║     ██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗  ╚██╔╝  
 ╚████╔╝ ╚██████╔╝███████╗██║ ╚████║███████╗╚██████╔╝██║  ██║   ██║   
  ╚═══╝   ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
    """ + RESET)

    typewriter(">>> VulnScout – Hacker Intelligence Suite Installer <<<", 0.01, CYAN)
    typewriter("by hack_neo\n", 0.05, GREEN)


def main():
    os.system("clear" if os.name != "nt" else "cls")

    banner()
    matrix_rain()

    typewriter("Questo installer configurerà le API Key Twilio per Phone Intelligence.\n", 0.02)

    # Input API Key
    typewriter("Inserisci TWILIO_API_KEY_SID:", 0.02, CYAN)
    sid = input(GREEN + "> " + RESET).strip()

    typewriter("Inserisci TWILIO_API_KEY_SECRET:", 0.02, CYAN)
    secret = input(GREEN + "> " + RESET).strip()

    if not sid or not secret:
        print(RED + "\n[ERRORE] Devi inserire entrambe le chiavi." + RESET)
        return

    # Scrittura file .env
    env_content = f'TWILIO_API_KEY_SID="{sid}"\nTWILIO_API_KEY_SECRET="{secret}"\n'

    with open(".env", "w") as f:
        f.write(env_content)

    typewriter("\n[✓] File .env creato con successo!", 0.02, GREEN)
    typewriter("[✓] API Key configurate correttamente!", 0.02, GREEN)

    matrix_rain(lines=4, speed=0.03)

    typewriter("\nOra puoi avviare VulnScout normalmente:", 0.03, CYAN)
    typewriter("   python3 main.py\n", 0.05, GREEN)


if __name__ == "__main__":
    main()
