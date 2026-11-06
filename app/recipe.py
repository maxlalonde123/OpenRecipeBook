class Recipe:
    def __init__(self, name, ingredients, steps, tags):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps
        self.tags = tags
    
    def __eq__ (self, x):
        if not isinstance(x, Recipe):
            return False
        return (self.name == x.name
                and self.ingredients == x.ingredients
                and self.steps == x.steps
                and self.tags == x.tags)