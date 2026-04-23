# Create a class called food_item
# This is a template for storing nutrition information for each food
class food_item:

    # Runs automatically when a new food item is created
    def __init__(self, name, calories, protein, carbohydrates, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fat = fat

# Create a function to calculate totals from a list of foods eaten
def nutrition_tracker(food_list):

    # Start all totals at zero
    total_calories = 0
    total_protein = 0
    total_carbohydrates = 0
    total_fat = 0

    # Go through each food item in the list
    for food in food_list:

        # Add this food's calories to total calories
        total_calories += food.calories

        # Add this food's protein to total protein
        total_protein += food.protein

        # Add this food's carbohydrates to total carbohydrates
        total_carbohydrates += food.carbohydrates

        # Add this food's fat to total fat
        total_fat += food.fat

    # Print the final totals
    print("Total calories:", total_calories)
    print("Total protein:", total_protein, "g")
    print("Total carbohydrates:", total_carbohydrates, "g")
    print("Total fat:", total_fat, "g")

    # If calories are above healthy limit, print warning
    if total_calories > 2500:
        print("Warning: calorie intake is over 2500.")

    # If fat is above healthy limit, print warning
    if total_fat > 90:
        print("Warning: fat intake is over 90 g.")


# Create food objects using the class

# Food name, calories, protein, carbohydrates, fat
apple = food_item("Apple", 60, 0.3, 15, 0.5)

sandwich = food_item("Sandwich", 400, 20, 40, 15)

pizza = food_item("Pizza", 800, 35, 90, 30)

ice_cream = food_item("Ice Cream", 300, 5, 35, 18)

burger = food_item("Burger", 700, 30, 50, 35)

# Put all foods eaten in one list
foods_eaten = [apple, sandwich, pizza, ice_cream, burger]

# Run the nutrition tracker function using the list
print ("total foods eaten: ")
nutrition_tracker(foods_eaten)

#   optional user input 
foods = {
    "apple": apple,
    "sandwich": sandwich,
    "pizza": pizza,
    "ice_cream": ice_cream,
    "burger": burger
}

foods_eaten = input(
    "what foods have you eaten? (apple sandwich pizza ice_cream burger): "
)

# split text into separate words
food_names = foods_eaten.split()

chosen_foods = []

# check each typed food
for name in food_names:
    if name in foods:
        chosen_foods.append(foods[name])
    else:
        print(name, "not found")

# run tracker if at least one valid food entered
if len(chosen_foods) > 0:
    nutrition_tracker(chosen_foods)
else:
    print("No valid foods entered")