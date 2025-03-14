import os
import random
import time

#vars
fancy_linux_messages = ["'/nonexistent': No such file or directory",
    "mkdir: cannot create directory ‘test_folder’: File exists",
    "rm: it is dangerous to operate recursively on '/'\nrm: use --no-preserve-root to override this failsafe",
    "touch: cannot touch '/root/file.txt': Permission denied",
    "cat: file.txt: Permission denied",
    "PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.\n64 bytes from 8.8.8.8: icmp_seq=1 ttl=118 time=12.4 ms\n64 bytes from 8.8.8.8: icmp_seq=2 ttl=118 time=11.2 ms\n--- 8.8.8.8 ping statistics ---\n2 packets transmitted, 2 received, 0% packet loss, time 1001ms",
    "[1] 12345",
    "[1]+  Terminated              sleep 10",
    "Filesystem      Size  Used Avail Use% Mounted on\n/dev/sda1       50G   20G   27G  43% /\ntmpfs           2.0G  4.0M  2.0G   1% /run",
    "Reading package lists... Done\nBuilding dependency tree... Done\nThe following packages will be upgraded:\n  libc6\n1 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.",
    "E: Unable to locate package somepackage",
    "Command 'somecommand' not found, but can be installed with:\napt install somepackage",
    "tar: archive.tar: Cannot open: No such file or directory",
    "tar: Exiting with failure status due to previous errors",
    "Segmentation fault (core dumped)",
    "Connection to 192.168.1.1 closed by remote host.",
    "ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)",
    "cp: cannot stat 'file.txt': No such file or directory",
    "mv: cannot move 'file1' to 'file2': Permission denied",
    "mount: only root can use '--options' option",
    "umount: /mnt: target is busy.",
    "df: cannot read table of mounted file systems: No such file or directory",
    "dd: error writing '/dev/sdb': No space left on device",
    "rsync: failed to set times on '/backup': Operation not permitted",
    "Error: Could not connect to the server",
    "ssh: connect to host 192.168.1.100 port 22: Connection refused",
    "fatal: Not a git repository (or any of the parent directories): .git",
    "journalctl: Failed to get journal fields: No data available",
    "systemctl: Unit not found.",
    "Error: disk /dev/sda does not exist",
    "grep: somefile.txt: No such file or directory",
    "sed: -e expression #1, char 3: unknown command: `x'",
    "awk: syntax error at source line 1",
    "find: ‘/root’: Permission denied",
    "make: *** No targets specified and no makefile found.  Stop.",
    "bash: syntax error near unexpected token `('",
    "bash: ./some_script.sh: Permission denied",
    "htop: command not found",
    "vim: E37: No write since last change (use ! to override)",
    "nano: Error opening file somefile.txt: Permission denied",
    "dmesg: command not found",
    "firefox: error while loading shared libraries: libX11.so.6: cannot open shared object file: No such file or directory",
    "modprobe: ERROR: could not insert 'module': Required key not available",
    "grub-install: error: failed to get canonical path of `/boot/grub'",
    "useradd: Permission denied.",
    "passwd: Authentication token manipulation error",""
    ]

#ansis
# Foreground Colors (Text)
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
ORANGE = '\033[38;2;255;165;0m'

# Background Colors
BLACK_BG = '\033[40m'
RED_BG = '\033[41m'
GREEN_BG = '\033[42m'
YELLOW_BG = '\033[43m'
BLUE_BG = '\033[44m'
MAGENTA_BG = '\033[45m'
CYAN_BG = '\033[46m'
WHITE_BG = '\033[47m'

# Bright Foreground Colors (Text)
BRIGHT_BLACK = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
BRIGHT_WHITE = '\033[97m'

# Bright Background Colors
BRIGHT_BLACK_BG = '\033[100m'
BRIGHT_RED_BG = '\033[101m'
BRIGHT_GREEN_BG = '\033[102m'
BRIGHT_YELLOW_BG = '\033[103m'
BRIGHT_BLUE_BG = '\033[104m'
BRIGHT_MAGENTA_BG = '\033[105m'
BRIGHT_CYAN_BG = '\033[106m'
BRIGHT_WHITE_BG = '\033[107m'

# 256 Colors (Example)
COLOR_256 = lambda x: f'\033[38;5;{x}m'  # Foreground 256 Color
BACKGROUND_256 = lambda x: f'\033[48;5;{x}m'  # Background 256 Color

# Reset color
RESET = '\033[0m'

# main loop

print(f'''{ORANGE}

⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠋⠉⠁⠀⠀⠀⠀⠈⠉⠙⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿
⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣦⠀⠀⠀⠈⢻⣿⣿⣿
⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⣶⣾⣷⣶⣆⠸⣿⣿⡟⠀⠀⠀⠀⠀⠹⣿⣿
⣿⠃⠀⠀⠀⠀⠀⠀⣠⣾⣷⡈⠻⠿⠟⠻⠿⢿⣷⣤⣤⣄⠀⠀⠀⠀⠀⠀⠘⣿
⡏⠀⠀⠀⠀⠀⠀⣴⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣦⠀⠀⠀⠀⠀⠀⢹
⠁⠀⠀⢀⣤⣤⡘⢿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⡇⠀⠀⠀⠀⠀⠈
⠀⠀⠀⣿⣿⣿⡇⢸⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣉⣉⡁
⡀⠀⠀⠈⠛⠛⢡⣾⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡇⠀⠀⠀⠀⠀⢀
⣇⠀⠀⠀⠀⠀⠀⠻⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⠟⠀⠀⠀⠀⠀⠀⣸
⣿⡄⠀⠀⠀⠀⠀⠀⠙⢿⡿⢁⣴⣶⣦⣴⣶⣾⡿⠛⠛⠋⠀⠀⠀⠀⠀⠀⢠⣿
⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⠿⢿⡿⠿⠏⢰⣿⣿⣧⠀⠀⠀⠀⠀⣰⣿⣿
⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⠟⠀⠀⠀⢀⣼⣿⣿⣿
⣿⣿⣿⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣄⣀⡀⠀⠀⠀⠀⢀⣀⣠⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿
      
       UBUNTU LINUX TERMINAL SIMULATOR
      
      this is a simulation of a terminal
      work in progress, current version is: pre-alpha 0.1; expect some errors, bugs, etc..
      WIP
      {RESET}''')

while True:
    user_input = input("root@jp:~$ ")

    if user_input == "help":
        print(f'''{GREEN}
              Simulation help commands:
              help - shows this message
              sudo rm/rf/./* - deletes all files on the 'system'
              exit - exits the program
              ls - lists all files in your actual system (this is very cool)
              socials - shows the developper's socials
              {RESET}''')
        
    elif user_input == "socials":
        print(f"{BLUE}I'm glad you asked :)")
        print(f"{BLUE}Discord: @jpab9_")
        print(f"{BLACK}Github: @jpab9{RESET}")
        
    elif user_input == "ls":
        files = os.listdir(".")
        if files:
            print("  ".join(files)) 
        else:
            print("No files found in the current directory.")



    elif user_input == "sudo rm/rf/./*":
        i = 0
        while i < 100000: # copilot are you trying to break my pc? bro just added 5 more zeros to the end of 1000
            print(f"{RED}{random.choice(fancy_linux_messages)}{RESET}") 
            i += 1
        print(f'''{RED}Your system has fully crashed due to losing essential files. Your system will not turn off.{RESET}''')
        time.sleep(5)
        break
        


    elif user_input == "exit":
        break

    else:
        print(f"{RED}Unvaible command{RESET}")
        continue  # i just noticed im a fucking idiot, copilot, YOU DONT ADD BREAK TO TERMINALS, YOU ADD CONTINUE
