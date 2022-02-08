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
        	for ing in self.ingredients:
        		if ing.name.lower() == ingredient_name.lower():
        			return ing
        		

    def adjust_numbers(self, basis_ingredient_name, quantity_in_fridge, unit):
    	rat = 0.0
        for ing in self.ingredients:
        	if ing.name.lower() == basis_ingredient_name.lower():
        		if unit != ing.unit:
        			if unit == 'kg':
        				rat = float((quantity_in_fridge*1000)/ing.quantity)
        			else:
        				rat = float(quantity_in_fridge/(ing.quantity*1000))
        		else:
        			rat = float(quantity_in_fridge/ing.quantity)
        		break
        self.min_servings = round(self.min_servings*rat)
        self.max_servings = round(self.max_servings*rat)
        for ing in self.ingredients:
        	ing.quantity *= rat
        	if ing.quantity == 'kg' and ing.quantity < 1000:
        		ing.unit = 'g'
        		ing.quantity *= 1000
        	if ing.quantity == 'g' and ing.quantity >= 1000:
        		ing.unit = 'kg'
        		ing.quantity /= 1000

class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity  # quantity prescribed by the recipe
        self.unit = unit

    def get_ratio(self, quantity_in_fridge, unit):
        if self.unit in ['kg','g']:
        	if self.unit == 'kg' and unit == 'g':
        		return quantity_in_fridge/(self.quantity*1000)
        	elif self.unit == 'g' and unit == 'kg':
        		return (quantity_in_fridge*1000)/self.quantity
        	return quantity_in_fridge/self.quantity
        else:
        	return quantity_in_fridge/self.quantity

    def adjust(self, ratio):
        if self.unit in ['kg', 'g']:
            self.quantity *= ratio
            if self.unit == 'kg' and self.quantity < 1000:
            	self.unit = 'g'
            	self.quantity *= 1000
            if self.unit == 'g' and self.quantity >= 1000:
            	self.unit = 'kg'
            	self.quantity /= 1000
        else:
            self.quantity = round(self.quantity*ratio)

    def __eq__(self, other):
        # don't remove, needed by the test cases
        return isinstance(other, Ingredient) and \
               self.name == other.name and \
               abs(self.quantity - other.quantity) <= 0.001 and \
               self.unit == other.unit
