filename = input("Enter file name: ")
filehandle = open(filename)
wordlist = list()
for line in filehandle:
    for words in line.split():
        if words not in wordlist:
            wordlist.append(words)
wordlist.sort()
print(wordlist)
