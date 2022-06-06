import random as r
import json as j
from os.path import expanduser

stats_file_dir = rf"{expanduser('~')}/.tordle_stats"

with open("words.txt", "r") as file:
    list1 = file.readlines()
filter1 = lambda x: len(x) == 5
map1 = lambda x: x.lower().replace("\n", "")
list1 = map(map1, list1)
words = list(filter(filter1, list1))

COLOR_LIST = ["_", "Y", "G"]
colorer = lambda x: COLOR_LIST[x]
def check(word1, word2):
    if word1 == word2:
        return 1
    if word2 not in words:
        return -1
    col_list = []
    for let1, let2 in zip(word1, word2):
        if let1 == let2:
            col_list.append(2)
        elif let2 in word1:
            col_list.append(1)
        else:
            col_list.append(0)
    return col_list
try:
    with open(stats_file_dir, "r") as file:
        # 1 2 3 4 5 6 losses
        stats = j.load(file)
except:
    stats = [0, 0, 0, 0, 0, 0, 0]

print("Welcome to Tordle, the terminal version of Wordle.")
print("Stats:")
print(f"One Guesses:\t{stats[0]}")
print(f"Two Guesses:\t{stats[1]}")
print(f"Three Guesses:\t{stats[2]}")
print(f"Four Guesses:\t{stats[3]}")
print(f"Five Guesses:\t{stats[4]}")
print(f"Six Guesses:\t{stats[5]}")
print(f"Losses:\t\t{stats[6]}")
print("-----------------------------------------------")

while True:
    ans = r.choice(words)
    for i in range(6):
        while True:
            inp = input(f"Enter Guess [{6-i} tries left]:\n").lower()
            col_list = check(ans, inp)
            if col_list != -1:
                break
            else:
                print("Invalid Word")
        if col_list == 1:
            print(f"Congrats it took you {i+1} tries to guess {ans}!!!")
            stats[i] += 1
            break
        else:
            print("".join(map(colorer, col_list)))
    if col_list != 1:
        print(f"Out of tries. Word was {ans}.")
        stats[-1] += 1
    with open(stats_file_dir, "w") as file:
        j.dump(stats, file, indent=0)
    print("-----------------------------------------------")
    print("Stats:")
    print(f"One Guesses:\t{stats[0]}")
    print(f"Two Guesses:\t{stats[1]}")
    print(f"Three Guesses:\t{stats[2]}")
    print(f"Four Guesses:\t{stats[3]}")
    print(f"Five Guesses:\t{stats[4]}")
    print(f"Six Guesses:\t{stats[5]}")
    print(f"Losses:\t\t{stats[6]}")
    print("-----------------------------------------------")
