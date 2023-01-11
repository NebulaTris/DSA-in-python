def ins_sort(ourlist):
    for x in range(1, len(ourlist)): 
        k = ourlist[x] 
        j = x-1
        while j >=0 and k < ourlist[j]: 
                ourlist[j+1] = ourlist[j] 
                j -= 1 
        ourlist[j+1] = k 
    return ourlist
        
ourlist = [15, 1, 9, 3]
ins_sort(ourlist)
