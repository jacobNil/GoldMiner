import string

def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

#contentsToWrite = "This is a test!\nIt is only a test!"
#writeFile("record.txt", contentsToWrite)

fileContet = readFile("record.txt")

records = []
for line in fileContet.splitlines():
    record = []
    for word in line.split():
        record.append(word)
    records.append(record)

contentsToWrite = ""

for record in records:
    line = ""
    for item in record:
        if (len(line) == 0):
            line += item 
        else:
            line += " "+item
    contentsToWrite += line + "\n"


writeFile("record.txt", contentsToWrite)

print(records)






