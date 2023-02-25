from os import system
system("cls")
disk = ["home","system","config","backup"]
home_folder= ["pictures","music","docs"]
system_folder =["windows", "nvidia","adobe"]
config_folder =["temp","drivers","premiere"]
backup_folder =["system bk","home bk","config bk"]
print("/-.")
for i in range(4):
    suf=""
    if disk[i] == "home":
        suf = " -."
    print ("  +-- "+ disk[i]+suf)
    if disk[i]=="home":
        for j in range(3):
            suf=""
            print("  |         +-- "+home_folder[j])
            if j == 2: break
            print("  |         |")

    if disk[i]=="system":
        suf = " -."
        for k in range(3):
            print("  |           +-- "+system_folder[k])
            if k == 2: break
            print("  |           |")
    
        
    if disk[i]=="config":
        suf = " -."
        for l in range(3):                  
            print("  |           +-- "+config_folder[l])
            if l == 2: break
            print("  |           |")
    if disk[i]=="backup":
        suf = " -."
        for f in range(3):                  
            print("              +-- "+backup_folder[f])
            if f == 2: break
            print("              |")
    last_sp= i == len(disk)-1
    if last_sp == True:
        print("  ")
    else: print("  |")

