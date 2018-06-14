import ex_1


def list_sheet(list):
    for i in range(len(list)):
        for k in range(len(list) * 7 + 1):
            print("_", end="")
        print()
        for j in range(len(list)):
            print("|", list[i][j], " ", end="")
        print("|")
    for k in range(len(list) * 7 + 1):
        print("_", end="")
