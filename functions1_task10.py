def unique (lst): 
    uniquelist=[]
    for item in lst:
        if item not in uniquelist:
            uniquelist.append(item)
    return uniquelist

sequence=list(map(int, input("Enter numbers in any order: ").split()))
print(unique(sequence))