# Task 2
# Write a new function jainsall function that takes a list of throughput values
# (integers and/or float) and returns a JFI.

# Function Jainsall with list as argument
def jainsall(valuelist):
    # n er antall verdier i listen
    n = len(valuelist)
    # s er verdiene over brøkstrek
    s = 0
    # k er verdier under brøkstrek. Her må hvert tall opphøyes i to.
    k = 0

    # For løkke for å iterere over verdiene i listen.
    for x in valuelist:
        # Henter ut verdien som skal legges i s
        s = s + x
        # Henter ut verdien som skal legges til i k og opphøyes
        k = k + x ** 2

    result = (s ** 2) / (n * k)
    return result


# Liste med forskjellige verdier
tpVal = [2.2, 4, 5, 6, 7, 80, 55]

# Kaller på funksjonen
output = jainsall(tpVal)

# Printer resultate
print('The JFI is: ', output)
