import math
class Recipe:
    def __init__(self, name, min_servings, max_servings):
        self.name = name
        self.min_servings = min_servings
        self.max_servings = max_servings
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def find_ingredient(self, ingredient_name):
        try:
            for i in self.ingredients:
                if i.name.lower() == ingredient_name.lower():
                    return i
        except ValueError:
            raise ingredient_name + ' not part of the recipe.'
            return

    def adjust_numbers(self, basis_ingredient_name, quantity_in_fridge, unit):
        rate = 0.000
        for i in self.ingredients:
            if i.name.lower() == basis_ingredient_name.lower():
                if i.unit == 'g' and unit == 'kg':
                    rate = float((float(quantity_in_fridge)*1000)/float(i.quantity))
                elif i.unit == 'kg' and unit == 'g':
                    rate = float(float(quantity_in_fridge)/(float(i.quantity)*1000))
                else:
                    rate = float(float(quantity_in_fridge)/float(i.quantity))
        self.min_servings = round(self.min_servings*rate)
        self.max_servings = round(self.max_servings*rate)
        for i in range(len(self.ingredients)):
            if self.ingredients[i].unit != 'g' and self.ingredients[i].unit != 'kg':
                self.ingredients[i].quantity = math.ceil(self.ingredients[i].quantity*rate)
            else:
                if self.ingredients[i].unit == 'g' and math.ceil(self.ingredients[i].quantity*rate) >= 1000:
                    self.ingredients[i].quantity = math.ceil(self.ingredients[i].quantity*rate)/1000
                    self.ingredients[i].unit = 'kg'
                elif self.ingredients[i].unit == 'kg' and math.ceil(self.ingredients[i].quantity*rate) < 1000:
                    self.ingredients[i].quantity = math.ceil(self.ingredients[i].quantity*rate)
                    self.ingredients[i].unit = 'g'
                else:
                    self.ingredients[i].quantity = math.ceil(self.ingredients[i].quantity*rate)

class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity  # quantity prescribed by the recipe
        self.unit = unit

    def get_ratio(self, quantity_in_fridge, unit):
        if self.unit in ['kg','g']:
            if self.unit == 'kg' and unit == 'g':
                return float((quantity_in_fridge)/(self.quantity*1000))
            elif self.unit == 'g' and unit == 'kg':
                return float((quantity_in_fridge*1000)/(self.quantity))
            return float((quantity_in_fridge)/(self.quantity))
        else:
            return float(quantity_in_fridge/self.quantity)
        # e.g. if recipe requires 800g chicken, but you have 1.2kg, then ratio is 1.5
        # e.g. if recipe requires 800g chicken, but you only have 300g, then ratio is 0.375

    def adjust(self, ratio):
        if self.unit in ['kg', 'g']:
            if self.unit == 'kg' and ratio < 1.00:
                self.unit = 'g'
                self.quantity = self.quantity*1000*ratio
            elif self.unit == 'g' and self.quantity*ratio >= 1000:
                self.unit = 'kg'
                self.quantity = (self.quantity*ratio)/1000.0
            else:
                self.quantity = (self.quantity*ratio)
        elif self.unit in ['cloves', 'pcs']:
            self.quantity = self.quantity*ratio
        else:
            pass

    def __eq__(self, other):
        # don't remove, needed by the test cases
        return isinstance(other, Ingredient) and \
               self.name == other.name and \
               abs(self.quantity - other.quantity) <= 0.001 and \
               self.unit == other.unit

recipe = Recipe('Chicken with Mushroom and Brocolli', 3, 4)
recipe.add_ingredient(Ingredient('Chicken', 1, 'kg'))
recipe.add_ingredient(Ingredient('Brocolli', 400, 'g'))
recipe.add_ingredient(Ingredient('Water', 4, 'cups'))
recipe.add_ingredient(Ingredient('Mushroom', 300, 'g'))
recipe.add_ingredient(Ingredient('Garlic', 6, 'cloves'))
recipe.adjust_numbers('chicken', 400, 'g')

print(recipe.min_servings)
print(recipe.ingredients)
