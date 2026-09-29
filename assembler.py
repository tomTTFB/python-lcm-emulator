

with open("program.txt") as f:
    for line in f:
        word = line.split()
        print(word)