from app.recipe_book import RecipeBook
from app.recipe_creator import create_recipe

def main():
    print("\nWelcome to the recipe book\n")
    option = ''

    recipe_book = RecipeBook.load_recipe_book()
    if recipe_book is None:
        recipe_book = RecipeBook([])

    while option != 'q':
        print("'c': Create a new recipe\n'v': View recipes\n's': Save recipe book\n'q': Quit the app\n\n")

        if not recipe_book.saved:
            print("WARNING: UNSAVED CHANGES TO YOUR RECIPE BOOK. SAVE RECOMMENDED\n\n")

        option = input()

        if option == 'c':
           create_recipe(recipe_book)

        elif option == 'v':
            for recipes in recipe_book.recipes:
                print(recipes.name)

        elif option == 's':
           recipe_book.save_recipe_book()

        elif option == 'q':
            print("Quitting app.")
            
        else:
            print("Error, please enter c, v, s, or q.")

if __name__ == "__main__":
    main()