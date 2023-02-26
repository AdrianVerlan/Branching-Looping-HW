PARKING_PLACES = 7
FREE_PLACE = 3

print("#"*PARKING_PLACES*5)

for place_index in range(1, PARKING_PLACES + 1):
    if place_index == FREE_PLACE:
       print("|   |", end="")
    else :
        print("| X |", end="")
    

print("\n","#"*PARKING_PLACES*5, sep="")

# sep="" argumentul sep poate fi folosit pentru personaliza afisarea datelor in functia print
# in cazul dat este folosit ca sa nu existe nici un spatiu intre caractere.
# diferenta dintre end si sep este ca end se foloseste pentru a afisa caracterele de la sfirsitul 
# afisarii iar sep pentru a seta delimitatorul in toate elementele din print