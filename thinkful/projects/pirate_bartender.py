import random


#Dictionaries

questions = {
    "Strong": "Do ye like yer drinks strong? yes/no?> ",
    "Salty": "Do ye like it with a salty tang? yes/no?> ",
    "Bitter": "Are ye a lubber who likes it bitter? yes/no?> ",
    "Sweet": "Would ye like a bit of sweetness with yer poison?> yes/no? ",
    "Fruity": "Are ye one for a fruity finish? yes/no?> ",
}

ingredients = {
    "Strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "Salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "Bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "Sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "Fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

"""
Drink Names
"""

adjectives = ["Fragrant", "Stinky", "Graceful", "Stupendous", "Raucous"]

nouns = ["Whale", "Shipyard", "Noose", "Captain", "Pearl"]


    
def drink_pref():    
    pref = {}
    for k,v in questions.items():
        response = input(v)
        if response == "yes":
            pref[k] = (response)
    return pref
               
def drink_ingre():        
    drink = []
    pref = drink_pref() 
    for key, value in pref.items():
        for key_ingr, value_ingr in ingredients.items():
            if key == key_ingr:
                drink.append(random.choice(value_ingr))
    return drink
       
def drink_name():
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    return adj, noun
        

def main():
    drink_limit = 0
    drink_tag = drink_name()
    while drink_limit <= 2:
        for each_drink_ingre in drink_ingre():
            print(each_drink_ingre)
        print("ARGGHH! I call this drink the {} {}".format(drink_tag[0],drink_tag[1])) 
        drink_limit += 1
    print("{} drinks is enough for you matey!".format(drink_limit))

if __name__ == "__main__":
    main()
