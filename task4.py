# Task 4
# Read the throughput values from a file and then use your jainsall function to calculate a JFI.
# Note: you must use the same units.

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
        s = float(x)
        # Henter ut verdien som skal legges til i k og opphøyes
        k = k + float(x) ** 2

    result = (s ** 2) / (n * k)
    return result


# Lager en tom liste.
data_into_list = []

# Legger in path til filen jeg skal lese med open og setter navn på filen.
with open("throughput2.txt") as file_name:
    # Bruker en for-løkke for å hente ut informasjonen
    for line in file_name:
        # split() deler opp teksten i string, hvor den splitter med mellomrom som default.
        a = line.split()
        if a[1] == "Mbps":
            # Legger bare til første del av verdien i en linje som er splittet.
            data_into_list.append(float(a[0]))
        else:
            x = float(a[0])
            y = (x / 1000)
            data_into_list.append(y)

    print(data_into_list)

# Kaller på funksjonen
output = jainsall(data_into_list)

# Printer resultate
print('The JFI is: ', output)
