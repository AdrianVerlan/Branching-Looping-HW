from os import system

system('cls')

robot_lvl = 5

robot_dir ="down"
robot_has_box = True
nr_boxes= 3
for level in range(10):
    if robot_lvl -1 == level and robot_dir =="up":
        print("▲")
    elif robot_lvl == level:
        print("■", end=" ")
        if robot_has_box:
            print("◍ "* nr_boxes, end="\n")
    elif robot_lvl +1 == level and robot_dir =="down":
        print("▼")
    else:
        print("□")