def answer(l):
    '''
    Args:
    l (list of ints): list of ascending intergers
    
    Return:
    Count (int): number of 'Triples'
    
    '''
    #initialize count of Triples
    count=0
    
    #the plan here is for every index i in l, 
    #look to see if there is an index ahead of it j for which l[j] is divisible by l[i]
    
    # if there is, then look to see if there is an index k ahead of j for which l[k] is divisable by l[j]
    # if this is also true, increase the counter
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[j]%l[i]==0:
                for k in range (j+1, len(l)):
                    if l[k]%l[j]==0:
                        #print([triple[i],triple[j],triple[k]]) - I was using this to see my triples
                        count+=1
    return count
