'''
Recipe Creator and Manager - Create a recipe class with ingredients and a put 
them in a recipe manager program that organizes them into categories like 
deserts, main courses or by ingredients like chicken, beef, soups, pies etc.

Author: Esha Uboweja
Date: June 13, 2015
'''

#------------------------------------------------------------------------------
# INGREDIENT class definition
#------------------------------------------------------------------------------
class Ingredient(object):
    def __init__(self, name, unit_of_measure):
        self.name = name
        self.unit_of_measure = unit_of_measure

    def __repr__(self):
        return "Name: " + self.name + ", Unit: " + self.unit_of_measure

#------------------------------------------------------------------------------
# RECIPE class definition
#------------------------------------------------------------------------------
class Recipe(object):
    def __init__(self, name):
        self.name = name
        self.ingredients = {}

    def addIngredient(self, ingredient, quantity = 1):
        self.ingredients[ingredient] = self.ingredients.get(ingredient, 0) + quantity

    def removeIngredient(self, ingredient, quantity):
        curQty = self.ingredients.get(ingredient, None)
        if curQty == None:
            print ingredient.name + " not in recipe"
        else:
            if quantity < curQty:
                self.ingredients[ingredient] -= quantity
            else:
                print "Removing " + ingredient.name + " from recipe"
                self.ingredients.pop(ingredient, None)

    def __str__(self):
        recipe = self.name + " recipe ingredients:\n"
        for ingredient in self.ingredients.keys():
            recipe += ingredient.name + " " + str(self.ingredients[ingredient]) \
                    + " " + ingredient.unit_of_measure + "\n"
        return recipe

#------------------------------------------------------------------------------
# RECIPE BOOK class definition
#------------------------------------------------------------------------------
class RecipeBook(object):
    def __init__(self, name):
        self.name = name
        self.recipes = {}

    def addRecipe(self, recipe, category):
        self.recipes[category] = self.recipes.get(category, []) + [recipe]

    def removeRecipe(self, recipe):
        self.recipes = filter(lambda r: r.name != recipe.name, self.recipes)

    def __str__(self):
        book = "* * * " + self.name + " Book of Recipes * * *\n"
        for category in self.recipes.keys():
            book += category.upper() + ":\n"
            for recipe in self.recipes[category]:
                book += str(recipe)
            book += "\n"
        book += "---- 'Stay hungry, stay foolish' ----"
        return book 

# Some tests
if __name__ == "__main__": 
    coffeePowder = Ingredient("Coffee Powder", "Teaspoons")
    sugar = Ingredient("Sugar", "Teaspoons")
    milk = Ingredient("Milk", "Cups")
    water = Ingredient("Water", "Cups")
    egg = Ingredient("Egg", "Pieces")
    onion = Ingredient("Onion", "Pieces")
    oil = Ingredient("Oil", "Teaspoons")


    # Recipe for 1 cup of coffee
    coffee = Recipe("Coffee")
    coffee.addIngredient(coffeePowder, 0.5)
    coffee.addIngredient(sugar, 1.0)
    coffee.addIngredient(milk, 0.5)
    coffee.addIngredient(water, 0.5)

    print coffee

    # Recipe for 1 omlette
    omlette = Recipe("Omlette")
    omlette.addIngredient(egg, 2)
    omlette.addIngredient(onion, 0.25)
    omlette.addIngredient(oil, 1)

    print omlette

    #menuCategories = ["Beverages", "Breakfast", "Lunch", "Dinner", "Dessert", "Specials"]
    book = RecipeBook("FunBuns")
    book.addRecipe(coffee, "Beverages")
    book.addRecipe(omlette, "Breakfast")
    
    print book 
