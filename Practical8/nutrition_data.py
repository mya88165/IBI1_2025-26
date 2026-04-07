class food_item:
    def __init__(self, name, calories, protein, carbohydrates, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fat = fat

def nutrition_tracker(food_list):
    total_calories = 0
    total_protein = 0
    total_carbohydrates = 0
    total_fat = 0

    for food in food_list:
        total_calories += food.calories
        total_protein += food.protein
        total_carbohydrates += food.carbohydrates
        total_fat += food.fat

    print("Total calories:", total_calories)
    print("Total protein:", total_protein, "g")
    print("Total carbohydrates:", total_carbohydrates, "g")
    print("Total fat:", total_fat, "g")

    if total_calories > 2500:
        print("Warning: calorie intake is over 2500.")

    if total_fat > 90:
        print("Warning: fat intake is over 90 g.")

apple = food_item("Apple", 60, 0.3, 15, 0.5)
sandwich = food_item("Sandwich", 400, 20, 40, 15)
pizza = food_item("Pizza", 800, 35, 90, 30)
ice_cream = food_item("Ice Cream", 300, 5, 35, 18)
burger = food_item("Burger", 700, 30, 50, 35)

foods_eaten = [apple, sandwich, pizza, ice_cream, burger]
nutrition_tracker(foods_eaten)
