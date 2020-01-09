import threading
import random
import os
import time

mutex = threading.Lock()
tree = list(open('treeTemplate.txt').read().rstrip())

def formatColor(color):
    if color == 'Y':
        return f'\033[93m⏺\033[0m'
    if color == 'R':
        return f'\033[91m⏺\033[0m'
    if color == 'G':
        return f'\033[92m⏺\033[0m'
    if color == 'B':
        return f'\033[94m⏺\033[0m'
        
def lights(color):
    indexes = lightList[color]
    lightOff = True
    
    while True:
        for index in indexes:
            tree[index] = formatColor(color) if lightOff else '⏺'

        # Critical section
        mutex.acquire()
        os.system('cls' if os.name == 'nt' else 'clear') # Clears screen
        print(''.join(tree))
        mutex.release()
        
        lightOff = not lightOff
        time.sleep(random.uniform(0.5, 1.5)) # Randomness of light blink

lightList = { # Dictionary of indices of lights on tree
    "Y": [],
    "R": [],
    "G": [],
    "B": []
}

threadList = { # Dictionary of various color threads
    "Y": threading.Thread(target=lights, args=("Y")),
    "R": threading.Thread(target=lights, args=("R")),
    "G": threading.Thread(target=lights, args=("G")),
    "B": threading.Thread(target=lights, args=("B"))
}

for index, char in enumerate(tree):
    if char in "YRGB":
        lightList[char].append(index)
        tree[index] = '⏺'

for thread in threadList.values():
    thread.start()
for thread in threadList.values():
    thread.join()
