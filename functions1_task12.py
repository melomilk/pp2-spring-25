def histogram(lst):
    for num in lst:
        print('*' * num)  

user = list(map(int, input("Enter numbers: ").split()))
(histogram(user))