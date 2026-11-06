from .recipe import Recipe

def create_recipe(recipe_book):
    name = input("enter recipe name ")
    ingredients = input("enter ingredients in the format 'ingredient;amount' (comma seprated) ").split(',')
    steps = input("enter instructions (comma seprated) ").split(',')
    tags = input("enter tags (comma seprated) ").split(',')

    recipe_book.add(Recipe(name, ingredients, steps, tags))
