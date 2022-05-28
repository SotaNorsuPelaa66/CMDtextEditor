print("")
print("Type ;123 to exit and save")
for i in range(10):
    print("")

def save():
    id = str(input("What filename?: "))
    codeLen = len(code)
    f = open(id, "w")
    for i in range(codeLen):
        f.write(code[i])
        print("Saving line: " + str(i))
    f.close()
    print("Saved!")
    exit()


code = []

while True:
    var = str(input())
    if var == ";123":
        save()

    code.append(var)