vards=input('Ievadi savu vārdu: ')
with open('5user.txt', 'w') as f:
    f.write(vards)
    if FileNotFoundError:
        print("Fails neeksistē vai nav atrasts!")