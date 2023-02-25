from os import system
system("cls")
disk = ["home","system","config","backup"]
home_folder= ["pictures","music","docs"]
print("/-.")
for i in range(4):
    suf=""
    if disk[i] == "home":
        suf == " -."
    print ("  +-- "+ disk[i]+suf)
    if disk[i]=="home":
        for j in range(3):
            
            print("  |         +-- "+home_folder[j])
            if j == 2: break
            print("  |         |")
    last_sp= i == len(disk)-1
    if last_sp == True:
        print("  ")
    else: print("  |")
