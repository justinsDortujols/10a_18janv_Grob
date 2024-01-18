faila_nosk=input("Ievadi faila nosaukumu: ")
faila_pap=input('Ievadi faila paplašinājumu: ')
with open(f"{faila_nosk}.{faila_pap}", 'r') as f:
    teksts = f.read()
    print(teksts)