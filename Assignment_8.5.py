filename = input("Enter file name: ")
if len(filename) < 1:
    filename = "mbox-short.txt"

filehandle = open(filename)
count = 0
for line in filehandle:
    line.rstrip()
    if line.startswith("From "):
        words = line.split()
        print(words[1])
        count = count + 1
print("There were", count, "lines in the file with From as the first word")
