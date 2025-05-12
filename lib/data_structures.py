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
    return [f["name"] for f in spicy_foods]

def get_spiciest_foods(spicy_foods):
      return [f for f in spicy_foods if f["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        foodName = food["name"]
        foodCuisine = food["cuisine"]
        foodHeat = food["heat_level"] * "🌶"
        print(f"{foodName} ({foodCuisine}) | Heat Level: {foodHeat}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_average_heat_level(spicy_foods):
    heat_levels = [food["heat_level"] for food in spicy_foods]
    return sum(heat_levels) // len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_food = {
        'name': 'Griot', 'cuisine': 'Haitian', 'heat_level': 10
    }

    updated_list = spicy_foods + [spicy_food]

    return updated_list

