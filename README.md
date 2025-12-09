```zsh
~/17❯ whoami 
▗▄▄▖  ▗▄▖ ▗▖ ▗▄▄▄▖▗▖ ▗▖▗▄▄▄▖ ▗▄▖ ▗▄▄▄  
▐▌ ▐▌▐▌ ▐▌▐▌   █  ▐▌ ▐▌▐▌   ▐▌ ▐▌▐▌  █ 
▐▛▀▚▖▐▌ ▐▌▐▌   █  ▐▛▀▜▌▐▛▀▀▘▐▛▀▜▌▐▌  █ 
▐▙▄▞▘▝▚▄▞▘▐▙▄▄▖█  ▐▌ ▐▌▐▙▄▄▖▐▌ ▐▌▐▙▄▄▀ 

~/17❯ uname -a
Linux boltman 6.17.9-arch1-1 #1 SMP x86_64 GNU/Linux

~/17❯ nvim aboutMe.py
#!/usr/bin/env python3

class AboutMe:
    def __init__(self):
        self.name = "bolthead"
        self.location = "/home/the-grid"
        self.age = 17
        self.langs = {
            "Python": "getting a good enough grip", # NOTE: I don't care 'bout PEP8 Rules
            "Bash":   "starting to like it [ but it's very weird... honestly ]",
            "C":      "printf('just getting started\n');"
        }
        self.setup = {
            "OS":       "Arch BTW",
            "WM":       "Hyprland",
            "Editor":   "Neovim", 
            "Shell":    "zsh",
            "Terminal": "kitty"  # only kitty I can have.
        }
        self.vibe = "CLI > GUI"
        self.mbti = "INFP > INTP"
^[:wq

~/17❯ ./aboutMe.py
zsh: permission denied: ./aboutMe.py

~/17❯ nvim -r
Found swap files:
   1. ~/docs/notes/shuttle/25-12-07.md (Dec 07 20:41)
      "I've always dreamt about being normal... but that's impossible."
   2. heart.c (Dec 01 11:08)
      "// it's like... everythin stopped for 5!"
   
~/17❯ ls --width 1 
 grace -- learnin' area... python, c!
 cinephile -- it's hard to put in a nutshell.
 dots -- my dotfiles... BONUS: scripts in there too...

~/17❯ grep -r "quote" ~/vids/movies
QUOTE: "I fight for the users." - Tron

~/17❯ ./checkStatus.sh
ERROR: motivation.service failed to start
  at /home/boltman/life.py (line 18)
  at https://linktr.ee/bolthead (segfault)

Attempting restart in 5... 4... 3... 2...
^C

~/17❯ sudo shutdown now
[sudo] password for boltman:
```

_Alright it's time to grab some coffee... or actually study... or maybe movies... I don't know!!!_

\[NOW PLAYING] Shadow Over Me -- Nine Inch Nails (TRON: Ares)

**END OF LINE**
