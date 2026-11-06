import pickle
from .recipe import Recipe

class RecipeBook:
    def __init__(self, recipes):
        self.recipes = recipes
        self.saved = True

    def add(self, recipe):
        self.recipes.append(recipe)
        self.saved = False
    
    def remove(self, recipe):
        self.recipes.remove(recipe)
        self.saved = False
    
    def __eq__(self, x):
        if not isinstance(x, RecipeBook):
            return False
        return self.recipes == x.recipes
    
    def save_recipe_book(self):
        self.saved = True
        try:
            with open("recipeBook.pickle", 'wb') as file:
                pickle.dump(self, file)
        except (pickle.PicklingError):
            self.saved = False
            print("Save failed.")
            return False
        return True

    @classmethod
    def load_recipe_book(cls):
        try:
            with open("recipeBook.pickle", 'rb') as file:
                recipe_book: RecipeBook = pickle.load(file)
        except FileNotFoundError:
            return None
        except (pickle.UnpicklingError, EOFError, AttributeError, ImportError):
            print("Save file is corrupted or unreadable.")
            return None
        recipe_book.saved = True
        return recipe_book