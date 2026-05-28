print("Wait a second...")
import sys
import webbrowser
import tkinter as tk
from datetime import date
from tkinter import messagebox
root = tk.Tk()
root.withdraw()

mode = "console"
print("Successfully imported all needed libs")
launched = True
responsemalware = tk.messagebox.askyesno("creosh", "creosh does have Protection mode, which disables malware apps. Do you want to enable it? You can also change your choice later using protection command.")

if responsemalware:
    protection = True
else:
    protection = False

print("Welcome to creosh\nby peoqafLy Corporation ||| powered by Python\nEnter any command or use help!")

# list of apps (commands) add anythin u want lal
allowed_apps = ["help", "exit", "protection", "version", "chrome", "telegram", "vscode", "steam", "discord", "firefox", "navidrome", "vlc", "transmission", "qbittorrent", "vivaldi", "element", "spotify", "adwcleaner", "prismlauncher", "epicgames"]
allowed_apps.sort()

# list of actual links (May 2026)  If you added something below, add it in allowed_apps too.
    # list of safe apps
link = {
    "chrome": "https://google.com/chrome",
    "telegram": "https://telegram.org",
    "vscode": "https://code.visualstudio.com",
    "steam": "https://store.steampowered.com",
    "discord": "https://discord.com",
    "firefox": "https://firefox.com",
    "navidrome": "https://navidrome.org",
    "vlc": "https://www.videolan.org",
    "transmission": "https://transmissionbt.com",
    "qbittorrent": "https://www.qbittorrent.org",
    "vivaldi": "https://vivaldi.com",
    "element": "https://element.io",
    "spotify": "https://open.spotify.com/download",
    "adwcleaner": "https://www.malwarebytes.com/adwcleaner",
    "prismlauncher": "https://prismlauncher.org",
    "epicgames": "https://store.epicgames.com",
}
    # list of sus apps, cannot be opened if protection mode is True.
link_protect = {
    # usage example   "name": "link",
}

while True:
    userinput = input()

    if (userinput not in allowed_apps):
        print("not found. Try again...")

    if (userinput == "help"):
        print("allowed commands:")
        print(allowed_apps)

    if (userinput == "exit"):
        print("Okay!")
        sys.exit(0)

    if (userinput == "version"):
        tk.messagebox.showinfo("creosh","version 1.3\nby peoqafLy\nAll product names, logos, and brands are property of their respective owners. All company, product, and service names used in this software are for identification purposes only.\n Repository: github.com/gartriss/creosh")
        

    if (userinput == "protection"):
        responsemalware = tk.messagebox.askyesno("creosh", "creosh does have Protection mode, which disables malware apps. Do you want to enable it?")
        if responsemalware:
            protection = True
        else:
            protection = False
      
    def openlink():
         webbrowser.open(link[userinput])
         print("opened in your default browser.")

    def openlink_safe():
         webbrowser.open(link_protect[userinput])
         print("opened in your default browser.")

    if (userinput in link):
        openlink()
    
    if (userinput in link_protect):
        if (protection == True):
            print("You have protection mode enabled. Turn it off to install this app.")
        else:
            openlink_safe()
