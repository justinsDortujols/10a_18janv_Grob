vards=input('Ievadi savu vārdu: ')
with open('5user.txt', 'w') as f:
    if FileNotFoundError:
        print("Fails neeksistē vai nav atrasts!")
        pass
    f.write(vards)
    print("Tavs vārds ir veiksmīgi ierakstīts failā!")