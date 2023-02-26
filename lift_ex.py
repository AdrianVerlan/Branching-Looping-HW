from os import system

DIR_UP =-1
DIR_STOPPED =0
DIR_DOWN =1

building_roof = False
building_floors =9
building_park = False

lift_flor = 7
lift_open = False
lift_dir  = DIR_UP

human_flor = 3
human_in_lift = False
system("cls")
if building_roof:
    
    print('---|-----|---')
    print(' R |     |   ')

    for floor in range (9,0,-1):
        print('---|     |---')
        print(f'{floor:^3}|     |   ')

else:
    
    for floor in range (9,0,-1):
        if floor == 9:
            print('---|-----|---') 
            print(' 9 |     |   ')  
        else:
            print('---|     |---')
            print(f'{floor:^3}|     |   ')
if building_park:
        print('---|     |---')
        print(' P |     |   ')
        print('---|-----|---')
else: print('---|-----|---')
    


#---|-----|---
# 9 |     |
#---|     |---
# 8 |     |
#---|     |---
# 7 |     |
#---|     |---
# 6 |     |
#---|     |---
# 5 |     |
#---|     |---
# 4 |     |
#---|     |---
# 3 |     |
#---|     |---
# 2 |     |
#---|     |---
# 1 |     |