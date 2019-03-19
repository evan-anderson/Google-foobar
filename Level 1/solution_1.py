def answer(data,n):
    '''
    
    Args:
        data (list of ints): list of id numbers 
        n (int): max number of times doing a job
    
    Returns:
        solution (list of ints): new list of id numbers without entries repeated more than n times
    
    '''
    
    # I thought a list comprehension would work well for this problem.
    # To make a list omiting numbers which are present more than n times,
    # we just make a list comprehension that includes all numbers which occur
    # n or fewer times in the list
    solution = [i for i in data if data.count(i)<=n]
    return solution
