list = [4, 2, 3,3]

def findIndex():
    for i in range(len(list)):
        if list[i] == 2:
            index = i
    return index

print(findIndex())


fo = open("avatar_list.txt", "r")
print(fo.read())