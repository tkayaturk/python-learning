import random
#
# #1
# names = ["Tolga", "Mert","Berkay","Kazim","Soner","Osman"]
#
# names = random.choice(names)
# print(names)
#
# #2
# food = ["Iskender" ,"Beyti","Sarma","Karniyarik","Fasulye"]
# print(food[random.randint(0,4)])
#
# #3
# names_other = ["Tolga", "Mert","Berkay","Kazim","Soner","Osman"]
# food_other = ["Iskender" ,"Beyti","Sarma","Karniyarik","Fasulye"]
#
# names_food = [names_other, food_other]
# print(names_food[0][3])

#4

# names= ["Tolga", "Mert","Berkay","Kazim","Soner","Osman"]
#
# names[-1]= "Mevlut"
#
# print(names)

#5

# zar = [1,2,3,4,5,6]
# zar_atma =input('Zar atmak icin Lutfen "Salla" yaziniz \n').lower()
#
# if zar_atma == "salla":
#     zar_sonucu = random.choice(zar)
#     print(zar_sonucu)
# else:
#     print("Sallayamadin")


zar_atma = input('Lutfen zar atmak icin "At" yazin \n' ).lower()

if zar_atma == "at":
    zar_sonucu= random.randint(1,6)
    print(zar_sonucu)
else:
    print("napiyorsun")