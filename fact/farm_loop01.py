farms = [{"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "E Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]}]

animals = ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]


def showNEFarmProd():
    for farm in farms:
        if farm["name"] == "NE Farm":
            for animals in farm["agriculture"]:
                print(animals)

def askUserAll():
    while True:
        userInput = input("Please choose a farm to see all: ").lower().strip()
        for farm in farms:
            if userInput ==  farm["name"].lower():
                for ani_plant in farm["agriculture"]:
                    print(ani_plant)
        break

def askUserAnimal():
    while True:
        userInput = input("Please choose a farm to see animals: ").lower().strip()
        for farm in farms:
            if userInput == farm["name"].lower():
                for element in farm["agriculture"]:
                     if element in animals:
                         print(element) 
                break
            else:
                print("Not animals there")
        break

showNEFarmProd()
askUserAll()
askUserAnimal()
