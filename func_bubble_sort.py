import random

def bubble_sort(list):
    disp = ""
    for i in range(0,len(list)):
        disp = disp + str(list[i]) +" "
    print("ソート前:",disp)

    for i in range(len(list)-1,0,-1):
        for j in range(0,i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list

list = []
for i in range(10):
    x = random.randint(0,100)
    list.append(x)

list2 = bubble_sort(list)
disp = ""
for i in range(0,len(list2)):
    disp = disp + str(list2[i]) +" "
print("ソート後:",disp)
