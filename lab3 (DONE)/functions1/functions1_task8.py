def spygame(nums):
    sequence = [0, 0, 7]
    index = 0  
    
    for num in nums:
        if num == sequence[index]:
            index += 1  
            if index == len(sequence):  
                return True
    return False 

user_input = input("Enter a list of numbers: ")
nums = list(map(int, user_input.split()))
print(spygame(nums))