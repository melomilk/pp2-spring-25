import os

with open('pp2_spring/lab6/examplefile.txt', 'r') as file:
    x = sum(1 for line in file)

print(x)
