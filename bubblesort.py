def bubble_sort(ourlist): 
    b=len(ourlist)-1 
    for x in range(b): 
        for y in range(b-x): 
            if ourlist[y]>ourlist[y+1]: 
                ourlist[y],ourlist[y+1]=ourlist[y+1],ourlist[y] 
                                                         
        return ourlist
    
ourlist=[15,1,9,3]
bubble_sort(ourlist)
