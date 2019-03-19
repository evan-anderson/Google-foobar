def answer(start, length):
    '''
    Args:
    start (int): ID number of first worker checked
    length (int): line capacity
    
    Return:
    checksum (int): checksum value for security check
    '''
    
    # initialize the list of IDs I'll end up checksumming
    checklist=[]
    
    # create the list of all numbers I'll be checksumming
    # the first part of the list is start to start + length -1
    # the next part of the list is start+length to start+length -2
    # and so on until we reach the line length
    for i in range(0,length):
        checklist.extend(list(range(start+i*length, start+i*length + length- i)))
    
    #initialize the checksum
    checksum=checklist[0]
    
    #sequentially checksum each id in the list
    for x in checklist[1:]:
        checksum=checksum^x
    return checksum
        
    
    