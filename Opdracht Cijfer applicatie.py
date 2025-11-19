#Opdracht 1
studenten = [("Alice", 8.5), ("Bob", 7.0), ("Charlie",6.2), ("Diana", 9.1)]

for naam, cijfer in studenten:
    print(f'{naam} - {cijfer}')

cijfers = []
for student in studenten:
    # 0 = Naam
    # 1 = Cijfer
    naam = student[0]
    cijfer = student[1]
    cijfers.append(cijfer)

gemiddelde = sum(cijfers) / len(cijfers)
print(f'\nGemiddeld cijfer: {gemiddelde}')




