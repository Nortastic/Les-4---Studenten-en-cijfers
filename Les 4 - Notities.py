#Lijstje klein opdracht

#Met slicing:
# Boodschappen_lijstje = ['Melk' , 'Kaas' , 'Eieren' , 'Banaan' , 'Chocola']
# print(Boodschappen_lijstje[1:4])

# Einde slicing opdracht.

# karretje = []
# while len(Boodschappen_lijstje) > 0:
#     index = int(input(f"Welk item heb je gevonden Geef het index nummer tussen 0 en {len(Boodschappen_lijstje)-1}\n:"))
#     print(f"Het eerste item is: " , Boodschappen_lijstje[index])
#     karretje.append(Boodschappen_lijstje.pop(index))
#
# Dit is de eerste versie van de opdracht


# # print(f"Dit is het eerste artikel van dit lijstje {Boodschappen_lijstje[0]}")
# # print(f"Dit is het derde artikel van dit lijstje {Boodschappen_lijstje[2]}")
# #
# # #Of
# # print(f"Het eerste item is ", Boodschappen_lijstje[0])
# # print(f"Het eerste item is ", Boodschappen_lijstje[2])


# #Ander opdracht (Slicing):
# list_of_numbers = [1, 2, 3, 4, 5]
# print(f"De middelste 3 nummers uit de lijst: {list_of_numbers[1:4]}\n")
# print(f"De eerste 3 nummers uit de lijst: {list_of_numbers[:3]}\n")
# print(f"De tweede en de een-na-laatste uit de lijst: {list_of_numbers[1::6]}\n")
#
# print(f"Dit zijn oneven getallen, {list_of_numbers[::2]}\n")
# print(f"Dit zijn even gestallen, {list_of_numbers[1::2]}\n")

#For Loop
# for number in list_of_numbers:
#     print(f"{number} keer = {number * 2}")

# stellen = [("Brad", "Angelina"), ("Kees" , "Jan"), ("Rob", "Argentijn")]
# for partner1, partner2 in stellen:
#     print(f"{partner1} is getrouwd met {partner2}")
#
# for partners in stellen:
#     print(f"{partners[0]} is getrouwd met {partners[1]}")

#
# Break en continue
# numbers = [1,2,3,4,5]
# for number in numbers:
#     if number == 3:
#         break
#     print(f"{number} is number")
#
#
# print("Out of loop")
# numbers = [1,2,3,4,5]
# for number in numbers:
#     if number == 3:
#         continue
#     print('number is ' + str (number))
#
# print("Out of loop")

#Uitzonderingen
studenten = ["lion", "Norbert" , "Bas" , "Oguzhan" , "Reduan"]
for student in studenten:
    if student == "Reduan":
        continue
    print("Welkom " + student)

#kwadrateren.
getallen = [1,2,3,4,5]
kwadraten = [x**2 for x in  getallen]
print(kwadraten)

getallen = [1,2,3,4,5,6]
even_getallen_dubbel = [x*2 for x in getallen if x % 2 == 0]
print(even_getallen_dubbel)

