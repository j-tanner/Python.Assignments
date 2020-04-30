def computepay(hoursworked, payrate):
    if hoursworked > 40:
        regular = 40 * payrate
        overtime = (hoursworked - 40.0) * (payrate * 1.5)
        pay = regular + overtime
    else:
        pay = hoursworked * payrate
    return pay


hw = float(input("Enter Hours: "))
pr = float(input("Enter Pay Rate: "))
xp = computepay(hw, pr)
print("Pay", xp)
