def ftoc (f):
    c = (5 / 9) * (f - 32)
    return c

f = float(input("Enter fahrenheit temp: "))
print(ftoc(f))