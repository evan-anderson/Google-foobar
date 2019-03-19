def answer(s):
    '''
    
    Args:
        s (string): hallway string made up of ">", "-", "<"
    
    Return:
        count (int): number of salutes in a hallway
    
    '''
    #turn string into list
    l=[j for j in s if j=='<' or j=='>']
    
    #initialize count of salutes
    count=0
    
    #create a list in reverse
    l_rev=l[::-1]
    
    #creating a loop for each index in l
    for i in range(len(l)):
        # if we encounter '>' in the list, we count how many '<'
        # are in a higher index
        if l[i]=='>':
            for j in range(i,len(l)):
                if l[j]=='<':
                    count+=1
        # if we encoutner '<' in the reverse list, we count
        # how many '>' are in a higher index in the reverse list
        if l_rev[i]=='<':
            for k in range(i,len(l_rev)):
                if l_rev[k]=='>':
                    count+=1
    
    return count