#

def sort_strings(chaine):
    chaine.sort()
    for i in range(1,len(chaine)):
        if len(chaine[i-1]) > len(chaine[i]) :
            a = chaine[i]
            chaine.insert(chaine[i-1],i)
            chaine.insert(a,i-1)
    return chaine

print(sort_strings(["salma","aya","aylaa"]))


