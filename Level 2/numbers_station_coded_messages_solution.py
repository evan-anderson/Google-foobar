def answer(l,t):
    '''
    
    Args:
        l (list of ints): list of numbers to be added
        t (int): desired sum
    
    Return:
        inds (list of indexes): The starting and ending indexes which will sum to t from list l
    
    '''
    
    # We're looking for the first sublist of integers in l which sums up to t
    
    #we will loop through starting indexes for summing
    for i in range(0,len(l)-1):
        #we will also loop for the length of the sublist, starting with 1
        j=1
        while i+j<=len(l):
            
            #if we find something that sums to our desired key, we return it
            if sum(l[i:i+j])==t:
                #if the key happens to be a single number, we return a single index
                if j==1:
                    return [i]
                #otherwise we return the two indexes, adjusted from half-open to closed intervals
                else:
                    return[i,i+j-1]
            j+=1
    
    
    #if there is no sum of list items adding to the key
    return [-1,-1]

