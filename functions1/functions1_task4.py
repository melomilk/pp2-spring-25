def is_prime(n):
    if n < 2:
        return False  
    for i in range(2, int(n ** 0.5) + 1):  
        if n % i == 0:
            return False  
    return True  

def filter_prime(numbers):
    return list(filter(is_prime, numbers))  

numbers = list(map(int, input("Enter numbers: ").split()))
print("Prime numbers are:", filter_prime(numbers))