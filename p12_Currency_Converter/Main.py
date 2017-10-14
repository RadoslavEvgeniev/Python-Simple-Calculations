value = float(input())
inputCurrency = input()
outputCurrency = input()

if inputCurrency == "BGN":
    value = value * 1
elif inputCurrency == "USD":
    value *= 1.79549
elif inputCurrency == "EUR":
    value *= 1.95583
elif inputCurrency == "GBP":
    value *= 2.53405

if outputCurrency == "BGN":
    value /= 1
elif outputCurrency == "USD":
    value /= 1.79549
elif outputCurrency == "EUR":
    value /= 1.95583
elif outputCurrency == "GBP":
    value /= 2.53405

print("{0:.2f} {1}".format(value, outputCurrency))
