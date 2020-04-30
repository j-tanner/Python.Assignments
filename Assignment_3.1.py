hrs = input("Enter Hours above 40:")
h = float(hrs)
csh = input("Enter Rate:")
c = float(csh)
if h < 1:
    print(40 * c)
else:
    print((40 * c) + (h * (1.5 * c)))