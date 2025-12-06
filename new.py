 

# import time
# import sys

# def print_lyrics():
#     lyrics = [
#         "Khamoshiyan......Ek Saaz Hai",
#         "Goonj Dhun Koi Laao Zaraa...",
#         "Khamoshiyan.........Alfaaz Hai",
#         "Kabhi Aa Gunguna Le Zaraa...",
#         "Beqrar Hain.........Baat Karne Ko..",
#         "Kahne Do Inko Zaraa..........",
#         "Khamoshiyan....."
#     ]

#     delays = [1.2, 1.8, 1.8, 2.0, 1.3, 2.0, 1.0]

#     print("Khamoshiyan:\n")
#     time.sleep(1.4)

#     for i, line in enumerate(lyrics):
#         for char in line:
#             sys.stdout.write(char)
#             sys.stdout.flush()
#             time.sleep(0.11)
#         print()
#         time.sleep(delays[i])

# print_lyrics()




# import time
# import sys
# from colorama import Fore, Style, init

# init(autoreset=True)

# def typewriter(text, delay=0.09, color=Fore.CYAN):
#     for char in text:
#         sys.stdout.write(color + char)
#         sys.stdout.flush()
#         time.sleep(delay)
#     print()

# def print_lyrics():

#     lyrics = [
#         "Khamoshiyan......Ek Saaz Hai",
#         "Goonj Dhun Koi Laao Zaraa...",
#         "Khamoshiyan.........Alfaaz Hai",
#         "Kabhi Aa Gunguna Le Zaraa...",
#         "Beqrar Hain.........Baat Karne Ko..",
#         "Kahne Do Inko Zaraa..........",
#         "Khamoshiyan....."
#     ]

#     delays = [1.2, 1.8, 1.7, 1.9, 1.4, 2.0, 1.2]

#     print(Fore.MAGENTA + "\n🎵 Khamoshiyan Lyrics 🎵\n")
#     time.sleep(1.2)

#     for i, line in enumerate(lyrics):
#         typewriter(line, delay=0.10, color=Fore.CYAN)
#         time.sleep(delays[i])

# print_lyrics()


import time
import sys
from colorama import Fore, Style, init

init(autoreset=True)

def typewriter(text, delay=0.07, color=Fore.CYAN):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

lyrics = [
    "Pal bhar theher jaao,\n",
    "Dil ye sambhal jaaye,\n",
    "Kaise tumhe roka karoon…\n",
    "Meri taraf aata,\n",
    "Har gham phisal jaaye,\n",
    "Aankhon mein tumko bharoon,\n",
    "Bin bole baatein tumse karoon…\n",
    "Agar tum saath ho…\n"
]

for line in lyrics:
    typewriter(line)
