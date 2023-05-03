spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = []
    for n in spicy_foods:
        names.append(n.get("name"))
    return(names)

def get_spiciest_foods(spicy_foods):
    tongue_burners = [n for n in spicy_foods if n.get("heat_level") > 5]
    return(tongue_burners)

def print_spicy_foods(spicy_foods):
    for n in spicy_foods:
        print(f'{n.get("name")} ({n.get("cuisine")}) | Heat Level: {"🌶" * n.get("heat_level")}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for n in spicy_foods:
        if n["cuisine"] == cuisine:
            return n
     

def print_spiciest_foods(spicy_foods):
    tongue_burners = [n for n in spicy_foods if n.get("heat_level") > 5]
    for n in tongue_burners:
        print(f'{n.get("name")} ({n.get("cuisine")}) | Heat Level: {"🌶" * n.get("heat_level")}')


def get_average_heat_level(spicy_foods):
    heat_list = [n.get("heat_level") for n in spicy_foods]
    return sum(heat_list) / len(heat_list)
    

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
