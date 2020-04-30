text = "X-DSPAM-Confidence:    0.8475"
fiveposition = text.find("5")
# print(fiveposition)
zeroposition = text.find("0")
# print(zeroposition)
number = text[zeroposition:]
print(float(number))
