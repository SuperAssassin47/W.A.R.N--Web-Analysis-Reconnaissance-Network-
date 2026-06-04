from main import App_Entry_Point
import sys
import os

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def app():
    running = True
    while running:
        clear_console()
        print("|| ===== W.A.R.N - Web Analysis & Reconnaissance Network\n ===== ||")

        print("Welcome to W.A.R.N, please select a module to initiate: \n")

        print("1. W.A.R.N.-EMDE (Embedded Malware Detection Engine)")
        print("2. Exit W.A.R.N")

        data = input("> ").strip()

        if data == "1":
            clear_console() # clears the console
            App_Entry_Point() # runs EMDE module
        elif data == "2":
            print("Exiting W.A.R.N -- Stay safe out there")
            sys.exit()
        else:
            print("[!] Error! No module found")
            # continue loop if invalid option is entered.

if __name__ == "__main__":
    app() # runs the app and displays main menu
