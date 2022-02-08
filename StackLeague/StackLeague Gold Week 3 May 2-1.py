def parse_molecule(formula):
	dct = {}
	cnt, i = -1, 0
	st = ''
	while i < len(formula):
		if formula[i] == '(' or formula == '[' or formula == '{':
			qct = parse_molecule(formula[i+1:])
		elif formula[i] == ')' or formula == ']' or formula == '}':
			qt = 0
			while formula[i+1].isnumeric():
				i += 1
				qt = qt*10 + 
			return dct
		elif formula[i].isalpha():
			if st != '':
				if st not in dct:
					dct[st] = (1 if cnt == -1 else cnt)
				else:
					dct[st] += (1 if cnt == -1 else cnt)
			if formula[i].isupper() and st == '':
				st += formula[i]
			if formula[i+1].isalpha() and formula[i+1].isupper():
				st += formula[i+1]
				i += 1
		else:



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
		except ValueError:
			raise ingredient_name + ' not part of recipe.'

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
        return isinstance(other, Ingredient) and self.name == other.name and abs(self.quantity - other.quantity) <= 0.001 and self.unit == other.unit


def test___OO___add_ingredients(self):
    recipe = Recipe('Chicken with Mushroom and Brocolli', 3, 4)
    recipe.add_ingredient(Ingredient('Chicken', 1, 'kg'))
    recipe.add_ingredient(Ingredient('Brocolli', 400, 'g'))

    self.assertEqual(recipe.ingredients, [
        Ingredient('Chicken', 1, 'kg'),
        Ingredient('Brocolli', 400, 'g')
    ])

def test___OO___get_ratio_1(self):
    apple = Ingredient('apple', 5, 'pcs')
    self.assertEqual(apple.get_ratio(2, 'pcs'), 0.4)

def test___OO___get_ratio_2(self):
    apple = Ingredient('apple', 5, 'kg')
    self.assertEqual(apple.get_ratio(500, 'g'), 0.1)

def test___SE___adjust_make_grams(self):
    chicken = Ingredient('chicken', 2, 'kg')
    chicken.adjust(0.3)
    self.assertEqual(chicken, Ingredient('chicken', 600, 'g'))

def test___SE___adjust_make_kilograms(self):
    chicken = Ingredient('chicken', 500, 'g')
    chicken.adjust(3)
    self.assertEqual(chicken, Ingredient('chicken', 1.5, 'kg'))

def test___SE___adjust_retain_kilograms(self):
    chicken = Ingredient('chicken', 2, 'kg')
    chicken.adjust(1.5)
    self.assertEqual(chicken, Ingredient('chicken', 3, 'kg'))

def test___SE___adjust_retain_grams(self):
    chicken = Ingredient('chicken', 500, 'g')
    chicken.adjust(1.25)
    self.assertEqual(chicken, Ingredient('chicken', 625, 'g'))

def test___AL___find_ingredient(self):
    recipe = Recipe('Chicken with Mushroom and Brocolli', 3, 4)
    recipe.add_ingredient(Ingredient('Chicken', 1, 'kg'))
    recipe.add_ingredient(Ingredient('Brocolli', 400, 'g'))
    recipe.add_ingredient(Ingredient('Water', 3, 'cups'))
    recipe.add_ingredient(Ingredient('Mushroom', 300, 'g'))
    recipe.add_ingredient(Ingredient('Garlic', 3, 'cloves'))

    self.assertEqual(recipe.find_ingredient('Water'), Ingredient('Water', 3, 'cups'))

def test___SL___find_ingredient(self):
    recipe = Recipe('Chicken with Mushroom and Brocolli', 3, 4)
    recipe.add_ingredient(Ingredient('Chicken', 1, 'kg'))
    recipe.add_ingredient(Ingredient('Brocolli', 400, 'g'))
    recipe.add_ingredient(Ingredient('Water', 3, 'cups'))
    recipe.add_ingredient(Ingredient('Mushroom', 300, 'g'))
    recipe.add_ingredient(Ingredient('Garlic', 3, 'cloves'))

    self.assertEqual(recipe.find_ingredient('MUSHROOM'), Ingredient('Mushroom', 300, 'g'))

def test___AL___adjust_numbers(self):
    recipe = Recipe('Chicken with Mushroom and Brocolli', 3, 4)
    recipe.add_ingredient(Ingredient('Chicken', 1, 'kg'))
    recipe.add_ingredient(Ingredient('Brocolli', 400, 'g'))
    recipe.add_ingredient(Ingredient('Water', 4, 'cups'))
    recipe.add_ingredient(Ingredient('Mushroom', 300, 'g'))
    recipe.add_ingredient(Ingredient('Garlic', 6, 'cloves'))
    recipe.adjust_numbers('chicken', 400, 'g')

    self.assertEqual(recipe.min_servings, 1)
    self.assertEqual(recipe.max_servings, 2)
    self.assertEqual(recipe.ingredients, [
        Ingredient('Chicken', 400, 'g'),
        Ingredient('Brocolli', 160, 'g'),
        Ingredient('Water', 1.6, 'cups'),
        Ingredient('Mushroom', 120, 'g'),
        Ingredient('Garlic', 3, 'cloves')
    ])

def test___AL___adjust_numbers_bigger(self):
    recipe = Recipe('Chicken with Mushroom and Brocolli', 3, 5)
    recipe.add_ingredient(Ingredient('Chicken', 1, 'kg'))
    recipe.add_ingredient(Ingredient('Brocolli', 400, 'g'))
    recipe.add_ingredient(Ingredient('Water', 3, 'cups'))
    recipe.add_ingredient(Ingredient('Mushroom', 300, 'g'))
    recipe.add_ingredient(Ingredient('Garlic', 6, 'cloves'))
    recipe.add_ingredient(Ingredient('Bell Pepper', 1, 'pcs'))
    recipe.adjust_numbers('mushroom', 1.2, 'kg')

    self.assertEqual(recipe.min_servings, 12)
    self.assertEqual(recipe.max_servings, 20)
    self.assertEqual(recipe.ingredients, [
        Ingredient('Chicken', 4, 'kg'),
        Ingredient('Brocolli', 1.6, 'kg'),
        Ingredient('Water', 12, 'cups'),
        Ingredient('Mushroom', 1.2, 'kg'),
        Ingredient('Garlic', 24, 'cloves'),
        Ingredient('Bell Pepper', 4, 'pcs')
    ])

def encode_rail_fence_cipher(s,n):
	lst = [[] for i in range(n)]
	rev, cnt = 1, 0
	for k in s:
		lst[cnt].append(k)
		cnt += rev
		if cnt == n-1 or cnt == 0:
			rev *= -1
	ans = ''
	for j in lst:
		ans += ''.join(j)
	return ans









